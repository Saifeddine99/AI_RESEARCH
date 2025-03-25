import os
import time
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai.llms import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import streamlit as st
from dotenv import load_dotenv
from functools import wraps
from collections import deque

# Load environment variables (Gemini API key)
load_dotenv()


#   Step 1: Load document content

def load_doc(file_bytes) -> str:
    save_file_name = "upload.pdf"

    # save file locally
    with open(save_file_name, "wb") as f:
        f.write(file_bytes.getvalue())

    doc = PyPDFLoader(save_file_name).load()
    
    doc = "\n\n".join([d.page_content for d in doc])
    return doc


#   Step 2: Summarise

def rate_limit(max_requests: int, window: float = 60.0):

    request_times = deque()

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            
            # Remove old requests outside the window
            while request_times and current_time - request_times[0] > window:
                request_times.popleft()
            
            # If we've hit the limit, wait until we can make another request
            if len(request_times) >= max_requests:
                sleep_time = request_times[0] + window - current_time
                if sleep_time > 0:
                    time.sleep(sleep_time)
                    request_times.popleft()
            
            # Add current request time and execute function
            request_times.append(current_time)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@rate_limit(max_requests=15)  # Limit to 15 requests per minute
# We'll be using cache to store the results of the summarisation
@st.cache_data(ttl=3600, show_spinner='Inferencing, Please Wait.....')
def summarise(doc_content: str) -> str:

    inference_date = time.time()

    # Load Gemini-1.5-flash model
    # API key is in the environment (.env file)
    model = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("API_KEY"), temperature=0)

    # prompt
    prompt = PromptTemplate.from_template("Provide a helpful summary of the contens provided by the user: {content}")

    # join prompt and model into a chain using LCEL
    summary_chain = prompt | model

    # Any LLM has a fixed context window, or the number of tokens it can take in one run.
    # If our file is bigger than context window, we need to split it in chunks
    # and summarise chunks individually and then combine them for complete summary.
    
    # Here, we take it to be 128,000 tokens almost 500,000 characters
    chunk_size = 500000

    if len(doc_content) > chunk_size:
        
        # Split into chunks
        doc_chunks = []
        for i in range(len(doc_content) // chunk_size + 1):
            doc_chunks.append(
                doc_content[i : min(
                    i+chunk_size,
                    len(doc_content) # The last chunk may not necessarily contain 500000 characters
                    )]
                )
            
        # Summarise each chunk
        chunk_summary = []
        for chunk in doc_chunks:
            chunk_summary.append(summary_chain.invoke({"content": chunk}))

        # Now let's summarise all chunks combined
        summary = summary_chain.invoke({"content": "\n\n".join(chunk_summary)})

    else:
        summary = summary_chain.invoke({"content": doc_content})
    
    return summary, inference_date
    

#   Streamlit server

def pdf_summarizing():
    st.title("LLM Document Summariser")
    st.info(": This app uses cache to store the results of the summarisation. The cache is cleared every hour.", icon="⚠️")
    st.info(": This app is rate limited to 15 requests per minute.", icon="⚠️")

    file = st.file_uploader(label="Upload document", type=['pdf'])
    if file:
        doc = load_doc(file)

        runtime = time.time()

        summary, inference_date = summarise(doc)
     
        if abs(inference_date - runtime) > 1:
            st.success("Result directly loaded from Cache!")
        else:
            st.info("Result returned after model inference!")

        st.write("## Summary")
        st.write(summary)


if __name__ == "__main__":
    pdf_summarizing()

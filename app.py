import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="AI Research Project",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    # Title and description
    st.markdown("""
             <div style='text-align: center; margin-bottom: 3rem; font-size: 4rem; font-weight: bold;'>AI Research Project
             </div>
             """,
            unsafe_allow_html=True)
    st.markdown("---")
    
    # PDF Link
    pdf_url = "https://arxiv.org/pdf/2503.13421"
    st.markdown(f"""
        <div style='text-align: center; margin-bottom: 3rem;'>
            <a href='{pdf_url}' target='_blank' style='color: #FF4B4B; text-decoration: none;'>
                📄 View Research Paper
            </a>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div style='text-align: center; padding: 20px; border: 1px solid #ddd; border-radius: 10px; margin-bottom: 3rem;'>
                <h3>🎧 Audio Conversation</h3>
                <p>Listen to the AI-generated discussion about the research paper</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='text-align: center; padding: 20px; border: 1px solid #ddd; border-radius: 10px; margin-bottom: 3rem;'>
                <h3>📝 PDF Summarizing</h3>
                <p>Get a detailed summary of the research paper</p>
            </div>
        """, unsafe_allow_html=True)

        
    
    selected = option_menu("Options", ["Audio Conversation", "PDF Summarizing"],
        icons=['headphones', 'file-earmark-text'],
        menu_icon="cast", default_index=0, orientation="horizontal")

    if selected == "Audio Conversation":
        from tasks.audio_conv_service import audio_conversation
        audio_conversation()
        
    elif selected == "PDF Summarizing":
        from tasks.pdf_summary_service import pdf_summarizing
        pdf_summarizing()

if __name__ == "__main__":
    main()
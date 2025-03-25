import streamlit as st
from pathlib import Path

def audio_conversation():
    st.title("🎧 Audio Conversation")
    st.markdown("---")
    
    # Setup message
    st.markdown("### My Setup Message: 👇👇")
    st.markdown("""
        <div style='padding: 20px; border: 2px solid #ddd; border-radius: 10px; margin-bottom: 2rem;'>
        Please analyze the selected research paper and generate an audio conversation script in dialogue format. 
        The dialogue should summarize the key findings, discuss the methodology, and highlight the significance of the paper. 
        Structure the dialogue as a conversation between two people, for example, a researcher and a student. 
        Ensure the audio script is clear, concise, and suitable for audio generation.
        </div>
    """, unsafe_allow_html=True)
    
    # Audio file path
    audio_file = "Optimal Expert Selection for Distributed Mixture-of-Experts.wav"
    
    if Path(audio_file).exists():
        st.markdown("### Listen to the AI-generated discussion")
        st.markdown("""
            Below you can listen to an AI-generated conversation discussing the research paper.
            The conversation provides insights and analysis of the key points in the paper.
        """)
        
        # Audio player
        st.audio(audio_file)
        
        # Additional information
        st.markdown("---")
        st.markdown("""
            ### About this Audio
            This audio was generated using NotebookLM, providing a natural conversation format
            that makes the research paper more accessible and engaging.
        """)
    else:
        st.error("Audio file not found. Please make sure the WAV file is in the correct location.")

if __name__ == "__main__":
    audio_conversation() 
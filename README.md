# AI Research Project 🤖

A Streamlit-based web application for analyzing and processing research papers using AI. The application provides two main features: audio conversations generated using Google NotebookLM and PDF summarization udsing Google Gemini 1.5 Flash.

## 🎥 Tutorial

Check out the video tutorial for this project [here](https://youtu.be/DgPA9EitUE8?si=-7wTRBik8DPvzWif).

## ✨ Features

### 1. Audio Conversation 🎧

- AI-generated discussion about research papers
- Natural dialogue format between a researcher and a student
- Easy-to-use audio player interface
- Focuses on key findings, methodology, and paper significance

### 2. PDF Summarization 📝

- Upload and process PDF research papers
- Intelligent text chunking for handling large documents
- Rate-limited API calls (15 requests per minute)
- Caching system for improved performance
- Powered by Google's Gemini 1.5 Flash model

## 🚀 Quick Start

### Prerequisites

- Python 3.x
- Gemini API key

### Running the Application

1. Clone the repository:

```bash
git clone https://github.com/Saifeddine99/AI_RESEARCH
cd AI_RESEARCH
```

2. Run the application:

**For macOS/Linux:**

```bash
chmod +x run.sh
./run.sh
```

**For Windows:**

- Double-click `run.bat`
- Or run it from command prompt:

```bash
run.bat
```

3. Add your Gemini API key to the `.env` file that was automatically created.

That's it! The script will automatically:

- Create a virtual environment
- Install all dependencies
- Start the application

## 🛠️ Project Structure

ai-research-project/
├── app.py # Main application file
├── tasks/
│ ├── audio_conv_service.py # Audio conversation functionality
│ └── pdf_summary_service.py # PDF summarization functionality
├── run.sh # Unix/Mac startup script
├── run.bat # Windows startup script
├── .gitignore # Git ignore file
├── requirements.txt # Project dependencies
└── .env # Environment variables (not tracked in git)

## 💡 Usage

1. Open the application in your web browser (automatically opened after running the script)
2. Choose between "Audio Conversation" or "PDF Summarizing"
3. For PDF summarization:
   - Upload a PDF research paper
   - Wait for the AI to process and generate the summary
   - View the cached results (cache refreshes hourly)
4. For Audio Conversation:
   - Listen to AI-generated discussions about the research paper
   - Follow along with the natural dialogue format

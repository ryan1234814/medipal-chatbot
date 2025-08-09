MediPal – Health & Medicine Assistant
Welcome to MediPal!
This project is a user-friendly health assistant web app designed to help elderly patients and anyone who wants easy access to medical information.
MediPal makes it simple to understand medicines, ask health questions, and even get summaries of lab reports.

 Features
Medicine Information Lookup:
Type in any medicine name and get a clear explanation of what it’s used for, its risks, and safety info.

General Health Q&A:
Ask any health-related question and get an answer powered by Google Gemini AI.

Lab Report Summarizer:
Upload your lab report (PDF or image) and get an easy-to-understand summary in plain language.

Multilingual Voice Chat:
Ask health questions by voice in English, Hindi, or Malayalam (requires a microphone).

Technologies Used
Python 3
Streamlit (for the web interface)
Flask (for backend API, if needed)
Google Gemini AI API (for all AI-powered answers)
PyMuPDF (fitz) (for extracting text from PDFs)
Pillow (for image handling)
Base64 (for sending images to Gemini)
SpeechRecognition (for voice chat)

How to Run
1 Clone this repository
git clone https://github.com/yourusername/medipal.git
cd medipal
2.Install dependencies
pip install -r requirements.txt
3.Set up your Gemini API key

Your API key is already in the code, but you can set it as an environment variable for security.

4.Run the app
python -m streamlit run app.py

5 (Optional) Run the Flask backend
python api.py


How to Use
Medicine Info:
Enter a medicine name and click "Check Medicine Info" to get details.

Ask Health Questions:
Type your question or use the voice chat feature to ask in your preferred language.

Lab Report Summary:
Upload a PDF or image of your lab report and get a simple summary.

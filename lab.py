import requests
from PIL import Image
import io
import fitz
import base64

GEMINI_API_KEY = "AIzaSyCMsmLd0V9t_k8Adb3ZvSZY1ULYvjVq0b0"
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
HEADERS = {"Content-Type": "application/json"}
PARAMS = {"key": GEMINI_API_KEY}

def extract_text_from_pdf(pdf_bytes):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_image(image_bytes):
    # Encode image as base64
    encoded_image = base64.b64encode(image_bytes).decode("utf-8")
    prompt = (
        "You are a medical assistant. The following is a base64-encoded image of a lab report. "
        "Extract the text from the image and provide a simple, easy-to-understand summary for a patient. Cover important aspects from each and every section of the report as well. "
        "Highlight any abnormal values and what they mean. "
        "Image (base64):\n" + encoded_image
    )
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    retries = 3
    delay = 2
    for attempt in range(retries):
        response = requests.post(GEMINI_URL, headers=HEADERS, params=PARAMS, json=data)
        if response.status_code == 200:
            result = response.json()
            return result["candidates"][0]["content"]["parts"][0]["text"]
        elif response.status_code == 503:
            import time
            if attempt < retries - 1:
                time.sleep(delay)
                continue
            else:
                return "The Gemini AI service is temporarily overloaded. Please try again in a few minutes."
        else:
            return f"Gemini API error: {response.text}"
    return "Failed to get a response from Gemini AI."

def summarize_lab_report(report_text):
    prompt = (
        "You are a medical assistant. Read the following lab report and provide a simple, easy-to-understand summary for a patient. "
        "Highlight any abnormal values and what they mean. Here is the report:\n\n"
        f"{report_text}\n\nSummary:"
    )
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    retries = 3
    delay = 2
    for attempt in range(retries):
        response = requests.post(GEMINI_URL, headers=HEADERS, params=PARAMS, json=data)
        if response.status_code == 200:
            result = response.json()
            return result["candidates"][0]["content"]["parts"][0]["text"]
        elif response.status_code == 503:
            import time
            if attempt < retries - 1:
                time.sleep(delay)
                continue
            else:
                return "The Gemini AI service is temporarily overloaded. Please try again in a few minutes."
        else:
            return f"Gemini API error: {response.text}"
    return "Failed to get a response from Gemini AI."

def process_lab_report(file):
    file_type = file.type
    if file_type == "application/pdf":
        report_text = extract_text_from_pdf(file.read())
        if not report_text.strip():
            return "Could not extract any text from the uploaded PDF file."
        summary = summarize_lab_report(report_text)
        return summary
    elif file_type.startswith("image/"):
        summary = extract_text_from_image(file.read())
        return summary
    else:
        return "Unsupported file type. Please upload a PDF or image."
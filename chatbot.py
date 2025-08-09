

def get_response(user_input):
    """Use Gemini API to answer general health questions."""
    import requests
    import time
    GEMINI_API_KEY = "AIzaSyCMsmLd0V9t_k8Adb3ZvSZY1ULYvjVq0b0"
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": GEMINI_API_KEY}
    prompt = f"Answer this general health question for a patient: {user_input}"
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    retries = 3
    delay = 2
    for attempt in range(retries):
        try:
            response = requests.post(url, headers=headers, params=params, json=data)
            if response.status_code == 200:
                result = response.json()
                return result["candidates"][0]["content"]["parts"][0]["text"]
            elif response.status_code == 503:
                if attempt < retries - 1:
                    time.sleep(delay)
                    continue
                else:
                    return "The Gemini AI service is temporarily overloaded. Please try again in a few minutes."
            else:
                return f"Gemini API error: {response.text}"
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(delay)
                continue
            return f"Gemini API exception: {e}"

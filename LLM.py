import requests

# LLaMA 3 model served via Ollama on your machine
OLLAMA_API_URL = "http://localhost:11434/api/generate"

def evaluate_note(prompt: str) -> str:
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        return response.json().get("response", "No response from model.")
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

if __name__ == "__main__":
    print("🧠 LLM-Powered Currency Verifier")

    try:
        user_input = ""
        while True:
            line = input()
            user_input += line + "\n"
    except EOFError:
        pass

    print("\n🔍 Evaluating currency features...\n")
    result = evaluate_note(user_input.strip())
    print("📝 Result:\n")
    print(result)

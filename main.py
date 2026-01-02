from flask import Flask, render_template, jsonify, request
from google import genai

# ✅ Gemini client (API key directly for now)
client = genai.Client(
    api_key="AIzaSyBJrkXLssU5zULIlDEncDzua1rWw4A1ykU"
)

app = Flask(__name__)

# 🔹 SYSTEM PROMPT → forces Markdown output
SYSTEM_PROMPT = """
You are a helpful AI assistant.

IMPORTANT RULES:
- Always respond ONLY in Markdown
- Use headings, bullet points, and code blocks
- Wrap all code inside triple backticks
- Do NOT explain formatting
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.get_json().get("message", "")

    # ✅ Force Markdown response
    prompt = f"""
{SYSTEM_PROMPT}

User question:
{user_message}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return jsonify({"reply": response.text})

if __name__ == "__main__":
    print("🚀 Flask running on http://127.0.0.1:8000")
    app.run(host="127.0.0.1", port=8000, debug=True)

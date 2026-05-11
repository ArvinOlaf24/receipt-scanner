import base64
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from groq import Groq

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/extract", methods=["POST"])
def extract():
    file = request.files.get("receipt")
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    image_data = base64.standard_b64encode(file.read()).decode("utf-8")
    media_type = file.content_type or "image/jpeg"

    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:{media_type};base64,{image_data}"
                        }
                    },
                    {
                        "type": "text",
                        "text": """You are a precise receipt data extractor. Analyze the receipt image and return ONLY a valid JSON object with no markdown, no explanation, and no extra text. Use exactly these keys:
{
  "merchant_name": "the store or restaurant name, or Unknown",
  "date": "in YYYY-MM-DD format if possible, or the original printed date, or Unknown",
  "total_amount": "the final total as a numeric string e.g. 24.50, or Unknown",
  "currency": "ISO 4217 3-letter code e.g. MYR USD SGD GBP, or Unknown"
}"""
                    }
                ]
            }
        ],
        max_tokens=512
    )

    result = response.choices[0].message.content.strip().replace("```json", "").replace("```", "").strip()
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run()
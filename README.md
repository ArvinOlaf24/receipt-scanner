# ReceiptScan — AI Receipt Extractor

A web app that extracts information from a receipt image using AI and auto-fills a form with the results.

## Live Demo
https://receipt-scanner-taupe-nu.vercel.app

## How to Run Locally

1. Clone the repo
   git clone https://github.com/ArvinOlaf24/receipt-scanner.git
   cd receipt-scanner

2. Install dependencies
   pip install flask groq python-dotenv

3. Create a .env file in the project folder
   GROQ_API_KEY=your-groq-api-key-here

4. Run the app
   python app.py

5. Open your browser and go to
   http://127.0.0.1:5000

## Model Used
- Model: meta-llama/llama-4-scout-17b-16e-instruct
- Provider: Groq API (free tier)

## Prompt Used
You are a precise receipt data extractor. Analyze the receipt image and return ONLY a valid JSON object with no markdown, no explanation, and no extra text. Use exactly these keys:
{
  "merchant_name": "the store or restaurant name, or Unknown",
  "date": "in YYYY-MM-DD format if possible, or the original printed date, or Unknown",
  "total_amount": "the final total as a numeric string e.g. 24.50, or Unknown",
  "currency": "ISO 4217 3-letter code e.g. MYR USD SGD GBP, or Unknown"
}

## Tech Stack
- Backend: Python, Flask
- Frontend: HTML, CSS, JavaScript
- AI API: Groq (Llama 4 Scout Vision)
- Deployment: Vercel
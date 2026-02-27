# Smart Notebook Checker

An AI-powered mobile web application for teachers to scan and check handwritten math notebooks.

## Tech Stack
- **Backend:** FastAPI, Pytesseract (OCR), OpenCV
- **Frontend:** Vanilla HTML/CSS/JS (Mobile-responsive)
- **Math Engine:** Custom logic for Arithmetic, LCM, HCF

## Prerequisites
1. **Tesseract OCR:** 
   - macOS: `brew install tesseract`
   - Linux: `sudo apt install tesseract-ocr`
   - Windows: Download installer from [UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
2. **Python 3.8+**

## Installation

### 1. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

### 2. Run Backend
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Frontend Setup
Simply open `frontend/index.html` in your browser. For mobile testing, serve it using a local server (e.g., `python -m http.server 3000`) and access it via your phone's browser using your computer's IP address.

## Usage
1. Open the app on your phone.
2. Tap "Click to Open Camera".
3. Snap a clear photo of a math notebook page (e.g., `12 + 5 = 17`).
4. Wait for AI analysis.
5. Review results and student performance.

## Features implemented
- ✅ Mobile-responsive Dashboard
- ✅ Hindi & English Support
- ✅ Camera Integration
- ✅ OCR Text Extraction
- ✅ Math Answer Verification (Arithmetics, LCM, HCF)

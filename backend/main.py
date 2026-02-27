from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
from .ocr_engine import OCREngine
from .math_logic import MathSolver

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "Smart Notebook Checker API is running"}

@app.post("/scan")
async def scan_notebook(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Process OCR
    raw_text = OCREngine.extract_text(file_path)
    
    # Parse lines and extract problems
    # Expected format: "12 + 5 = 17" or "12 + 5 [newline] 17"
    lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
    results = []
    
    for line in lines:
        # Regex to find something like "12 + 5 = 17"
        match = re.search(r'([\d\s+\-*/xX]+)\s*=\s*(\d+)', line)
        if match:
            problem_str = match.group(1).strip()
            student_val = float(match.group(2).strip())
            
            is_correct, correct_val = MathSolver.verify_answer(problem_str, student_val)
            
            results.append({
                "problem": problem_str,
                "student_answer": student_val,
                "correct_answer": correct_val,
                "status": "correct" if is_correct else "wrong"
            })
    
    # Fallback if no "=" patterns found
    if not results:
        results.append({
            "problem": "OCR Result",
            "student_answer": "N/A",
            "correct_answer": "N/A",
            "status": "wrong",
            "message": "Could not detect clear math patterns. Raw: " + raw_text[:50]
        })

    return {
        "filename": file.filename,
        "raw_text": raw_text,
        "results": results
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

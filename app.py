from flask import Flask, render_template, request
import pdfplumber
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Upload folder configuration
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Static required skills (can be made dynamic later)
REQUIRED_SKILLS = [
    'python', 'django', 'flask', 'sql', 'git', 'html', 'css'
]

# ---------- PDF TEXT EXTRACTION ----------
def extract_text_from_pdf(path):
    text = ''
    try:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "
    except Exception as e:
        print("PDF read error:", e)

    return text.lower()


# ---------- RESUME ANALYSIS ----------
def analyze_resume(resume_text):
    matched = []
    missing = []

    for skill in REQUIRED_SKILLS:
        if skill in resume_text:
            matched.append(skill)
        else:
            missing.append(skill)

    score = (len(matched) / len(REQUIRED_SKILLS)) * 100

    if score >= 70:
        status = 'Suitable'
    elif score >= 40:
        status = 'Partially Suitable'
    else:
        status = 'Not Suitable'

    return score, status, matched, missing


# ---------- MAIN ROUTE ----------
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':

        # Safety checks
        if 'resume' not in request.files:
            return render_template('index.html', result=None)

        resume = request.files['resume']
        job_desc = request.form.get('job_description', '')

        if resume.filename == '':
            return render_template('index.html', result=None)

        # Secure file saving
        filename = secure_filename(resume.filename)
        resume_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        resume.save(resume_path)

        # Extract and analyze
        resume_text = extract_text_from_pdf(resume_path)

        score, status, matched, missing = analyze_resume(resume_text)

        result = {
            'score': round(score, 2),
            'status': status,
            'matched': matched,
            'missing': missing
        }

    return render_template('index.html', result=result)


# ---------- RUN APP ----------
if __name__ == '__main__':
    app.run(debug=True)

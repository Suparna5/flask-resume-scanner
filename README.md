# Resume Scanner using Flask

## Description
A Flask-based ATS-style resume scanner that extracts text from PDF resumes, matches technical skills, and calculates a job-fit score.

## Features
- Upload PDF resumes
- Extract text using pdfplumber
- Skill matching based on job description
- ATS-style scoring
- Clean and simple UI

## Tech Stack
- Python
- Flask
- HTML, CSS
- pdfplumber

## Installation
1. Clone the repository
2. Create a virtual environment (optional)
3. Install dependencies

## Run in terminal
pip install -r requirements.txt
python app.py

## Open in browser
http://127.0.0.1:5000

## Usage
1. Upload a resume in PDF format
2. Enter the job description
3. Click on "Scan Resume"
4. View ATS score and missing skills


## Project Structure
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── uploads/
└── requirements.txt

## Future Enhancements
1.NLP-based skill extraction
2.Resume ranking for multiple candidates
3.Database integration
4.AI/ML-based job matching

## AUTHOR
Suparna Sabud

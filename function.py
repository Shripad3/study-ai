import PyPDF2
import os
import google.generativeai as genai

#gemini api
genai.configure(api_key="API-KEY")
model = genai.GenerativeModel(model_name='gemini-2.0-flash')

#pdf convertor
def pdf_text_convertor(pdf):
    reader = PyPDF2.PdfReader(pdf)
    total_pages = reader.pages
    print(total_pages)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

#create pdf specific paths
def load_pdfs_from_folder(folder_path):
    pdf_path = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            filepath = os.path.join(folder_path, filename)
            pdf_path.append(filepath)
    return pdf_path

def ask_gemini(prompt_text):
    response = model.generate_content(prompt_text)
    return response.text
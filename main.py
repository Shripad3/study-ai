import function
import os
import time

time_start = time.time()

folder_path = r"C:\Users\shrip\source\repos\study ai\pdfs"

text = ""
pdf_paths = function.load_pdfs_from_folder(folder_path)
for pdf_path in pdf_paths:
    text = function.pdf_text_convertor(pdf_path)

flag = 1
while flag != 0:
    prompt_text = input("Enter your question: ")
    if prompt_text.lower() == 'exit':
        flag = 0
    else:
        prompt_text += f",from the text [{text}]"
        response = function.ask_gemini(prompt_text)
        print(response)
time_end = time.time()
print(time_end - time_start)
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import function  # your function.py file

def select_pdf():
    file_path = filedialog.askopenfilename(
        title="Select a PDF",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if file_path:
        pdf_text = function.pdf_text_convertor(file_path)
        if not pdf_text:
            messagebox.showerror("Error", "No text found in PDF!")
            return
        pdf_text_area.delete('1.0', tk.END)
        pdf_text_area.insert(tk.END, "📄 PDF Content:\n\n")
        pdf_text_area.insert(tk.END, pdf_text[:3000])  # Show first 3000 characters
        ask_button.config(state=tk.NORMAL)
        app.selected_text = pdf_text

def ask_gemini():
    user_prompt = prompt_text_area.get('1.0', tk.END).strip()
    if not user_prompt:
        messagebox.showerror("Error", "Please write a prompt!")
        return
    
    final_prompt = f"{user_prompt}\n\nContext from PDF:\n{app.selected_text[:5000]}"
    try:
        answer = function.ask_gemini(final_prompt)
        pdf_text_area.insert(tk.END, "\n\n🤖 Gemini's Response:\n\n")
        pdf_text_area.insert(tk.END, answer)
        
    except Exception as e:
        messagebox.showerror("Error", f"Failed to connect to Gemini:\n{e}")

# GUI Setup
app = tk.Tk()
app.title("📚 PDF Reader + Gemini AI (Custom Prompt)")
app.geometry("800x700")

select_button = tk.Button(app, text="📄 Select PDF", command=select_pdf, font=("Arial", 14))
select_button.pack(pady=10)

pdf_text_area = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=90, height=20)
pdf_text_area.pack(padx=10, pady=10)

prompt_label = tk.Label(app, text="✍️ Write your prompt:", font=("Arial", 12))
prompt_label.pack(pady=(20, 5))

prompt_text_area = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=90, height=5)
prompt_text_area.pack(padx=10, pady=5)

ask_button = tk.Button(app, text="💬 Ask Gemini", command=ask_gemini, font=("Arial", 14), state=tk.DISABLED)
ask_button.pack(pady=20)

app.selected_text = ""

app.mainloop()

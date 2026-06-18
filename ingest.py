import os
from pypdf import PdfReader

PDF_FOLDER = "schemes"

all_text = ""

for file in os.listdir(PDF_FOLDER):
    if file.endswith(".pdf"):
        path = os.path.join(PDF_FOLDER, file)

        reader = PdfReader(path)

        for page in reader.pages:
            text = page.extract_text()

            if text:
                all_text += text + "\n"

with open("scheme_data.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

print("PDF Processed Successfully")

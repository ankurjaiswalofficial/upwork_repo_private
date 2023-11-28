from PyPDF2 import PdfReader 


reader = PdfReader('./auto_pdf_reader/Story.pdf')

print("No of Pages: ", len(reader.pages))

for i in range(0, len(reader.pages)):
    page = reader.pages[i]
    text = page.extract_text()
    with open(f"./auto_pdf_reader/data_files/data_file_{i}.txt", "w") as f:
        f.write(text)
        f.close()

print("Task Complete") 

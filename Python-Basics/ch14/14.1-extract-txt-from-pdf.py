import json
from pathlib import Path
from PyPDF2 import PdfFileReader

pdf_path = Path.joinpath(Path.cwd(), "Pride_and_Prejudice.pdf")
pdf = PdfFileReader(str(pdf_path))
first_page = pdf.getPage(0)

pp_text_path = Path.joinpath(Path.cwd(), "Pride_and_Prejudice.txt")

with pp_text_path.open(mode="a", encoding="utf-8") as file:
  for page in pdf.pages:
    file.write(page.extractText()) 
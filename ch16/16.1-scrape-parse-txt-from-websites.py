from operator import mod
from urllib.request import urlopen
from pathlib import Path




url = "https://github.com/darioarias"
html_page = urlopen(url)

html_as_text = html_page.read().decode("utf-8")


html_path = Path.joinpath(Path.cwd(), "scraped_html.html")
html_path.touch()

with html_path.open(mode="a", encoding="utf-8") as file:
  file.write(html_as_text)
import time
import mechanicalsoup

browser = mechanicalsoup.Browser()



for i in range(2):
  page = browser.get("http://olympus.realpython.org/dice") 
  tag = page.soup.select("#result")[0]
  result = tag.text
  print(f'dice val: {result}')
  time.sleep(1)


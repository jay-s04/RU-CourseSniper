import requests
import pandas as pd
from bs4 import BeautifulSoup
import asyncio
from email.message import EmailMessage
import time

# This is where you put the sections
# These are temporary already open sections
numsOfSections = ["05575", "05576"]

# The infinite loop that checks the website over and over
while (True):
  page = requests.get("https://sis.rutgers.edu/soc/api/openSections.json?year=2024&term=1&campus=NB")
  bspage = BeautifulSoup(page.text)
  #print(bspage.prettify())
  open_sections = repr(bspage.select("body p")[0])
  chars_to_remove = ['<', 'p', '>', '"', '[', ']', '/']
  for char in chars_to_remove:
    open_sections = open_sections.replace(char, '')
  open_sections = open_sections.split(',')
  print(len(open_sections))
  for section in numsOfSections:
    if section in open_sections:
      print("THERE IS A SECTION OPEN WITH THE CODE " + section)
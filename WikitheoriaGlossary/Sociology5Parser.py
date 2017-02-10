# Sociology5 Parser

from bs4 import BeautifulSoup
soup = BeautifulSoup(open("Sociology5.html"), 'html.parser')

print soup.prettify()
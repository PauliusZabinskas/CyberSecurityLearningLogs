from bs4 import BeautifulSoup

with open("index.html","r") as f:
  doc = BeautifulSoup(f, "html.parser")

print(doc.prettify())

# v-1.1
from bs4 import BeautifulSoup

with open("index.html","r") as f:
  doc = BeautifulSoup(f, "html.parser")

tag = doc.find_all("p")[0]
# doc.find_all("a") = find something

#doc.find("p").text = scrape text only

# tag = doc.find_all("p")[0] && print(tag.find_all("b"))= indexing what i am looking for precisely. 
# 
# 
#  
print(tag.find_all("b"))

# v-1.2
import string
from urllib import request
from bs4 import BeautifulSoup

url = "https://www.amazon.com/ASUS-Graphics-DisplayPort-Axial-tech-2-7-Slot/dp/B0985Z47C8/ref=sr_1_3?crid=15VEGAJCJOS6D&keywords=gpu&qid=1656666149&sprefix=gpu%2Caps%2C315&sr=8-3"


with open("index.html", 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify())
    
    #v-1.3. iteration is beeeing used to scrape html's 'p' tags
import string
from urllib import request
from bs4 import BeautifulSoup

url = "https://www.amazon.com/ASUS-Graphics-DisplayPort-Axial-tech-2-7-Slot/dp/B0985Z47C8/ref=sr_1_3?crid=15VEGAJCJOS6D&keywords=gpu&qid=1656666149&sprefix=gpu%2Caps%2C315&sr=8-3"


with open("index.html", 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('p')
    for course in tags:
        print(course.text)
    




    
    
    

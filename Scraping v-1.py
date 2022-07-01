from bs4 import BeautifulSoup

with open("index.html","r") as f:
  doc = BeautifulSoup(f, "html.parser")

print(doc.prettify())

# more
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



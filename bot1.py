import requests
from bs4 import BeautifulSoup

GET_URL = 'https://www.uludagsozluk.com/'



get1=requests.get(GET_URL)
#print(get1.text)
soup = BeautifulSoup(get1.content, 'html.parser')
#print(soup.prettify())
tbl=soup.find_all("div",class_="li_capsul_entry")
#print(tbl)
entry_tag = soup.find_all("h4")
#print(entry_tag)
with open("test.txt",'r+') as f:
    for option in entry_tag:
        f.write(option.text)
        f.write("\n")
        print(option.text)
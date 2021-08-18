import requests
from bs4 import BeautifulSoup 

URL="https://en.wikipedia.org/wiki/History_of_Mexico"
page=requests.get(URL)

soup=BeautifulSoup(page.content,'html.parser')

def get_citations_needed_number(url):
    count=[]
    for wrapper in soup.find("div",class_="mw-parser-output").find_all("p"):
        for wrapperr in wrapper.find_all('a', title="Wikipedia:Citation needed"):
            a=wrapperr
            count.append(a)

    print("How many citations? the Citations =",len(count))
    return len(count)    

def  get_citations_needed_report(url):
    for wrapper in soup.find("div",class_="mw-parser-output").find_all("p"):
        for wrapperr in wrapper.find_all('a', title="Wikipedia:Citation needed"):
            a=wrapperr.parent.parent.parent.text.strip()
            print("\n",a,"\n")
    return a

if __name__ == "__main__":
    get_citations_needed_number(URL)
    get_citations_needed_report(URL)
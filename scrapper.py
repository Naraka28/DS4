"""
Web scrapper
"""
import requests
from bs4 import BeautifulSoup

def scrap(URL:str):
    page=requests.get(URL)
    return page
def main():
    url="https://bit.ly/dolarInfo"
    pagina=scrap(url)
    soup=BeautifulSoup(pagina.content,"html.parser")
    result=soup.find(class_="exchangeRate")
    ex=get_exchange_rate(result)
    print(ex)
def get_exchange_rate(dom):
    exchange_rate={}
    for row in dom.find_all("p"):
        print(f"{row}")
        title=row.text.strip()
        if title[0]=="C":
            title="Compra"
        else:
            title="Venta"
        value=row.find("span")
        value=value.text.strip()
        exchange_rate[title]=value
    return exchange_rate

if __name__=="__main__":
    main()

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
    # result=soup.find(class_="exchangeRate")
    # ex=get_exchange_rate(result)
    result=soup.find(id="dllsTable")
    dic=get_exchange_rate_dict(result)
    print(dic)

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
def get_institutions():
    url="https://bit.ly/dolarInfo"
    pagina=scrap(url)
    soup=BeautifulSoup(pagina.content,"html.parser")
    result=soup.find(id="dllsTable")
    dic=get_exchange_rate_dict(result)
    print(dic)


def get_exchange_rate_dict(dom):
    inst={}
    body=dom.find("tbody")
    for row in body.find_all("tr"):
        i=0
        long=len(row.find_all("td"))
        for col in row.find_all("td"):
            if long<4:
                if i==0:
                    institucion=col.find(class_="small-hide")
                    institucion=institucion.text.strip()
                if i==2:
                    compra=float(compra.text.strip())
                    print(compra)
            else:
                if i==0:
                    institucion=col.find(class_="small-hide")
                    institucion=institucion.text.strip()
                    print(institucion)
                if i==2:
                    compra=float(compra.text.strip())
                    print(compra)
                if i==3:
                    venta=float(venta.text.strip())
                    print(venta)
        i+=1
    inst[institucion]={"Compra":compra,"Venta":venta}



if __name__=="__main__":
    main()

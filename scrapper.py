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
    dic_list=get_exchange_rate_dict(result)
    fix_dic=dic_list.pop()
    bank_dic=dic_list.pop()
    print(bank_dic)
    print(fix_dic)
    maximo_dolar(bank_dic,"Compra")
    min_dolar(bank_dic,"Compra")
    maximo_dolar(bank_dic,"Venta")
    min_dolar(fix_dic,"FIX")
    maximo_dolar(fix_dic,"FIX")

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
def get_exchange_rate_dict(dom):
    body=dom.find("tbody")
    inst={}
    fix_dic={}
    for row in body.find_all("tr"):
        i=0
        long=len(row.find_all("td"))
        for col in row.find_all("td"):
            if long<5:
                if i==0:
                    institucion=col.find(class_="small-hide")
                    institucion=institucion.text.strip()
                if i==3:
                    compra=float(col.text.strip())
                    fix_dic[institucion]={"FIX":compra}
            else:
                if i==0:
                    institucion=col.find(class_="small-hide")
                    institucion=institucion.text.strip()
                if i==3:
                    compra=float(col.text.strip())
                if i==4:
                    venta=float(col.text.strip())
                    inst[institucion]={"Compra":compra, "Venta": venta}
            i+=1
    list_dic=[inst,fix_dic]
    return list_dic
def maximo_dolar(dic:dict,eleccion:str):
    compra_max=0
    for k in dic:
       compra=dic[k][eleccion]
       if compra_max<compra:
           banco=k
           compra_max=compra
    print(f"Banco: {banco} {eleccion}_max: {compra_max}")
def min_dolar(dic:dict,eleccion:str):
    compra_min=1000
    for k in dic:
       compra=dic[k][eleccion]
       if compra<compra_min:
           banco=k
           compra_min=compra
    print(f"Banco: {banco} {eleccion}_min: {compra_min}")





if __name__=="__main__":
    main()

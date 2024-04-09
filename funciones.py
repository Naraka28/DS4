import csv
import  datetime

def carga_csv(archivo:str) ->list :
    """
    Cargar el csv y regresar una lista
    """
    lista = []
    with open(archivo,'r',encoding='utf-8') as csv_file:
        lista = list(csv.DictReader(csv_file))
        return lista

def peliculas_mas_recientes(dic:list) -> list:
    """
    Regresa una lista con las peliculas más recientes
    """
    lista = []
    

if __name__=="__main__":
    lista = carga_csv('cartelera_2024.csv')
    print(lista)


from collections import namedtuple
import csv
from datetime import datetime
Entreno = namedtuple('Entreno','tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

def lee_entrenos(ruta_csv):
   with open(ruta_csv, encoding='utf-8') as f:
       lector = csv.reader(f)
       next(lector)
       entrenos = []
       for tipo, fechahora, ubicacion, duracion, calorias, \
            distancia, frecuencia, compartido in lector:
            fechahora = datetime.strptime(fechahora,"%d/%m/%Y %H:%M")
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            compartido = compartido == 'S'
            tupla = Entreno(tipo, fechahora, ubicacion, duracion, calorias, \
            distancia, frecuencia, compartido)
            entrenos.append(tupla)
       return entrenos 
        
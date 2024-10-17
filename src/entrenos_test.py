from entrenos import *

def test_lee_entrenos():
    print("Prueba de lee_entrenos:")
    entrenos = lee_entrenos("data/entrenos.csv")
    print(entrenos[:3])
    print(entrenos[-3:])
    
def test_tipos_entrenos(entrenos):
    print("Prueba de tipos de entreno")
    print(tipos_entrenos)
    
def test_entrenos_duracion_superior(entrenos):
    print("Prueba de 'entrenos_duracion_superior'")
    print(entrenos_duracion_superior(entrenos, 75))
    
if __name__ == "__main__":
    entrenos = lee_entrenos("data/entrenos.csv")
    # test_lee_entrenos()
    test_entrenos_duracion_superior(entrenos)
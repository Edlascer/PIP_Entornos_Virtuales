import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text)) # ==> Imprime la clase string
    categories = r.json() # ==> Método json para transformar el string a lista sobre la cual podemos iterar
    for category in categories:
        print(category['name']) #Imprimimos únicamente los nombres de las categorías
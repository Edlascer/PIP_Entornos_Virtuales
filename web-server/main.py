import store
from fastapi import FastAPI

app = FastAPI() #Instancia de la aplicación

@app.get('/') #Slash o ruta donde podrán acceder desde la web
def get_list():
    return[1, 2, 3]

@app.get('/contact') #Slash o ruta donde podrán acceder desde la web
def get_list():
    return{'name' : 'Platzi'}

def run():
    store.get_categories()

if __name__ == '__main__':
    run()
import requests

def get_cateories():
    """Funcion para obtener información a traves de la api
    Se debe ingresar una api
    """
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json()
    for category in categories:
        print(category['name'])
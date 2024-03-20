import requests
from bs4 import BeautifulSoup


proxies = {"http": "http://142.202.220.242:18510",  # Ajusta el esquema del proxy aquí
        "https": "http://142.202.220.242:18510"} 





def verificar_sql_enlace(url):
    try:
        # Realizar la solicitud GET a la URL
        response = requests.get(url)
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Analizar el contenido HTML de la respuesta
            soup = BeautifulSoup(response.content, 'html.parser')
            # Buscar todos los enlaces ('a') en el contenido
            enlaces = soup.find_all('a')
            # Verificar si alguno de los enlaces contiene ".sql" en su atributo href
            for enlace in enlaces:
                if enlace.get('href') and '.sql' in enlace.get('href'):
                    print("Valido")
                    print(url)
                    return
            # Si no se encontró ningún enlace con ".sql", imprimir "invalido"
            print("Invalido")
        else:
            # Si la solicitud no fue exitosa, imprimir un mensaje de error
            print("Error al realizar la solicitud:", response.status_code)
    except Exception as e:
        # Manejar cualquier error que ocurra durante el proceso
        print("Error:", e)




def search_google(query, api_key, cx,proxies):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}"
    response = requests.get(url,proxies=proxies)
    if response.status_code == 200:
        data = response.json()
        if 'items' in data:
            for item in data['items']:
                #print(item['title'], item['link'])
                print("Procesando:", item['link'])
                verificar_sql_enlace(item['link'])
                with open("results.txt","a+") as r:
                    r.write(item['link']+"\n")
        else:
            print("No se encontraron resultados.")
    else:
        print("Error al realizar la búsqueda:", response.status_code)

if __name__ == "__main__":
    print("""
----|\----------------- **--------------------
----|/-----------------**---****---*****------
---/|-----------------**---**--**----**-------
--/-|_-------------****---******---**---------
-|--|-\------------****---**--**--*****-------
_|__|_|
  \_|_/
""")
    # Término de búsqueda
    search_query = input('Paste your Query:')

    # Clave de API de Google
    google_api_key = "tu api key de google"

    # ID de búsqueda de Google (cx)
    google_cx = "tu id de busqueda de google"

    # Realizar búsqueda en Google
    search_google(search_query, google_api_key, google_cx,proxies)

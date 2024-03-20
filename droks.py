import requests
from bs4 import BeautifulSoup

proxies = {"http": "http://142.202.220.242:18510",
           "https": "http://142.202.220.242:18510"}


def verificar_sql_enlace(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            enlaces = soup.find_all('a')
            for enlace in enlaces:
                if enlace.get('href') and '.sql' in enlace.get('href'):
                    print("Valido")
                    print(url)
                    return
            print("Invalido")
        else:
            print("Error al realizar la solicitud:", response.status_code)
    except Exception as e:
        print("Error:", e)


def search_google(query, api_key, cx, proxies, num_pages):
    try:
        for page in range(1, num_pages + 1):
            start = (page - 1) * 10 + 1  # Calcula el índice de inicio de la página
            url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}&start={start}"
            response = requests.get(url, proxies=proxies)
            if response.status_code == 200:
                data = response.json()
                if 'items' in data:
                    for item in data['items']:
                        print("Procesando:", item['link'])
                        verificar_sql_enlace(item['link'])
                        with open("results.txt", "a+") as r:
                            r.write(item['link'] + "\n")
                else:
                    print("No se encontraron resultados en la página", page)
            else:
                print("Error al realizar la búsqueda en la página", page, ":", response.status_code)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    print("""
----|\----------------- **--------------------
----|/-----------------**---****---*****------
---/|-----------------**---**--**----**-------
--/-|_-------------****---******---**---------
-|--|-\------------****---**--**--*****-------
_|__|_|Drophack666
  \_|_/
""")
    search_query = input('Paste your Query:')
    num_pages = int(input('Enter the number of pages to extract:'))  # Número de páginas a extraer

    google_api_key = "Your Google API Key"
    google_cx = "Your Google CX"

    search_google(search_query, google_api_key, google_cx, proxies, num_pages)

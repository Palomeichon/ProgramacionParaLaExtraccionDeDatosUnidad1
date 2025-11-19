# Palafox Remirez Elvia Paloma 2209849 elvia.palafox@uabc.edu.mx
# grupo 951 Materia Programacion Para la extraccion de datos
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# --- FUNCIÓN PARA EXTRAER DATOS DEL HTML ---
def extraer(html):
    d = {
        "numero": [],
        "nombre": [],
        "precio": [],
        "opiniones": []
    }

    soup = BeautifulSoup(html, "html.parser")

    numeros = soup.find_all("span", class_="zg-bdg-text")
    nombres = soup.find_all("div", class_="_cDEzb_p13n-sc-css-line-clamp-3_g3dy1")
    precios = soup.find_all("span", class_="_cDEzb_p13n-sc-price_3mJ9Z")
    opiniones = soup.find_all("span", class_="a-size-small", attrs={"aria-hidden": "true"})


    max_len = max(len(numeros), len(nombres), len(precios))

    for i in range(max_len):
        num = numeros[i].text.strip().replace("#", "") if i < len(numeros) else None
        nom = nombres[i].text.strip() if i < len(nombres) else None
        pre = precios[i].text.strip() if i < len(precios) else None
        op = opiniones[i].text.strip().replace(",", "") if i < len(opiniones) else None



        d["numero"].append(num)
        d["nombre"].append(nom)
        d["precio"].append(pre)
        d["opiniones"].append(op)


    return pd.DataFrame(d)


# --- NAVEGACIÓN AUTOMÁTICA CON SELENIUM ---
def navegacion(paginas):
    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument("--window-size=1020,1200")
    #opc.add_argument("--headless=new")

    navegador = webdriver.Chrome(service=s, options=opc)
    url_base = "https://www.amazon.com.mx/gp/bestsellers/beauty/10178384011/ref=zg_bs_pg_{pag}_beauty?ie=UTF8&pg={pag}"

    todos_datos = pd.DataFrame()

    for pag in range(1, paginas + 1):
        url = url_base.format(pag=pag)
        navegador.get(url)
        time.sleep(4)

        # Desplazamiento para cargar completamente la página
        last_height = navegador.execute_script("return document.body.scrollHeight")
        while True:
            navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = navegador.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        df = extraer(navegador.page_source)
        todos_datos = pd.concat([todos_datos, df], ignore_index=True)
        print(f"Página {pag}: {len(df)} productos extraídos.")

    navegador.quit()

    # Guarda todo en un csv
    todos_datos.to_csv("amazon_belleza.csv", index=False, encoding="utf-8-sig")
    print(f"\n Archivo final guardado: amazon_belleza.csv con {len(todos_datos)} productos.")


# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    paginas = 2  # numero de paginas existentes
    navegacion(paginas)

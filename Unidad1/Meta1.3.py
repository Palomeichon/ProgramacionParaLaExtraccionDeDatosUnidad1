# Autor: Palafox Ramirez Elvia Paloma
# Grupo: 951
# Meta 1.3: Implementar proceso de Scraping usando Selenium
# Página elegida: Amazon México, buscando la palabra shampoo


import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# --- FUNCIÓN PRINCIPAL ---
def buscar_producto(producto, paginas):
    # Configurar navegador
    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument("--window-size=1020,1200")
    # opc.add_argument("--headless=new")

    navegador = webdriver.Chrome(service=s, options=opc)

    # Crear carpeta de capturas si no existe
    if not os.path.exists("capturas"):
        os.makedirs("capturas")

    # URL base de Amazon para búsqueda
    url_base = f"https://www.amazon.com.mx/s?k={producto}"

    for pag in range(1, paginas + 1):
        url = f"{url_base}&page={pag}"
        navegador.get(url)
        time.sleep(4)

        # Hacer scroll para cargar todo el contenido
        last_height = navegador.execute_script("return document.body.scrollHeight")
        while True:
            navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = navegador.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # Guardar captura de pantalla
        nombre_archivo = f"capturas/{producto}_pagina_{pag}.png"
        navegador.save_screenshot(nombre_archivo)
        print(f"Captura guardada: {nombre_archivo}")

    navegador.quit()
    print(f"\nProceso completado. Se tomaron {paginas} capturas del producto '{producto}'.")



if __name__ == "__main__":
    buscar_producto("shampoo", 2)

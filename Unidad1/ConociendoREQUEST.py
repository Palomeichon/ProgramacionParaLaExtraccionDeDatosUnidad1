import requests
url="https://www.amazon.es/Genesis-Mochila-Port%C3%A1til-Pallad-Negro/dp/B0C25W1846/ref=sr_1_1?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1JJ13KP9I453O&dib=eyJ2IjoiMSJ9.SqDVCXHx7zZRX1VXOX2etbpP3D6R75jN3M4Jr4mop0I.Sp7BvGCfQh-iIFPTE9U-J1XZSzeT1jGiA6jy8OVL8PI&dib_tag=se&keywords=GENESIS+PALLAD+500+15.6&qid=1759141556&sprefix=genesis+pallad+500+15.6%2Caps%2C389&sr=8-1"


#recibimos una respuesta de estatus de 500 lo que significa que es error del servidor, eso paso
# porque el sistema detecto que no lo hicimos desde el navegador, para poder entrara utilizamos un diccionario
# nosotros utilizares el user agent tenemos que hacerle creer al servidor que le mandamos peticiones desde un navegador
h= {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                 "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"}
res= requests.get(url, headers=h)
print(res.status_code)
print(res.reason)
print(res.ok)
# Guardar el HTML en un archivo
with open("codigo_200.html", "w", encoding="utf-8") as f:
    f.write(res.text)
print(res.headers)
# formas de acceder al cuerpo de la respuesta
#print(res.content)#bytes
#print(res.text)#string
#print(res.json)#estructura json

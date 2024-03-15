# %%

from selenium import webdriver
from bs4 import BeautifulSoup 
from bs4 import BeautifulSoup
import pandas as pd
import re

# %%
# Configurar el controlador de Selenium (asegúrate de tener instalado el controlador correspondiente, como Chromedriver)
driver = webdriver.Chrome()

# URL de la página
url = "https://buenosaires.gob.ar/areas/registrocivil/nombres/busqueda/imprimir.php"

# Cargar la página
driver.get(url) 

# Esperar a que la tabla esté presente (puedes ajustar el tiempo de espera según sea necesario)
driver.implicitly_wait(3)

# Obtener el HTML de la página
html = driver.page_source  

# Cerrar el navegador
driver.quit()

# %% [markdown]
# FUNCIONA CREAR DATAFRAME

# %%
# Pasar el HTML a BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Encontrar la tabla
#table = soup.find('table')
table = soup.find('table')

# Encontrar todas las filas de la tabla
rows = table.find_all('tr')

# Inicializar listas para almacenar nombres y géneros
nombres = []
generos = []
pattern = r'>(.*?)</td>'

# Iterar sobre las filas e imprimir el contenido de las celdas
for row in rows:
    cells = row.find_all('td')
    if len(cells) > 0 :  
        nombre = re.findall(pattern, str(cells[0]))[0].strip()  # Extraer el nombre
        genero = re.findall(pattern, str(cells[1]))[0].strip()  # Extraer el género
        nombres.append(nombre)
        generos.append(genero) 

# Crear DataFrame
df = pd.DataFrame({'Nombre': nombres, 'Género': generos}) 

# %%
df.to_excel('name_gender.xlsx',index=False)

# %%




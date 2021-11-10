# Importo Selenium que manejará el navegadro y el componente webdriver
from selenium import webdriver

# Asigno a browser el objeto webdriver Firefox y pido que abra esa dirección
browser = webdriver.Firefox()
browser.get("http://localhost:8000")

# chequeo que Django sea el título del browser que abrí
assert "Congratulations!" in browser.title

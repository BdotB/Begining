"""
Tema 8 - SELECTORS
"""

"""
Exerciții Recomandate - grad de dificultate: Ușor
1. Revizualizează întâlnirea 7 și ia notițe în caz că ți-a scăpat ceva.
Te rog să scrii pe canalul de comunicare scrisă unde întâmpini dificultăți și te
ajut.
Dacă stai blocat > 30 min, cere indiciu.
"""

"""
Exerciții obligatorii - grad de dificultate: Usor spre Mediu
Alege-ți unul sau mai multe din sugestiile de site-uri de mai jos
- https://www.phptravels.net/
- http://automationpractice.com/index.php
- https://formy-project.herokuapp.com/
- https://the-internet.herokuapp.com/
- https://www.techlistic.com/p/selenium-practice-form.html
- jules.app
Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id
● Link text
● Parțial link text
● Name
● Tag*
● Class name*
● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
observație:
- Probabil nu vei găsi un singur website care să cuprindă toate variantele
de mai sus, astfel că îți recomandăm să folosești mai multe site-uri
"""

from selenium import webdriver

# Deschide browser-ul
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.phptravels.net/")

# Id
search_form = driver.find_element_by_id("searchform")
modal = driver.find_element_by_id("modal")
header = driver.find_element_by_id("header")

# Link text
home = driver.find_element_by_link_text("Home")
blog = driver.find_element_by_link_text("Blog")
contact = driver.find_element_by_link_text("Contact")

# Partial link text
my_account = driver.find_element_by_partial_link_text("My Account")
sign_up = driver.find_element_by_partial_link_text("Sign Up")
book_now = driver.find_element_by_partial_link_text("Book Now")

# Name
email = driver.find_element_by_name("email")
password = driver.find_element_by_name("password")
country = driver.find_element_by_name("country")

# Tag
div = driver.find_element_by_tag_name("div")
input = driver.find_element_by_tag_name("input")
span = driver.find_element_by_tag_name("span")

# Class name
btn_primary = driver.find_element_by_class_name("btn btn-block btn-primary")
btn_lg = driver.find_element_by_class_name("btn-lg")
p1 = driver.find_element_by_class_name("p1")

# CSS (1 dupa id, 1 dupa clasa, 1 dupa atribut=valoare_partiala)
select2_drop = driver.find_element_by_css_selector("#select2-drop")
navbar = driver.find_element_by_css_selector(".navbar")
departure = driver.find_element_by_css_selector("[name^='departure']")

# Inchide browser-ul
driver.quit()
'''
"""
- Opțional: La tag și class name vei folosi find elementS! - salvează în listă.
Interactionează cu un element la alegere din listă.
Pentru xpath identifică elemente după criteriile de mai jos:
● 3 după atribut valoare
● 3 după textul de pe element
● 1 după parțial text
● 1 cu SAU, folosind pipe |
● 1 cu *
● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci
cu (xpath)[1]
● 1 în care să folosești parent::
● 1 în care să folosești fratele anterior sau de după (la alegere)
● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu
ce element vreau să interacționez.
"""
'''
from selenium import webdriver

# Deschide browser-ul
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.phptravels.net/")

# 3 dupa atribut valoare
elements_by_value = driver.find_elements_by_xpath("//input[@type='text' or @type='password' or @type='email']")

# 3 dupa textul de pe element
elements_by_text = driver.find_elements_by_xpath("//*[text()='Home' or text()='Blog' or text()='Contact']")

# 1 dupa parțial text
element_by_partial_text = driver.find_element_by_xpath("//*[contains(text(), 'Account')]")

# 1 cu SAU, folosind pipe |
element_by_pipe = driver.find_element_by_xpath("//input[@type='text' or @type='email']")

# 1 cu *
element_by_star = driver.find_element_by_xpath("//div/*")

# 1 în care le iei ca pe o lista de xpath si în python ajunge 1 element, deci cu (xpath)[1]
element_by_list = driver.find_element_by_xpath("(//input[@type='text' or @type='password' or @type='email'])[1]")

# 1 în care sa folosesti parent::
element_by_parent = driver.find_element_by_xpath("//input[@name='password']/parent::div")

# 1 în care sa folosesti fratele anterior sau de dupa (la alegere)
element_by_sibling = driver.find_element_by_xpath("//input[@name='email']/following-sibling::button")

# 1 functie ca si cea de la clasa prin care sa pot alege eu prin parametru cu ce element vreau sa interactionez
def interact_with_element(element_index):
    elements = driver.find_elements_by_xpath("//a")
    elements[element_index].click()


# Interactioneaza cu al 2-lea element din lista de elemente "elements_by_text"
elements_by_text[1].click()

# Interactioneaza cu primul element din lista de elemente "elements_by_value"
elements_by_value[0].send_keys("test@example.com")

# Inchide browser-ul
driver.quit()
'''
"""
Exerciții extra - Opțional
https://www.automatetheplanet.com/most-exhaustive-xpath-locators-cheat-sh
eet/
"""
# Curs 8: Exceptii + Selectors

## 📝 OBIECTIVE
1. Sa verificam daca toata lumea are proiectul pe github
2. Sa invatam sa folosim github direct din interfata de pycharm
3. Recapitulare CURS 7
4. Q&A Tema 7
5. Sa stim ce e o exceptie si cum o 'tratam'
6. Sa aprofundam si sa sedimentam diferitele tipuri de selectori
- Id
- Link Text
- Partial Link Text
- Name
- Tag
- Class name
- CSS
- Xpath

## 📌 Exceptii in Python

- Exista situatii in care codul nu poate fi executat/apar erori.
- In aceste cazuri, codul 'arunca' o exceptie.

```python
# Exemplul 1:
x = 5 / 0  # ZeroDivisionError

# Exemplul 2:
my_dict = {'pret': 25.00, 'nume': 'perna'}
print(my_dict['culoare']) # KeyError
```

- Programatorii se pot astepta la ea, pot sa o 'prinda' si sa o 'trateze'
- In acest sens, putem anticipa erori si evitam sa 'crape' aplicatia
- Se foloseste sintaxa try/except

```python
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Can not divide by zero!")
```

- Uneori, dorim sa 'ridicam' noi o exceptie intentionat.

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Al doilea parametru trebuie "
                                "sa fie diferit de 0.")
    return a / b

print(divide(1, 0))
```

## 📌 Selenium - selectori - testare automata site-uri web

- Pentru a putea testa automat o aplicatie web/ un site,
folosim in Python, tool-ul Selenium. 
- Instalare: pip install selenium
- Inainte de a testa comportamentul unui site, trebuie sa invatam
cum sa identificam elementele de pe acel site.
- Exemplu de site pentru testare: https://the-internet.herokuapp.com/

### Elementele de pe un site
- Orice site, are la baza un template, care descrie
elementele dintr-un site.
- Acest template este definit folosind HTML (limbaj de markup)

### Cum accesam elementele / partea de HTML a unui site?

- Navigam catre URL-ul dorit
- Click dreapta pe elementul ce dorim sa il inspectam
- Selectam optiunea 'Inspect'
- Veti gasi partea de html a unui website
- Structura e urmatoarea:
  - tag sau webelement (ex: \<input>)
  - atribut="valoare" (ex: type="text" id="first-name")

### Selectori
- Ne folosim de libraria webdriver din selenium

#### Id
- Accesarea unui element de pe un site dupa atributul id

```python
# selector by ID
first_name = chrome.find_element(By.ID, 'first-name')
first_name.send_keys('Andy')
```

#### Link Text / Partial Link text
- link text = textul care este pus pentru un link
- Un site este format din mai multe pagini.
pentru a naviga pe diferite pagini dintr-un site,
definim aceste pagini prin intermediul unor ancore,
adica tag-ul a din html.
- Elementul de tip ancora are urmatoarele elemente:
1. tag-ul de inceput (a)
2. link-ul catre care se face navigarea ( atributul href, la care ii dam valoarea/link-ul)
3. textul care este afisat peste link (linktext)
4. tag-ul de sfarsit </a>

```python
# selector by link text
chrome.find_element(By.LINK_TEXT, 'Checkboxes').click()
```

```python
# selector by Partial Link Text
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Enabled').click()
```

#### Name/Tag

```python
chrome.get('http://www.seleniumframework.com/PracticeForm')

# selector by Name
chrome.find_element(By.NAME, 'country').send_keys('Romania')
```

```python
chrome.get('http://formy-project.herokuapp.com/form')

# selector by Tag - ia primul tot timpul. - e ok doar daca avem
# un tag unic
chrome.find_element(By.TAG_NAME, 'input').send_keys('Andy')

# gasim mai multe si le punem in lista
input_list = chrome.find_elements(By.TAG_NAME, 'input')
input_list[1].send_keys('Pop')
```

#### Class name
```python
chrome.get('https://formy-project.herokuapp.com/form')

# selector by Class - ia primul tot timpul. - e ok
# daca avem o clasa unica
chrome.find_element(By.CLASS_NAME, 'form-control').send_keys('Andy')

# gasim mai multe si le punem intr-o lista
input_list = chrome.find_elements(By.CLASS_NAME, 'form-control')
input_list[1].send_keys('Pop')
```

#### CSS
```python
chrome.get('https://formy-project.herokuapp.com/form')

# selector by CSS - ID
element = chrome.find_element(By.CSS_SELECTOR, 'input#first-name')
element.send_keys('An')

# selector by CSS - Class - only first one if multiple choices
element = chrome.find_element(By.CSS_SELECTOR, 'input.form-control')
element.send_keys('dy')

# selector by CSS - atribut=valoare
element = chrome.find_element(
  By.CSS_SELECTOR,
  'input[placeholder="Enter last name"]'
)
element.send_keys('S')

# selector by CSS - atribut=valoare partiala + parinte -> copil
element = chrome.find_element(
  By.CSS_SELECTOR,
  'div input[placeholder*="last name"]'
)
element.send_keys('pop')
```

#### XPATH
```python
chrome.get('https://formy-project.herokuapp.com/form')

# selector by Xpath - atribut=valoare
el1 = chrome.find_element(By.XPATH, '//input[@id="first-name"]')
el1.send_keys('A')

# selector by Xpath - * toate elementele care respecta regula
el2 = chrome.find_element(By.XPATH, '//*[@id="first-name"]')
el2.send_keys('n')

# selector by Xpath - navigare in jos - trecem prin fiecare element
el3 = chrome.find_element(
  By.XPATH,
  '//div/div/input[@id="first-name"]'
)
el3.send_keys('d')

# selector by Xpath - navigare in jos - skip tags -
# cautam oriunde sub form un input care sa respecte regula
el4 = chrome.find_element(
  By.XPATH,
  '//form//input[@id="first-name"]'
)

el4.send_keys('y')

# selector by Xpath - selectare elem din lista - index incepe de la 1
el5 = chrome.find_element(
  By.XPATH,
  '(//input[@class="form-control"])[2]'
)

el5.send_keys('S')

# selector by Xpath - OR primul gasit dintre variante
s = chrome.find_element(
  By.XPATH,
  '//input[@id="last-name1"] | //input[@id="last-name2"]'
)
# stergem valorile din input
s.clear()
s.send_keys('Popa')

# selector by Xpath - in f de textul partial
# + luam textul de pe el cu proprietatea text
full_text = chrome.find_element(
  By.XPATH,
  '//a[contains(text(), "Sub")]'
).text
print(full_text)

# selector by Xpath -  in f de textul vizibil
chrome.find_element(By.XPATH, '//a[text()="Submit"]').click()
```

#### XPATH NAVIGATION
```python
"""
x y navigation
cu parent in sus
cu /elem_type - ajungem la elementul copil
cu //elem_type - cauta prin toti descendentii
cu parent::elem_type in sus
cu following-sibling::elem_type - urmatorul frate de la 
acelasi nivel
cu preceding-sibling::elem_type - fratele anterior de la
acelasi nivel
//label[text()='First name']/parent::strong
/following-sibling::input/preceding-sibling::strong

"""
```

```python
# cu ajutorul unei functii cand avem foarte multe
# elemente de acelasi tip si vrem sa parametrizam selectorul
def formy_input(placeholder_text, input_value):
    input = chrome.find_element(
      By.XPATH,
      f'//input[@placeholder="{placeholder_text}"]'
    )
    input.clear()
    input.send_keys(input_value)

formy_input('Enter first name', 'ANDY')
formy_input('Enter last name', 'Popa')
```


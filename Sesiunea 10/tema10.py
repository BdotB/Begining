
# OBLIGATORIU - grad de dificultate: Usor spre Mediu
#
#
# 1. Implementează o clasă Login care să moștenească unittest.TestCase.
#
# In metoda de setUp():
# - seteaza driver-ul (instanta de browser)
# - acceseaza site-ul 'https://the-internet.herokuapp.com/'
# - click pe Form Authentication

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.find_element(By.LINK_TEXT, 'Form Authentication').click()

# In metoda de tearDown():
# - quit la browser

    def tearDown(self):
        self.driver.quit()
# ● Test 1
# - Verifică dacă noul url e corect

    def test_new_url_is_correct(self):
        expected_url = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(self.driver.current_url, expected_url)

# ● Test 2
# - Verifică dacă page title e corect (page title este tag-ul title din <head>)
    def test_page_title_is_correct(self):
        expected_title = 'The Internet'
        self.assertEqual(self.driver.title, expected_title)

# ● Test 3
# - Verifică daca textul de pe elementul xpath=//h2 e corect
    def test_heading_text_is_correct(self):
        expected_heading = 'Login Page'
        heading = self.driver.find_element(By.XPATH, '//h2').text
        self.assertEqual(heading, expected_heading)


# ● Test 4
# - Verifică dacă butonul de login este displayed
    def test_login_button_is_displayed(self):
        login_button = self.driver.find_element(By.CSS_SELECTOR, '#login button')
        self.assertTrue(login_button.is_displayed())

# ● Test 5
# - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
  def test_elemental_selenium_link_href_is_correct(self):
        expected_href = 'http://elementalselenium.com/'
        link = self.driver.find_element(By.LINK_TEXT, 'Elemental Selenium')
        self.assertEqual(link.get_attribute('href'), expected_href)

# ● Test 6
# - Lasă goale user și pass
# - Click login
# - Verifică dacă eroarea e displayed
  def test_empty_username_and_password_show_error(self):
        self.driver.find_element(By.ID, 'username').send_keys('')
        self.driver.find_element(By.ID, 'password').send_keys('')
        self.driver.find_element(By.CSS_SELECTOR, '#login button').click()
        error = self.driver.find_element(By.ID, 'flash').text
        self.assertTrue('Your username is invalid!' in error)

# ● Test 7
# - Completează cu user și pass invalide
# - Click login
# - Verifică dacă mesajul de pe eroare e corect
# - Este și un x pus acolo extra așa că vom folosi soluția de mai jos
# expected = 'Your username is invalid!'
# self.assertTrue(expected in actual, 'Error message text is
# incorrect')
    def test_invalid_username_and_password_show_error(self):
        self.driver.find_element(By.ID, 'username').send_keys('invalid')
        self.driver.find_element(By.ID, 'password').send_keys('invalid')
        self.driver.find_element(By.CSS_SELECTOR, '#login button').click()
        error = self.driver.find_element(By.ID, 'flash').text
        expected_error = 'Your username is invalid!'
        self.assertTrue(expected_error in error)
# ● Test 8
# - Lasă goale user și pass
# - Click login
# - Apasă x la eroare
# - Verifică dacă eroarea a dispărut
    def test_close_error_removes_error(self):
        self.driver.find_element(By.ID, 'username').send_keys('')
        self.driver.find_element(By.ID, 'password').send_keys('')
        self.driver.find_element(By.CSS_SELECTOR, '#login button').click()
        close = self.driver.find_element(By.CSS_SELECTOR, '#flash > .close')
        close.click()
        error_displayed = EC.visibility_of_element_located((By.ID, 'flash'))
        self.assertFalse(error_displayed(self.driver))

# ● Test 9
# - Ia ca o listă toate //label
# - Verifică textul ca textul de pe ele să fie cel așteptat (Username și
# Password)
# - Aici e ok să avem 2 asserturi
  def test_labels_have_expected_text(self):
        expected_labels = ['Username', 'Password']
        labels = self.driver.find_elements(By.XPATH, '//label')
        self.assertEqual(len(labels), len(expected_labels))
        for i, label in enumerate(labels):
            self.assertEqual(label.text, expected_labels[i])


# ● Test 10
# - Completează cu user și pass valide
# - Click login
# - Verifică ca noul url CONTINE /secure
# - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
# - Verifică dacă elementul cu clasa=’flash succes’ este displayed
#
# - Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’

    def test_login_success(self):
        self.driver.find_element(By.ID, "username").send_keys("tomsmith")
        self.driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-in").click()
        # Verifică ca noul url CONTINE /secure
        self.assertIn('/secure', self.driver.current_url)
        # Folosește un explicit wait pentru elementul cu clasa ’flash succes’
        success_msg = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "flash.success")))
        # Verifică dacă elementul cu clasa=’flash succes’ este displayed
        self.assertTrue(success_msg.is_displayed())
        # Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’
        self.assertIn('secure area!', success_msg.text)

# ● Test 11
# - Completează cu user și pass valide
# - Click login
# - Click logout
# - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login
    def test_logout(self):
    self.driver.find_element(By.ID, "username").send_keys("tomsmith")
    self.driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-in").click()
    # Verifică ca noul url CONTINE /secure
    self.assertIn('/secure', self.driver.current_url)
    self.driver.find_element(By.CSS_SELECTOR, ".icon-2x.icon-signout").click()
    # Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login
    self.assertEqual(self.driver.current_url, "https://the-internet.herokuapp.com/login")

# OPTIONAL - grad de dificultate: Mediu spre greu: may need Google
# ● Test 12 - brute force password hacking
# - Completează user tomsmith
# - Găsește elementul //h4
# - Ia textul de pe el și fă split după spațiu. Consideră fiecare cuvânt ca o
# potențială parolă.
# - Folosește o structură iterativă prin care să introduci rând pe rând
# parolele și să apeși pe login.
# - La final testul trebuie să îmi printeze fie
# ‘Nu am reușit să găsesc parola’
# ‘Parola secretă este [parola]’


from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# Configuraciones
DELAY = 10  # Tiempo de espera en segundos para cada enlace.
BROWSER = 'Firefox'  # Elije entre 'Firefox', 'Chrome', 'Brave', 'Edge', o 'Safari'.
VISIBLE_MODE = True  # True para ver el navegador mientras se ejecuta, False para modo silencioso.
TIMEOUT = 15  # Tiempo máximo para cargar una página.

def check_link_status(driver, link, delay):
    try:
        driver.get(link)
    except TimeoutException:
        return "Unknown"  # No pudimos cargar la página en el tiempo esperado.

    time.sleep(delay)
    try:
        driver.find_element(By.XPATH, "//*[contains(text(), 'WOO HOO!')]")
        return "Used"
    except NoSuchElementException:
        pass

    try:
        driver.find_element(By.XPATH, "//form[contains(@class, 'MintForm_form__NE__8')]")
        return "Not Used"
    except NoSuchElementException:
        pass

    return "Unknown"

def initialize_browser():
    if BROWSER == 'Firefox':
        options = webdriver.FirefoxOptions()
        if not VISIBLE_MODE:
            options.add_argument('-headless')
        driver = webdriver.Firefox(options=options)
        driver.set_page_load_timeout(TIMEOUT)
        return driver
    elif BROWSER == 'Chrome':
        options = webdriver.ChromeOptions()
        options.headless = not VISIBLE_MODE
        return webdriver.Chrome(options=options)
    elif BROWSER == 'Brave':
        options = webdriver.ChromeOptions()
        options.binary_location = 'path_to_brave_browser'  # Añade el path al ejecutable de Brave.
        options.headless = not VISIBLE_MODE
        return webdriver.Chrome(chrome_options=options)
    elif BROWSER == 'Edge':
        options = webdriver.EdgeOptions()
        options.use_chromium = True
        options.headless = not VISIBLE_MODE
        return webdriver.Edge(options=options)
    elif BROWSER == 'Safari':
        # Safari no soporta modo silencioso directamente.
        return webdriver.Safari()

def main():
    driver = initialize_browser()

    used_links = []
    not_used_links = []
    unknown_links = []

    with open('links.txt', 'r') as file:
        links = [line.strip() for line in file]

    start_time = time.strftime('%Y-%m-%d %H:%M:%S')
    for link in links:
        status = check_link_status(driver, link, DELAY)
        if status == "Used":
            used_links.append(link)
        elif status == "Not Used":
            not_used_links.append(link)
        else:
            unknown_links.append(link)
    end_time = time.strftime('%Y-%m-%d %H:%M:%S')

    driver.quit()

    with open('used-links.txt', 'w') as f:
        f.write(f"Checked on: {start_time} to {end_time}\n")
        for link in used_links:
            f.write(link + '\n')

    with open('claimable-links.txt', 'w') as f:
        f.write(f"Checked on: {start_time} to {end_time}\n")
        for link in not_used_links:
            f.write(link + '\n')

if __name__ == "__main__":
    main()

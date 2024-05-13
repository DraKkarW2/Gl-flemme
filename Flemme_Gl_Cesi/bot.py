from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-dev-shm-usage')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")

driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get('https://auth.global-exam.com/login')

try:

    username = driver.find_element(By.ID, 'email')
    password = driver.find_element(By.ID, 'password')
    button = driver.find_element(By.CLASS_NAME, 'button-solid-primary-big')

    username.send_keys("email")
    password.send_keys("password")
    button.click()

    button_cesi_acc= driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div/div/div/div[1]/div')
    button_cesi_acc.click()

    button_parcours = driver.find_element(By.XPATH, '//*[@id="app"]/div/header/div/div[3]/div/ul/li[2]/span/a')
    button_parcours.click()

    button_continue =  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/main/div[1]/div/div/div[2]/div[3]/button')))
    button_continue.click()

    activités = driver.find_elements(By.CLASS_NAME,'w-15 h-15 relative flex items-center justify-center lg:w-30 lg:h-30 rounded-full bg-listening')

    '''checkbox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/main[2]/div/div[2]/div/div[2]/div/div[3]/label[2]/div')))
    checkbox.click()


    test_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'button-solid-default-small')))
    test_button.click()
   
    # Récupérer tous les blocs de questions et réponses
    questions = driver.find_elements(By.CSS_SELECTOR, 'div.w-full')

    for question in questions:
        # Récupérer le texte de la question
        question_text = question.text.strip()
        print("Question:", question_text)
        
        # Trouver les réponses possibles à la question
        answers = question.find_elements(By.XPATH, '../following-sibling::div//label//div[@class="flex items-center justify-center shrink-0 w-6 h-6 border rounded mr-4"]')
        
        # Parcourir chaque réponse possible
        possible_answers = []
        for answer in answers:
            # Récupérer le texte de la réponse
            answer_text = answer.text.strip()
            possible_answers.append(answer_text)
        
        print("Réponses possibles:", possible_answers)
        
        # Répondez aléatoirement à la question (remplacez ceci par votre logique de réponse)
        # par exemple, choisissez une réponse au hasard
        # import random
        # random_answer = random.choice(possible_answers)
        # print("Réponse choisie:", random_answer)'''

except Exception as e:
    print("Error:", e)
finally:
    # Ajoutez une pause pour voir le résultat avant de fermer le navigateur
    input("Press Enter to close...")
    driver.quit()

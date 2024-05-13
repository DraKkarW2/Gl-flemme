from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def botGl(email,passwords,time_skip):
    def log(message):
        print(f"[LOG] {message}")

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
        log("Attempting to log in...")
        username = driver.find_element(By.ID, 'email')
        password = driver.find_element(By.ID, 'password')
        button = driver.find_element(By.CLASS_NAME, 'button-solid-primary-big')

        username.send_keys(email)
        password.send_keys(passwords)
        button.click()
        log("Login submitted.")

        log("Clicking CESI account button...")
        button_cesi_acc = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/main/div/div/div/div/div[1]/div'))
        )
        button_cesi_acc.click()
        log("CESI account button clicked.")

        log("Navigating to parcours...")
        button_parcours = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/header/div/div[3]/div/ul/li[2]/span/a'))
        )
        button_parcours.click()
        log("Navigated to parcours.")

        log("Clicking continue button...")
        button_continue = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/main/div[1]/div/div/div[2]/div[3]/button'))
        )
        button_continue.click()
        log("Continue button clicked.")

        log("Waiting for activity buttons to be visible...")
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'card-hover')))
        log("Activity buttons are visible.")

        activities = driver.find_elements(By.CLASS_NAME, 'card-hover')
        log(f"Found {len(activities)} activity buttons.")

        for activity in activities:
            try:
                activity_text_element = activity.find_element(By.TAG_NAME, 'p')
                activity_text = activity_text_element.text.strip()

                if activity_text in ["Introduction","Work environments - Offices","Colleagues and working relationships","Present continuous - I am doing","Present continuous - I am doing","Describing procedures (how something works, problems, processes, etc.)"]:
                    log("Skipping 'Introduction' activity.")
                    continue

                score_element = WebDriverWait(activity, 2).until(
                    EC.presence_of_element_located((By.XPATH, './/span[contains(@class, "font-bold")]'))
                )
                score_text = score_element.text.strip()

                if score_text == "100%":
                    continue
            except Exception as e:
                log(f"Exception while checking activity: {e}")
                activity.click()
                log("Clicked on an activity.")
                break

        try:
            start_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//button[text()="Démarrer"]'))
            )
            if start_button.is_displayed():
                start_button.click()
                log("Clic 'Démarrer' button.")
        except Exception as e:
            log(f"Exception clicking 'Démarrer': {e}")

        while True:
            try:
                progress_text = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, '//p[contains(@class, "progress-bar-arrow-top")]'))
                ).text.strip()
                current_progress, total_progress = map(int, progress_text.split('/'))
                log(f"Progress: {current_progress}/{total_progress}")

                if current_progress == total_progress:
                    log("All questions have been answered.")
                    break

                correction_buttons = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, '//span[text()="Voir la correction"]'))
                )
                for button in correction_buttons:
                    try:
                        button.click()
                        log("Clicked 'Voir la correction' button.")
                        time.sleep(1)
                    except Exception as e:
                        log(f"Error clicking 'Voir la correction' button: {e}")

                labels = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'bg-success-05'))
                )
                for label in labels:
                    try:
                        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", label)
                        time.sleep(1)

                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(label))
                        label.click()
                        log("Clicked a label with class 'bg-success-05'.")
                        time.sleep(1)
                    except Exception as e:
                        log(f"Error clicking label: {e}")

                time.sleep(2)

                valider_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "button-solid-primary-large") and text()="Valider"]'))
                )
                valider_button.click()
                log("Clicked 'Valider' button.")
                time.sleep(5)

            except Exception as e:
                log(f"Error during process: {e}")
                break

        log("Process completed. Waiting 30 minutes before clicking 'Terminer'.")
        time.sleep(time_skip)  # Attendre 30 minutes 30 * 60

        try:
            terminer_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "button-solid-primary-large") and text()="Terminer"]'))
            )
            terminer_button.click()
            log("Clicked 'Terminer' button.")
        except Exception as e:
            log(f"Error clicking 'Terminer' button: {e}")

        log("Waiting to close the browser.")
        time.sleep(5)

    except Exception as e:
        log(f"Error: {e}")
    finally:
        input("Press Enter to close...")
        driver.quit()

email = "email"
passwords = "password"
time_skip = 1    
botGl(email,passwords,time_skip)
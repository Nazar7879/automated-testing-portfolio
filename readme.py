# Коли ми шукаж щлях до файлу ми може мо використати:
# ID,CLASS,NAME,TAG
#driver.save_screenshot('screenshot.png') - це робить скрінщоти 
#driver.maximize_window()  це робить повний екран
#driver.implicitly_wait(10)  # Чекає до 10 секунд для всіх елементів


# element = driver.find_element(By.ID, 'myElement') Якщо потрібно зробити скріншот не всієї сторінки, а конкретного елемента:   
# element.screenshot('element_screenshot.png')

#Дія з випадаючими списками (Dropdown)
# Для роботи з випадаючими списками використовуйте бібліотеку Select:

# python
# Копіювати код
# from selenium.webdriver.support.ui import Select

# select = Select(driver.find_element(By.ID, 'dropdown'))
# select.select_by_value('optionValue')  # Вибрати опцію за значенням
# select.select_by_visible_text('Option Text')  # Вибрати опцію за текстом


from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    ElementClickInterceptedException,
    InvalidElementStateException,
    NoAlertPresentException
)

try:
    # Тут має бути ваша дія, наприклад, пошук елемента чи взаємодія з ним
    element = driver.find_element_by_id('element_id')
    element.click()

except NoSuchElementException:
    print("Елемент не знайдено на сторінці.")

except TimeoutException:
    print("Час очікування для знаходження елемента або умови сплив.")

except StaleElementReferenceException:
    print("Елемент більше не є актуальним у DOM.")

except ElementNotInteractableException:
    print("Елемент не можна взаємодіяти, можливо він прихований або неактивний.")

except ElementClickInterceptedException:
    print("Клік на елемент перехоплено іншим елементом на сторінці.")

except InvalidElementStateException:
    print("Елемент знаходиться в некоректному стані для дії (наприклад, поле для введення неактивне).")

except NoAlertPresentException:
    print("Алерт на сторінці відсутній.")
## 1 Feladat: Pitagorasz-tétel

# """A program töltse be a Pitagorasz-tétel app-ot az [https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html](https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html) oldalról.
#
# Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a Pitagorasz-tétel appban:
#
# Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!"""
#
#
# * Helyesen jelenik meg az applikáció betöltéskor:
#     * a: <üres>
#     * b: <üres>
#     * c: <nem látszik>
#
# * Számítás helyes, megfelelő bemenettel
#     * a: 2
#     * b: 3
#     * c: 10
#
# * Üres kitöltés:
#     * a: <üres>
#     * b: <üres>
#     * c: NaN

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.headless = False


driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 600, 600)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html"

driver.get(URL)
time.sleep(2)

input_a = driver.find_element_by_id("a")
input_b = driver.find_element_by_id("b")


submit_button = driver.find_element_by_id("submit")
result_text = driver.find_element_by_id("result")

test_data = ["2", "3", ""]
reference_data = ["10", "NaN"]


#* Helyesen jelenik meg az applikáció betöltéskor:
#     * a: <üres>
#     * b: <üres>
#     * c: <nem látszik>
def correct_app_visible_test():
    assert input_a != ""
    assert input_b != ""

print(input_a, input_b)

# * Üres kitöltés:
#     * a: <üres>
#     * b: <üres>
#     * c: NaN
def empty_input_field_test():
    submit_button.click()
    assert result_text.text == reference_data[1]

# * Számítás helyes, megfelelő bemenettel
#     * a: 2
#     * b: 3
#     * c: 10
def correct_output_test():
    submit_button.click(test_data[0][1])
    assert result_text.text == reference_data[0]


#print(result_text.text)

driver.quit()





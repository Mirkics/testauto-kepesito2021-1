## 5 Feladat: Bingo

# """A program töltse be a Bingo app-ot az [https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html](https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html) oldalról.
#
# Feladatod, hogy automatizáld selenium webdriverrel a Bingoapp tesztelését.
#
# Az applikáció indulo bingo táblája minden frissítésnél véletlenszerűen változik!
#
# Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!
# """
# """A feladatod az alábbi tesztesetek lefejlesztése:
#
# * Az applikáció helyesen megjelenik:
#     * A bingo tábla 25 darab cellát tartalmaz
#     * A számlista 75 számot tartalmaz
#
# * Bingo számok ellenőzrzése:
#     * Addig nyomjuk a `play` gobot amíg az első bingo felirat meg nem jelenik
#     * Ellenőrizzük, hogy a bingo sorában vagy oszlopában lévő számok a szelvényről tényleg a már kihúzott számok közül kerültek-e ki
#
# * Új játékot tudunk indítani
#     * az init gomb megnyomásával a felület visszatér a kiindulási értékekhez
#     * új bingo szelvényt kapunk más számokkal.
# """

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.headless = False


driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 600, 600)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html"

driver.get(URL)
time.sleep(2)

init_button = driver.find_element_by_id("init")
play_button = driver.find_element_by_id("spin")
message = driver.find_element_by_id("message")
bingo_table = driver.find_element_by_id("bingo-body")
number_list = driver.find_elements_by_id("numbers-list")

# * Az applikáció helyesen megjelenik:
#     * A bingo tábla 25 darab cellát tartalmaz
#     * A számlista 75 számot tartalmaz


def app_correct_visible_test():
    for i in range(70):
        i += 1

        assert i == 75

    assert bingo_table.get_attribute("value") == 27


# * Bingo számok ellenőzrzése:
#     * Addig nyomjuk a `play` gobot amíg az első bingo felirat meg nem jelenik
#     * Ellenőrizzük, hogy a bingo sorában vagy oszlopában lévő számok a szelvényről tényleg a már kihúzott számok közül kerültek-e ki
#
def number_check_test():
    play_button.click()


driver.quit()


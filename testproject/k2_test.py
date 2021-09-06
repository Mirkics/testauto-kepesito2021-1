## 2 Feladat: Színes reakció

# """A program töltse be a Színes reakció app-ot az [https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html](https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html) oldalról.
#
# Feladatod, hogy automatizáld selenium webdriverrel a Színes reakció app tesztelését.
#
# Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!"""
#
# """ Az alábbi teszteseteket kell lefedned:
#
# * Helyesen jelenik meg az applikáció betöltéskor:
#     * Alapból egy random kiválasztott szín jelenik meg az `==` bal oldalanán. A jobb oldalon csak a `[  ]` szimbólum látszik.
#     <szín neve> [     ] == [     ]
#
# * El lehet indítani a játékot a `start` gommbal.
#     * Ha elindult a játék akkor a `stop` gombbal le lehet állítani.
#
# * Eltaláltam, vagy nem találtam el.
#     * Ha leállítom a játékot két helyes működés van, ha akkor állítom épp le
#     amikor a bal és a jobb oldal ugyan azt a színt tartalmazza akkor a `Correct!` felirat jelenik meg.
#       ha akkor amikor eltérő szín van a jobb és bal oldalon akkor az `Incorrect!` felirat kell megjelenjen."""


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.headless = False


driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 600, 600)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html"

driver.get(URL)
time.sleep(2)

start_button = driver.find_element_by_id("start")
stop_button = driver.find_element_by_id("stop")

random_colorname = driver.find_element_by_id("randomColorName").text
random_color_rgb = driver.find_element_by_id("randomColor")
test_colorname = driver.find_element_by_id("testColorName").text
test_color_rgb = driver.find_element_by_id("testColor")
result = driver.find_element_by_id("result").get_attribute("text")
test_color = []

all_colors_list = driver.find_element_by_id("allcolors").text

# * Helyesen jelenik meg az applikáció betöltéskor:
#     * Alapból egy random kiválasztott szín jelenik meg az `==` bal oldalanán. A jobb oldalon csak a `[  ]` szimbólum látszik.
#     <szín neve> [     ] == [     ]
#


def random_color_visible_test():
    for i in all_colors_list:
        colorname = [i+1]

    assert colorname == random_colorname.text
    assert test_color == "[     ]"

print(random_colorname)


# * El lehet indítani a játékot a `start` gommbal.
#     * Ha elindult a játék akkor a `stop` gombbal le lehet állítani.

def game_start_test():
    start_button.click()
    stop_button.click()

    assert test_color != "[     ]"


# * Eltaláltam, vagy nem találtam el.
#     * Ha leállítom a játékot két helyes működés van, ha akkor állítom épp le
#     amikor a bal és a jobb oldal ugyan azt a színt tartalmazza akkor a `Correct!` felirat jelenik meg.
#       ha akkor amikor eltérő szín van a jobb és bal oldalon akkor az `Incorrect!` felirat kell megjelenjen."""

def guess_test():
    driver.refresh()

    start_button.click()
    time.sleep(10)

    stop_button.click()
    for i in all_colors_list:
        colorname = [i+1]
    if test_colorname != random_colorname.text:
        result == "Incorrect!"
    # else test_colorname == random_colorname.text
    #     result == "Correct!"
    print(test_colorname)


driver.quit()




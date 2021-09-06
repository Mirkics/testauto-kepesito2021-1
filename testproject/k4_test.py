## 4 Feladat: Műveletek karakterekkel

# """A program töltse be a Műveletek karakterekkel app-ot az [https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html](https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html) oldalról.
#
# Feladatod, hogy automatizáld selenium webdriverrel a Műveletek karakterekkel app tesztelését.
#
# Az applikáció minden frissítésnél véletlenszerűen változik!
#
# Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!"""
#
# """Az alábbi teszt eseteket kell kidolgozzad:
#
# * Helyesen betöltődik az applikáció:
#     * Megjelenik az ABCs műveleti tábla, pontosan ezzel a szöveggel:
#       * !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
#
# * Megjelenik egy érvényes művelet:
#     * `chr` megző egy a fenti ABCs műveleti táblából származó karaktert tartalmaz
#     * `op` mező vagy + vagy - karaktert tartlamaz
#     * `num` mező egy egész számot tartalamaz
#
# * Gombnyomásra helyesen végződik el a random művelet a fenti ABCs tábla alapján:
#     * A megjelenő `chr` mezőben lévő karaktert kikeresve a táblában
#     * Ha a `+` művelet jelenik meg akkor balra lépve ha a `-` akkor jobbra lépve
#     * A `num` mezőben megjelenő mennyiségű karaktert
#     * az `result` mező helyes karaktert fog mutatni
# """

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.headless = False


driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 600, 600)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html"

driver.get(URL)

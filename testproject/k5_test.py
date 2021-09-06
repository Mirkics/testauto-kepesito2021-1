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


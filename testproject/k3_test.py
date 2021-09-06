## 3 Feladat: Alfanumerikus mező

# """A program töltse be a Alfanumerikus mezőapp-ot az [https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html](https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html) oldalról.
#
# Feladatod, hogy automatizáld selenium webdriverrel a Alfanumerikus mező app tesztelését.
# Az ellenőrzésekhez használj `pytest` keretrendszert. A tesztjeidben használj `assert` összehasonlításokat használj!
# """
# """A cél a mező validáció tesztelése:
#
# * Helyes kitöltés esete:
#     * title: abcd1234
#     * Nincs validációs hibazüzenet
#
# * Illegális karakterek esete:
#     * title: teszt233@
#     * Only a-z and 0-9 characters allewed.
#
# * Tul rövid bemenet esete:
#     * title: abcd
#     * Title should be at least 8 characters; you entered 4.
# """

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.headless = False


driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_size(1000, 600, 600)
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html"

driver.get(URL)
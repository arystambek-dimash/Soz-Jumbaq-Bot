import requests
from bs4 import BeautifulSoup as bs
import random
URL = ["http://kaz.slovopedia.com/147/53392-1.html",
       "http://kaz.slovopedia.com/147/53393-14.html",
       "http://kaz.slovopedia.com/147/53395-2.html",
       "http://kaz.slovopedia.com/147/53396-6.html",
       "http://kaz.slovopedia.com/147/53409-15.html",
       "http://kaz.slovopedia.com/147/53419-0.html",
       "http://kaz.slovopedia.com/147/53914-0.html"]
rand_int = random.randint(0,6)

r = requests.get(URL[rand_int])
s = bs(r.text, "html.parser")
sozdik = s.find_all('div',class_ = "row_word")


clear_sozdik = [c.text for c in sozdik]

length = len(clear_sozdik)
rand_soz_int = random.randint(1,length)
while True:
       try:
              rand_soz = clear_sozdik[rand_soz_int-1]
              break
       except ValueError:
              print(ValueError)

print(rand_soz)


EREJE_COMMAND = """
Būl oiyn söz jūmbaq oiyny, 
iağni bot oiyndy bastağan 
adamğa söz beredı al sözdı 
alğan adam basqa oiynşylarğa 
tüsındıredı egerde basqa 
oiynyşylardyñ bıreuı sözdı 
tabatyn bolsa sözdı sol 
tapqan adam jasyrady

!!Oiyn tolygimen qazaq tilinde
"""

HELP_COMMAND = """
/komek - bottyñ funksiasyn sūrau
/ereje - oiynnyñ qalai oinalatynyn sūrau
"""


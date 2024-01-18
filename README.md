# Projekts
Ir situācijas, kad cilvēkam nav pieejama pašam sava automašīna un ir jāvēršās pie nomas. Viens no man zināmākajiem auto nomas uzņēmumiem
ir AVIS, tomēr tur ieejot bieži vien apjūku, jo šim uzņēmumam ir vairākas vietnes un ir grūti atrast, kurā var izvēlēties mašīnu.
Savukārt, atrodot šo vietni, kurā var iznomāt auto, filtrēšanas opcijas nav tik redzamā vietā. Lai atrisinātu šo problēmu un vairs
nebūtu jāmeklē ne pareizā vietne, ne filtrēšanas opcijas, var palaist šo kodu, kur piedāvāju lietotājam ievadīt degvielas veidu
un kārbu, kādu vēlētos.

Automatizējot šo vietni paveicu šādas lietas, ko lietotājs var novērot: programma atver AVIS vietni, kas ir automašīnu nomai paredzēta.
Lietotājs var ievadīt kādu degvielu un kārbu vēlētos iznomāt terminālī, vēlāk ieliekot filtrā šīs opcijas un parādot lietotājam.

Izmantotās Python bibliotēkas:

  import time - bibliotēka ļauj ieviest pauzes koda izpildes laikā, piemēram, atverot vietni tiek izpildīta 2 sekunžu ilga pauze, lai 
tā atvērtos.

  import selenium - bibliotēka ļauj automatizēt tīmekļa pārlūkprogrammu, kā arī veikt dažādas darbības tīmekļa lapās, kā arī ļauj
izmantot piedāvātās funkcijas, lai kontrolētu tīmekļa pārlūkus, izpildītu darbības lapās. Izmantoju to, piemēram, lapas atvēršanai, 
formas aizpildīšanai, interaktīvai darbību simulēšanai.

  from selenium import webdriver - šīs pakotnes pamatā ir piedāvāt funkcijas un metodes, lai kontrolētu tīmekļa pārlūkprogrammas 
darbības. WebDriver ļauj automatizēt tīmekļa pārlūkprogrammu darbību, piemēram, atvērt pārlūkprogrammu, pārvietoties pa lapām,
noklikšķināt uz pogām utt.

  from selenium.webdriver.chrome.service import Service - šī pakotne tiek izmantota, lai konfigurētu un pārvaldītu pārlūkprogrammas 
pakalpojumus, piemēram, Chrome darbības parametrus.

  from selenium.webdriver.common.by import By - šī pakotne nodrošina dažādas metodes, ar kurām var norādīt, kā identificēt elementus 
web lapā, piemēram, elementa atrašana, noklikšķināšana, teksta ievadīšana.

  from selenium.webdriver.support import expected_conditions as EC - šis modulis nodrošina dažādus waiting conditions, kas ir 
noderīgi, kad automatizē pārlūkprogrammas darbības ar Selenium WebDriver.

  from selenium.webdriver.support.ui import WebDriverWait -  šī pakotne nodrošina iespēju veikt gaidīšanu pārlūkprogrammas 
darbībās, 
piemēram, kamēr kāds elements kļūst redzams vai uz tā var uzklikšķināt.

Metožu apraksts:

  1. Konfigurē ChromeDriver - importē pakotnes

  2. Atver mājaslapu - atver mājaslapu izmantojot driver.get.url(), sameklē cookies pogu un uzklikšķina "Es piekrītu", lietotājs
ievada degvielas veidus (atdalot ar komatu)

  3. Iegūst nepieciešamos datus un atlasa/filtrē - iet cauri katram ievadītājam degvielas veidam un dotajiem degvielas veidiem no
html dokumenta un ieklikšķina, ja atbilst nosacījumiem, atkārto šīs pašas darbības ar kārbu ievadīto.

  4. Programma aizverās - kad viss tiek izfiltrēts un apskatīts chrome webdriver aizverās.

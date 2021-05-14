###### Samuli Karvinen

## Robottikäsi

### Esittely

#### Tiedosto- ja kansiorakenne

##### Juurikansio
- Projektisuunnitelma.pdf
- Projektityön dokumentti.pdf
- README.md

##### Sovelluskansio
- window.py (Window; ajettava ohjelma ja pääikkuna)
- robot.py  (Robot; robottikäden fyysiset ominaisuudet)
- robot_graphics_item.py (RobotGraphicsItem; robottikäden graafiset ominaisuudet)
- square.py (Square; laatikon fyysiset ominaisuudet)
- square_graphics_item.py (SquareGraphicsItem; laatikon graafiset ominaisuudet)
- text_graphics_item.py (TextGraphicsItem; graafisten tekstien ominaisuudet)
- kinematics_test.py (UnitTest; Robot-luokan kinematiikan yksikkötestaus)

#### Asennusohje
Ohjelma tarvitsee toimiakseen kirjastot PyQt5 sekä NumPy:
>PyQt5 asennetaan komentorivillä komennolla `pip install pyqt5`

>NumPy asennetaan komentorivillä komennolla `pip install numpy`

#### Käyttöohje
Ohjelma ajetaan suorittamalla Pythonilla tiedosto window.py, johon on muutama eri vaihtoehto:

> Ohjelman voi suorittaa komentorivillä Sovellus-kansiossa komennolla `python window.py`

> Ohjelman voi suorittaa myös PyCharmissa seuraavasti:
> 1.  Avaa Sovellus-kansio PyCharmissa ja avaa tiedosto window.py.
> 2.  Klikkaa koodia oikealla hiiren painikkeella ja klikkaa nappia 'Run 'window'' hiiren vasemmalla painikkeella.

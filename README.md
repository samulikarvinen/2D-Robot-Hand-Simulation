Samuli Karvinen, 602945

••Checkpoint••

1. Mitä ominaisuuksia olet jo toteuttanut projektiisi?

   >Manuaalinen ohjaus, imun ohjaus (esineen siirtäminen), graafinen
   käyttöliittymä, robotin ja esineen luokat, sekä niiden graafiset luokat.

2. Käyttöohje

   Voiko ohjelmaa jo ajaa?
    >Kyllä.
    
   Kuinka ohjelma käynnistetään?
    >Suorita ohjelma 'window.py'
    
   Mitä sillä voi tässä vaiheessa tehdä?
    >Robottikättä voidaan ohjata manuaalisesti kahdella
     sliderilla ja kappaletta voidaan siirtää imun avulla.

3. Aikataulu

   Kuinka paljon olet jo käyttänyt aikaa projektiin?
    >Noin 36 tuntia.
    
   Onko ilmennyt muutoksia suunnitelman aikatauluun?
    >Olen saanut enemmän valmiiksi kuin mitä suunnittelin.

4. Muuta

   Onko ilmaantunut erityisiä ongelmia?
    >Kappaleen liikuttamisessa on hieman ongelmia. Olisi kiva jos osa, johon
     robottikäden end-effector osuu painettaessa suction-näppäintä, jäisi
     pisteeksi, josta robottikäsi pitää kiinni kappaletta liikuttaessa.
     Tällä hetkellä liikuttaessa end-effectori tarrautuu kiinni aina kappaleen
     keskipisteestä onnistuneessa suctionissa.
      
   Oletko joutunut tekemään muutoksia suunnitelmaasi?
    >Muutin reilusti ohjelman rakennetta. 'Pääohjelmana' toimii window.py ja
     poistin erikseen manual.py sekä auto.py tiedostot sillä lisäsin ne osaksi
     robot.py:n Robot-luokkaa. PyQt5 opiskellessani tajusin myös, että on
     helpompaa jos jokaisella esineellä olisi oma graafinen luokkansa ja siksi
     lisäsin robot_graphics_item.py:n sekä square_graphics_item.py:n.


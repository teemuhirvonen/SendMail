# Säätietojen lähetys sähköpostiin

## Projektin tarkoitus

Tarkoituksena oli luoda python sovellus, joka hakee apin avulla säätiedot ja lähetää ne viikoittain sähköpostilla.

## Projektin toteutus

Ideana oli luoda yksinkertainen api jonka avulla haen sää tiedot omasta asuinkaupungistani ja lähettää ne omaan sähköpostiini maanantai aamuisin.

WeatherCall.py toimii tällä hetkellä ja käyttäjä pystyy tällä hetkellä syöttämään minkä kaupungin 5 päivän sää ennusteen haluaa.

WeatherWeekly.py ei tällä hetkellä pysty lähettämään sähköpostia ajastuksessa olevasta virheestä johtuen.

## Projektin ongelmat

Ensimmäinen ongelma tuli siitä, että googlen api vaatii tiukan todennuksen, jotta sen avulla pystyy lähettämään sähköposteja. Ratkaisin ongelman käyttämällä mockup sähköposti sovellusta. Kyseinen sivu ei vaadi todennuksia ja tarjosi ilmaisen käytön 50 sähköpostin lähettämiseen, joka sopi täydellisesti omaan testi käyttööni.

Toinen ongelma, jota en onnistunut korjaamaan tuli ajastuksen kanssa. Kun käytin ajastusta sovellus ei lähettänyt sähköpostia eikä antanut virheitä miksi viestiä ei lähetetty. Ohjelma kuitenkin tulostaa koodin lopussa olevan sähköposti lähetetty viestin joka kerta. Toistaiseksi en ole saanut ongelmaa korjattua.

## Linkkejä käytettäviin verkkosivuihin

<a href="https://mailtrap.io">Mailtrap</a>
<br>
<a href="https://openweathermap.org/">Open Weather Map</a>

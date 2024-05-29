# Project: brug als IOT device
## Raspberry pi en python
"Het brein" achter dit project is een raspberry pi (v3 B). Het besturingssysteem hierop is Rasbian OS (een linux distributie gebaseerd op debian).  
De python versie die gebruikt wordt is python 3.11.2

### Python
Met python worden diverse zaken in de raspberry pi aangestuurd. De communicatie met de qwiic via I2C en de verwerking van de data ontvangen van de sensor gebeuren via python (\~/Python/qwiic.py). De motor wordt ook aangestuurd met een bestand die de gpoi pinnen van de arduino aanstuurt (\~/Python/motor_control.py).  
Tijdens het testen werd sensor data ook aangemaakt met een python script (\~/Python/sensor_simulator.py), dit bestand genereert zowel een lijst met data, als een lijst met timestamps als een tekst bestand met beide.

#### HTML generator
De HTML die weergeven word is opgesteld aan de hand van een template, dit is een html bestand waar alles in staat die nodig is (standaard HTML structuur, opmaak, javascript code, knoppen met href naar url) behalve de sensorwaarden. Het html generator script (\~/Python/html_generator.py) deelt de template html op in 3 delen op de plaats waar de sensordata en de waarden voor de scale in de javascript code moeten komen. De sensordata wordt ingevoerd na het eerste deel en het tweede deel wordt ingevoegd na de sensordata daarna wordt de minimum en maximum waarde voor de scale ingevoegd zodat de scaling van de grafiek dynamisch wordt bijgewerkt en als laatste wordt het laatste onderdeel van de html toegevoegd. De html wordt dan naar een nieuw bestand geschreven(\~/web/generated_site.html) en deze wordt ook teruggegeven als string.

#### Qwiicscale
Om massa te meten werd er gebruik gemaakt van een qwiicscale i²c bordje. Dit bordje werd aangestuurd via de zelfgeschreven qwiic (\~/Python/qwiic.py) bibliotheek die de door de KULAB geleverde qwiicscale (\~/Python/qwiicscale.py) bibliotheek bevat. Er is ook een testbestand (\~/Python/test_qwiic.py) gemaakt om verschillende functies van de bibliotheken te testen. het uitvoerbestand (\~/Python/uitvoeren qwiic.py) dient als template van hoe de qwiic bibliotheek geïmplementeerd moet worden.


## Arduino brug besturing
Het Arduino-onderdeel beheert de brugsturing, verkeerslicht en buzzer op basis van de input van de Raspberry Pi en de MPU6050 sensor. De sturing van elk onderdeel en de input van de Raspberry Pi en de MPU6050, die via I2C gebeurd, verloopt via Arduino IDE (\~/Programma_brug/Programma_brug.ino). Verder wordt alle sensordate in de seriële monitor geplaatst, zijnde de actuele hoek waaronder de brug staat en de status van de inputs van de Raspberry Pi (omhoog of omlaag input).
De Arduino versie die gebruikt wordt is Arduino IDE 2.3.2.


## Flask web server
De data word weergegeven aan de hand van een webapp. Deze web app is gemaakt aan de hand van de python module flask. Dit is een verzameling van library's die het zeer makkelijk maken om een web applicatie op te zetten met python. (\~/Python/flask_server.py)
De webserver moet gestart worden op de raspberry pi met een "speciaal" commando (dus niet gewoon: python3 flask_server.py)

### HTML
De web app geeft een html bestand weer. Deze bevat knoppen die verwijzen naar urls om zo acties uit te voeren met de webapp aangezien deze een HTTP request doen die de web app kan detecteren. Er zijn verschillende urls om verschillende acties uit te voeren zoals de brug openen en sluiten.  
In de html is er ook een grafiek met sensordata te zien deze wordt geplot met javascript die emeded is in de html.  
Deze html word gegenereerd door een python script (\~/Python/html_generator.py) zodat de meetwaarden telkens worden vervangen.

### Javascript
Er wordt gebruik gemaakt van javascript om de data te plotten op een html canvas. Er wordt gebruik gemaakt van de library "charts.js" om een grafiek te plotten.


## Extra

### Version controll met git
Er wordt gebruik gemaakt van git versie beheer. Dit maakt het makkelijker om samen te werken en om de meest up-to-date bestanden op de raspberry pi te krijgen.

### flake.nix en flake.lock
In deze repository is een flake.nix en een flake.lock bestand aanwezig. Deze bestanden definiëren de project omgeving. Ze zorgen er voor dat je met iedere computer die de Nix packages manager kan gebruiken, in dezelfde omgeving kan werken (het installeert automatisch de juiste versie van python en de libs en ook de nodig IDE zoals de Arduino IDE en pycharm).
De flake.lock wordt automatisch gegenereerd door nix op basis van de flake.nix. De flake.lock beschrijft de exacte pakketten en van de software dus als op basis van deze lock "gebuild" word op een ander systeem zou dat het exact zelfde resultaat moeten leveren. De flake.lock kan worden vernieuwd met de flake.nix (enkel pycharm en arduino ide zullen een vernieuwd worden aangezien de python versie en die library's een vaste source hebben en dus een vaste versie).

### install_python_stuff.sh
Een bash scriptje die de nodige library's installeert adhb de apt pacakge manager. (Gewoon een bash script met de install commandos uit de opgaven). Dit scriptje maakt het makkelijker om alles te installeren op verschillende raspberry pi en om het systeem opnieuw op te zetten bij het opnieuw installeren.

### Ongebruikte prototype bestanden

#### (old)_flask_server.py
Dit was de eerste versie van de flask webserver. Dit werd vooral gebruikt om te testen hoe haalbaar het was om een eigen webserver op te zetten en als template. We besloten om een nieuwe bestand aan te maken omdat we de oude dan nog als referentie konden gebruiken.

#### main.py
Voor dat we besloten om een webserver te gebruiken was dit het script waar alles in ging samenkomen. Dit bestand werd vroeg in de ontwikkeling achtergelaten.

#### motor toggle + I2C_test.ino
Een script die aan de hand van I2C data naar de arduino stuurt. Was een eventuele piste voor de motoraansturing maar GPIO bleek veel simpeler. Om deze I2C signalen te ontvangen werd ook een arduino scrip geschreven.

#### original testing template.html
De eerste html die gebruikt werd als template. Hier werden verschillende methodes getest om data weer te geven (waarvan chart.js het makkelijkste en overzichtelijkste bleek). Er werd ook nog getest om eventueel tekst te gebruiken als grafiek (hoe hoger de waarde hoe meer symbolen op de lijn van het tijdstip).
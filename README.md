- # Project: brug als IOT device
- ## Raspberry pi en python
  "Het brein" achter dit project is een raspberry pi (v3 B). Het besturingssysteem hierop is Rasbian OS (een linux distributie gebaseerd op debian).  
  De python versie die gebruikt wordt is python 3.11.2  
-
- ### Python
  Met python worden diverse zaken in de raspberry pi aangestuurd. De communicatie met de qwiic via I2C en de verwerking van de data ontvangen van de sensor gebeuren via python (~/Python/qwiic.py). De motor wordt ook aangestuurd met een bestand die de gpoi pinnen van de arduino aanstuurt (~/Python/motor_control.py).  
  Tijdens het testen werd sensor data ook aangemaakt met een python script (~/Python/sensor_simulator.py), dit bestand genereert zowel een lijst met data, als een lijst met timestamps als een tekst bestand met beide.  
- #### HTML generator
  De HTML die weergeven word is opgesteld aan de hand van een template, dit is een html bestand waar alles in staat die nodig is (standaard HTML structuur, opmaak, javascript code, knoppen met href naar url) behalve de sensorwaarden. Het html generator script (~/Python/html_generator.py) deelt de template html op in 2 delen op de plaats waar de sensordata in de javascript code moet komen. De sensordata wordt ingevoerd na het eerste deel en het tweede deel wordt ingevoegd na de sensordata. De html wordt dan naar een nieuw bestand geschreven(~/web/generated_site.html)  
- #### Qwiic
-
- ## Flask web applications
  De data word weergegeven aan de hand van een webapp. Deze web app is gemaakt aan de hand van de python module flask. Dit is een verzameling van library's die het zeer makkelijk maken om een web applicatie op te zetten met python. (~/Python/flask_server.py)  
- #### HTML
  De web app geeft een html bestand weer. Deze bevat knoppen die verwijzen naar urls om zo acties uit te voeren met de webapp aangezien deze een HTTP request doen die de web app kan detecteren. Er zijn verschillende urls om verschillende acties uit te voeren zoals de brug openen en sluiten.  
  In de html is er ook een grafiek met sensordata te zien deze wordt geplot met javascript die emeded is in de html.  
  Deze html word gegenereerd door een python script (~/Python/html_generator.py) zodat de meetwaarden telkens worden vervangen.  
- #### Javascript
  Er wordt gebruik gemaakt van javascript om de data te plotten op een html canvas. Er wordt gebruik gemaakt van de library "charts.js" om een grafiek te plotten.  
-
- ## Extra
- ### Version controll met git
  Er wordt gebruik gemaakt van git versie beheer. Dit maakt het makkelijker om samen te werken en om de meest up-to-date bestanden op de raspberry pi te krijgen.  
- ### flake.nix en flake.lock
  In deze repository is een flake.nix en een flake.lock bestand aanwezig. Deze bestanden definiëren de project omgeving. Ze zorgen er voor dat je met iedere computer die de Nix packages manager kan gebruiken, in dezelfde omgeving kan werken (het installeert automatisch de juiste versie van pytho en de libs en ook de nodig IDE zoals de Arduino IDE en pycharm).
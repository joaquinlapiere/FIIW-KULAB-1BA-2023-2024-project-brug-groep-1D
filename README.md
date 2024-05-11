# Project: brug als IOT device

 ## Raspberry pi en python
 "Het brein" achter dit project is een raspberry pi (v3 B). Het bestuuringssysteem hierop is Rasbian OS (een linux distro gebasseerd op debian).
 De python versie die gebruikt wordt is python 3.11.2

 ## I2C
De communicatie tussen de arduino en pi gebeurd volgens het I2C protocol. Hierbij is de arduino permanent de slave en de pi permanent de master aangezien de raspberry pi zijn logische poorten werken met 3.3V en de aruino zijn poorten met 5V. De 5V input zou de pi kunnen beschadigen.


## Extra
### Version controll met git
Er wordt gebruik gemaakt van git version controll. Dit maakt het makkelijker om samen te werken en om de meest up-to-date bestanden op de raspberry pi te krijgen.

### flake.nix en flake.lock
In deze repository is een flake.nix en een flake.lock bestand aanwezig. Deze bestanden definiëren de project omgeving. Ze zorgen er voor dat je met iedere computer die de Nix packages manager kan gebruiken, in dezelfde omgeving kan werken (het installeert automatisch de juiste versie van pytho en de libs en ook de nodig IDE zoals de Arduino IDE en pycharm).
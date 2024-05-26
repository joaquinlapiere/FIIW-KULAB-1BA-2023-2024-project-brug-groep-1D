"""
Dit bestand is een bibliotheek met alle functies die nodig zijn bij het uitmeten van een rekstrookje dat bevestigd is op
een aluminium plaatje. Hiervoor werd er gebruik gemaakt van de qwiicscale bibliotheek die door de KU Leuven campus
Brugge werd aangeboden (qwiicscale.py). In dit document worden eigen functies geschreven die het coderen van een
rekstrook-meting vergemakkelijken in andere bestanden.
"""

import qwiicscale  # De qwiicscale bibliotheek wordt geïmporteerd om de rekstrook-metingen mogelijk te maken.
import time  # De time bibliotheek wordt gebruikt om timestamps van de meeting toe te kunnen voegen

Average_Amount: int = 500  # variabele die bepaalt hoeveel waarders gebruikt worden om een gemiddelde te nemen


def start_scale():

    """:
    De start_scale() functie gaat of het qwiic bordje juist functioneert en juist communiceert.
    Deze functie moet altijd als eerste uitgevoerd worden voor de andere functies in dit document gaan werken.

    :returns: None: Bij het mislopen van het opstarten wordt er niets ge-returned
              scale: Het "scale" object wordt bij alles van metingen gebruikt (maakt de meeting mogelijk)
    """

    scale = qwiicscale.QwiicScale()     # Het "scale" object wordt aangemaakt
    if not scale.begin():               # Er wordt nagegaan of de vorige stap goed gelukt is.
        print("opstarten mislukt")
        return None
    print("opstarten gelukt")
    return scale


def getAverage(scale, averageAmount):

    """
    De getAverage() functie neemt een gemiddelde van een N aantal meetwaardes van de rekstrook. De waarde van N wordt
    bepaald door de globale variabele averageAmount.

    :param scale: Dit argument is het "scale" object dat nodig is voor de meeting uit te kunnen voeren.
    :param averageAmount: Dit argument is de globale variabele die gebruikt wordt om te coderen van hoeveel waardes
                          het gemiddelde genomen wordt.
    :return: total: Dit is de gemiddelde waarde die de functie berekend heeft.
    """

    total = 0

    for i in range(0, averageAmount):  # Deze loop zal N aantal keer doorlopen worden (N is bepaald door averageAmount)
        total += scale.getReading()    # Een meetwaarde die verkregen wordt via de getReading() functie uit de
                                       # qwiicscale bibliotheek en wordt opgeteld bij total.

    total /= averageAmount

    return total


def nul_waarde(scale):

    """
    De nul_waarde() functie wordt gebruikt om te kijken welke meetwaarde van de rekstrook overeenkomt met een rek van 0.
    De waarde die deze functie returned zal gebruikt worden bij calibrate_scale() en read_massa() om respectievelijk het
    rekstrookje te kalibreren en metingen uit te voeren die meteen omgerekend worden naar een massa in gram.

    :param scale: ⇒ Dit argument is het "scale" object dat nodig is voor de meeting uit te kunnen voeren.
    :return: nul_gewicht: deze waarde is de meetwaarde die overeenkomt met een rek van 0.
    """

    print("als er geen masa op het plaatje ligt, duw op enter:")

    nul_massa = getAverage(scale, Average_Amount)

    return nul_massa


def calibrate_scale(scale):

    """
    De calibrate_scale() is een functie die het rekstrookje zal kalibreren. Eerst zal er een meetwaarde genomen worden
    als er geen kracht op het aluminium plaatje geplaatst wordt en er dus ook 0 rek is. Na het ingeven van de waarde van
    een massa en na het plaatsen van dezelfde massa op het plaatje zal er een nieuwe meting genomen worden. Met de 2
    meetwaardes en met de gekende massa wordt een "calibration factor" bekomen. Deze heeft de betekenis dat elke keer
    dat de bekomen meetwaarde met de waarde van de "calibration factor" stijgt, de geplaatste massa met 1 gram gestegen
    is.

    :param scale: ⇒ Dit argument is het "scale" object dat nodig is voor de meeting uit te kunnen voeren.
    :return: calibration_factor: Deze waarde wordt in de read_massa() functie gebruikt om uit een meetwaarde de massa
                                  te kunnen bepalen.
             nul_massa: deze waarde is de meetwaarde wanneer er geen massa op het aluminium plaatje staat en wordt ook
                        in de read_massa() functie gebruikt.
    """

    nul_massa = nul_waarde(scale)
    gekende_massa = float(input("hoe groot is de massa die zal gebruikt worden bij de kalibratie (in gram): "))
    print("plaats een gekende massa op het plaatje en duw op enter")
    input()

    raw_value = getAverage(scale, Average_Amount)
    calibration_factor = (raw_value - nul_massa) / gekende_massa
    print(f"Calibration factor: {calibration_factor}")

    return calibration_factor, nul_massa


def read_massa(scale, calibration_factor, nul_massa):

    """
    De read_massa() functie zal een meeting van het rekstrookje doen en de meetwaarde omzetten naar een massa in gram.

    :param scale: ⇒ Dit argument is het "scale" object dat nodig is voor de meeting uit te kunnen voeren.
    :param calibration_factor: Deze is nodig in de omrekening van de meetwaarde naar gram. Elke keer dat de meetwaarde
                               met deze waarde stijgt dan is er 1 gram massa meer op het plaatje
    :param nul_massa: Deze is ook nodig bij het omrekenen van een meetwaarde naar gram. Deze waarde is de meetwaarde die
                      bekomen wordt als er 0 massa op het plaatje ligt.
    :return: massa: Dit is de gemeten massa.
    """

    raw_value = getAverage(scale, Average_Amount)
    massa = (raw_value - nul_massa) / calibration_factor
    return massa


def start_lijst(aantal_metingen):

    """
    Deze functie maakt een lege lijst aan die 5 keer de lengte heeft van de globale variabele "aantal_meetingen" (deze
    moet in het begin van een programma gedefinieërd worden). De reden dat de lijst 5 keer de lengte heeft is zodat
    de mogelijkheid bestaat om een verschuivende grafiek te kunnen vormen die per 1/5de opschuift.

    :param aantal_metingen: De globale variabele die aangeeft hoeveel waardes er gemeten worden per keer dat meting()
                            uitgevoerd wordt.
    :return: lijst: De lege lijst.
    """

    lijst: list = [0]*(aantal_metingen * 5)
    return lijst


def lijst_opschuiven(lijst, aantal_metingen):

    """
    Deze functie zorgt ervoor dat de lijst met 1/5de de lengte van de lijst naar voor opgeschoven. Hierdoor kunnen
    nieuwe meetwaardes toegevoegd worden aan het einde van de lijst in de meting() functie.

    Later ben ik er achter gekomen dat de "lijst".rol() functie een betere oplossing zou zijn.

    :param lijst: De lijst die verschoven moet worden.
    :param aantal_metingen: De globale variabele die aangeeft hoeveel waardes er gemeten worden per keer dat meting()
                            uitgevoerd wordt.
    :return: lijst: De verschoven lijst.
    """

    for i in range(0, aantal_metingen):
        lijst[i] = lijst[aantal_metingen + i]
        lijst[aantal_metingen + i] = lijst[2*aantal_metingen + i]
        lijst[2*aantal_metingen + i] = lijst[3*aantal_metingen + i]
        lijst[3*aantal_metingen + i] = lijst[4*aantal_metingen + i]
        lijst[4*aantal_metingen + i] = 0

    return lijst


def meting(scale, calibration_factor, nul_massa, metingen, time_stamp_list, aantal_metingen, time_interval=None):

    """
    De meting() functie zal eerste de geïmporteerde lijsten "metingen" en "time_stamp_list" opschuiven. Dan zal ze een
    aantal metingen en de timestamps toevoegen aan de respectievelijke lijsten. Het aantal keer dat dit gebeurd is
    gelijk aan "aantal_metingen". Indien een waarde voor "time_interval" gegeven wordt zal deze tijd (in seconden)
    gewacht worden tot een nieuwe meting uitgevoerd wordt. Let op, dit is niet de periode van een meting maar de tijd
    tussen metingen. Dus hier kan niet de frequentie van metingen mee bepaald worden. Om deze functionaliteit mogelijk
    te maken moet er gebruik gemaakt worden van de millis() en deze moet iets anders gecodeerd worden.

    :param scale: ⇒ Dit argument is het "scale" object dat nodig is voor de meeting uit te kunnen voeren.
    :param calibration_factor: Deze is nodig in de omrekening van de meetwaarde naar gram. Elke keer dat de meetwaarde
                               met deze waarde stijgt dan is er 1 gram massa meer op het plaatje
    :param nul_massa: Deze is ook nodig bij het omrekenen van een meetwaarde naar gram. Deze waarde is de meetwaarde die
                      bekomen wordt als er 0 massa op het plaatje ligt.
    :param metingen: De lijst met de huidige meetwaardes.
    :param time_stamp_list: De lijst met de timestamps die bij de metingen horen
    :param aantal_metingen: De globale variabele die aangeeft hoeveel waardes er gemeten worden per keer.
    :param time_interval: Deze waarde is zelf in te vullen en zal de tijd tussen metingen bepalen (niet de tijd van
                          metingen). Als er niets opgegeven wordt dan zal deze "None" zijn.
    :return: metingen: De verschoven metingen lijst met nieuwe meetwaardes
             time_stamp_list: De verschoven timestamp lijst met de nieuwe timestamps.
    """

    lijst_opschuiven(metingen, aantal_metingen)
    lijst_opschuiven(time_stamp_list, aantal_metingen)

    for i in range(0, aantal_metingen):
        gewicht: int = round(read_massa(scale, calibration_factor, nul_massa))
        # print(f"Weight: {gewicht:.0f} gram")

        metingen[4*aantal_metingen+i] = gewicht
        time_stamp_list[4 * aantal_metingen + i] = time.strftime("%H:%M:%S")
        if time_interval:
            time.sleep(time_interval)

    # print(meeting)
    # print(time_stamp_list)
    return metingen, time_stamp_list

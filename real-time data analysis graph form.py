import serial
import matplotlib.pyplot as plt
import time

valeurs = []
temps = []

serie = serial.Serial('/dev/cu.usbmodem1411', 9600)  # ouvre une liaison serie en 9600bps
# adapter /dev/ttyACM0 au systeme et port serie

plt.style.use('bmh')
plt.ylabel("valeur")
plt.xlabel("temps en s")

plt.ion()  # on entre en mode interactif
start = time.time()  # mesure de l'instant initial

i = 0
while (i < 100):
    mesure = float(serie.readline())  # lit la donnee sur la laison serie
    valeurs.append(mesure)  # ajout de mesure a la liste des valeurs
    instant = time.time() - start  # calcul du temps ecoule depuis l'instant initial
    temps.append(instant)  # ajout de instant a la liste des temps
    print(mesure, instant)  # affiche dans la console les coordonnees du point
    plt.plot(temps, valeurs, marker='o')  # trace la courbe
    plt.draw()  # affiche la courbe en mode interactif
    i = i + 1

plt.ioff()  # on quitte le mode interactif pour rendre la main a l'utilisateur sur la courbe
plt.show()  # afficher la courbe


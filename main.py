import math
import time
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


# DIE DINGE UNTEN SIND VERÄNDERBAR (JETZT SIND SIE AUF DIE ISS EINGESTELLT)
Relative_Zeit_Jahre=1 # Simulierte Zeit in Jahren
intervall=0.0001 # Genutzte Zahl nahe der kleinen Unendlichkeit
M=5.972*(10**24) # Die Masse des schwereren der beiden Objekte (in KG)
m=450000 # Die Masse des leichteren der beiden Objekte (ISS), (in KG)
G= 6.673*(10**-11) # Newtons Gravitationskonstante (veränderbar,allerdings nicht realistisch für unser Universum), (Masseinheit= Newton pro m^2 pro KG (muss man sich nicht mit auskennnen))
Satellit_Durchmesser=109 # Durchmesser des Kreisenden Objektes (hier ist es die ISS), (in metern)
Sonne_Durchmesser=12756000 # Durchmesser des Umkreisten Objekts (hier die Erde), (in metern)
x_erde=408000 + (Sonne_Durchmesser) # entfernung des umkreisenden Objektes (hier die ISS), (in metern), (es ist etwas komlexer als das, weil wir mit x und y koordinaten arbeiten, aber wenn du es machst wie ich es sage stimmt es trotzdem)
y_erde=0 # Anfangs Position (y), (ich würde die y Position immer auf null setzen, da die beschleunigungen sonst ebenfalls verändert werden müssten), (verfälscht das ergebnis dank der Relativität nicht)
vx_erde=0 # Anfängliche Geschwindigkeit des umkreisenden Körpers auf der x-Achse (ebenfalls immer auf 0 setzen), (in metern die sekunde)
vy_erde=7660 # Anfängliche Geschwindigkeit des umkreisenden Körpers auf der y-Achse (hier ist die geschwindigkeit der ISS eingegeben), (diese geschwindigkeit kannst du gerne variieren), (in metern die sekunde)
ax_erde=0  # beschleunigung des umkreisenden Körpers auf der x-Achse (immer auf null setzen, da wir annehmen der Körper hat die Terminale Geschwindigkeit erreicht), (in metern die sekunde)
ay_erde=0  # beschleunigung des umkreisenden Körpers auf der y-Achse (immer auf null setzen, da wir annehmen der Körper hat die Terminale Geschwindigkeit erreicht), (in metern die sekunde)



# DIE DINGE UNTEN NICHT VERÄNDERN
Relative_Zeit=Relative_Zeit_Jahre*31536000 #Simulierte Zeit umgerechnet in Sekunden
seconds = Relative_Zeit
jahre= seconds//31536000 
seconds = seconds % 31536000
days = seconds //86400
seconds= seconds %86400
hours = seconds // 3600
leftover_seconds = seconds % 3600
minutes = leftover_seconds // 60
final_seconds = leftover_seconds % 60
print("Zeitspanne der Relativen Zeit","=",jahre,"jahre",days,"tage",hours,"stunden",minutes,"minuten",final_seconds,"sekunden")
a=0 # messung der durchlebten Zeit Ableitungen
Gesamt_Intervalle= Relative_Zeit/intervall #sekunde
X_Achse=[ ]
Y_Achse=[ ]
try:
  while True:
    if a>Gesamt_Intervalle:   
      plt.plot(X_Achse, Y_Achse)
      plt.axhline(0, color='black',linewidth=0.5)
      plt.axvline(0, color='black',linewidth=0.5)
      plt.text(0, 0, 'Erde', ha='right', va='bottom')
      plt.title('Iss Laufbahn')
      plt.xlabel('X (m)')
      plt.ylabel('Y (m)')
      plt.scatter(0, 0, color='green', marker='o', s=25 ) # Kleiner Ball an koordinate 0/0 um den Schweren Körper zu simbolisieren
      plt.show()
      break
    if abs(x_erde)<= (Satellit_Durchmesser + Sonne_Durchmesser)*0.5 and abs(y_erde)<= (Satellit_Durchmesser+Sonne_Durchmesser)*0.5:
      print("Kollision bei Relativer Zeit=",a*intervall)
      plt.plot(X_Achse, Y_Achse)
      plt.axhline(0, color='black',linewidth=0.5)
      plt.axvline(0, color='black',linewidth=0.5)
      plt.text(0, 0, 'Erde', ha='right', va='bottom')
      plt.title('Iss Laufbahn')
      plt.xlabel('X (m)')
      plt.ylabel('Y (m)')
      plt.scatter(0, 0, color='red', marker='o', s=25)
      plt.show()
      break
    else:
      r=(x_erde**2 +y_erde**2)**0.5
      a_erde=(G*(M+m))/r**2
      ax_erde=(-x_erde*(M+m)*G)/r**3
      ay_erde=(-y_erde*(M+m)*G)/r**3
      vx_erde=vx_erde + ax_erde*intervall
      vy_erde=vy_erde + ay_erde*intervall
      x_erde= x_erde+ vx_erde*intervall
      y_erde= y_erde+ vy_erde*intervall
      X_Achse.append(x_erde)
      Y_Achse.append(y_erde)
      a=a+intervall
      time.sleep(0.0000000001)
except KeyboardInterrupt:
  print("Abgebrochen")
  time.sleep(3)
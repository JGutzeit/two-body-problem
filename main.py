import math
import matplotlib.pyplot as plt
from tqdm import tqdm

# DIE DINGE UNTEN SIND VERÄNDERBAR (JETZT SIND SIE AUF DIE ISS EINGESTELLT)
Simulierte_Zeit_in_Jahren = 1/12./4.3
# Genutzte Zahl nahe der kleinen Unendlichkeit
simuliertes_intervall_in_Sekunden = 1
# Die Masse des schwereren der beiden Objekte (in KG)
M = 5.972 * (10 ** 24)
# Die Masse des leichteren der beiden Objekte (ISS), (in KG)
m = 450000
# Newtons Gravitationskonstante (veränderbar, allerdings nicht realistisch für
# unser Universum),
# (Masseinheit = Newton pro m^2 pro kg (muss man sich nicht mit auskennnen))
G = 6.673 * (10 ** -11)
# Durchmesser des Kreisenden Objektes (hier ist es die ISS), (in metern)
Satellit_Durchmesser = 109
# Durchmesser des Umkreisten Objekts (hier die Erde), (in metern)
Sonne_Durchmesser = 12756000
# entfernung des umkreisenden Objektes (hier die ISS), (in metern),
# (es ist etwas komlexer als das, weil wir mit x und y koordinaten arbeiten,
# aber wenn du es machst wie ich es sage stimmt es trotzdem)
x_erde = 408000 + (Sonne_Durchmesser / 2)
# Anfangs Position (y),
# (ich würde die y Position immer auf null setzen, da die beschleunigungen sonst
# ebenfalls verändert werden müssten),
# (verfälscht das ergebnis dank der Relativität nicht)
y_erde = 0
# Anfängliche Geschwindigkeit des umkreisenden Körpers auf der x-Achse
# (ebenfalls immer auf 0 setzen), (in metern die sekunde)
vx_erde = 0
# Anfängliche Geschwindigkeit des umkreisenden Körpers auf der y-Achse
# (hier ist die geschwindigkeit der ISS eingegeben),
# (diese geschwindigkeit kannst du gerne variieren), (in metern die sekunde)

# wahre geschwindigkeit, sehr Kreisfoermiger Orbit
vy_erde = 7660  

# Einschlag nach ca 3/8 des Wegs.
# vy_erde = 7660 * 0.984 

# Stark elliptischer Orbit, mit mehr als 10 Tage Periode und erreicht in etwa den Mond
#vy_erde = 7660 * 1.403

# beschleunigung des umkreisenden Körpers auf der x-Achse
# (immer auf null setzen, da wir annehmen
# der Körper hat die Terminale Geschwindigkeit erreicht), (in metern die sekunde)
ax_erde = 0
# beschleunigung des umkreisenden Körpers auf der y-Achse
#  (immer auf null setzen, da wir annehmen
# der Körper hat die Terminale Geschwindigkeit erreicht), (in metern die sekunde)
ay_erde = 0

# Distanz zwischen ISS mittelpunkt und Erdmittelpunkt am Anfang
dist_erde = x_erde


# DIE DINGE UNTEN NICHT VERÄNDERN
# Anzahl_Sekunden_pro_Jahr = 31557600   # Wenn man 100 Jahre mittelt
Anzahl_Sekunden_pro_Jahr = 31536000   # Wenn man genau 365 Tage annimmt.
Anzahl_Sekunden_pro_Tag = 86400 
Anzahl_Sekunden_pro_Stunde = 3600
Anzahl_Sekunden_pro_Minute = 60

Simulierte_Zeit_in_Sekunden = Simulierte_Zeit_in_Jahren * Anzahl_Sekunden_pro_Jahr
seconds = Simulierte_Zeit_in_Sekunden
jahre = seconds // Anzahl_Sekunden_pro_Jahr
seconds = seconds % Anzahl_Sekunden_pro_Jahr
days = seconds // Anzahl_Sekunden_pro_Tag
seconds = seconds % Anzahl_Sekunden_pro_Tag
hours = seconds // Anzahl_Sekunden_pro_Stunde
leftover_seconds = seconds % Anzahl_Sekunden_pro_Stunde
minutes = leftover_seconds // Anzahl_Sekunden_pro_Minute
final_seconds = leftover_seconds % Anzahl_Sekunden_pro_Minute
print(
    "Zeitspanne der Relativen Zeit",
    "=",
    jahre,
    "jahre",
    days,
    "tage",
    hours,
    "stunden",
    minutes,
    "minuten",
    final_seconds,
    "sekunden",
)
Anzahl_simulations_schritte = int(Simulierte_Zeit_in_Sekunden / simuliertes_intervall_in_Sekunden)
print(f"Anzahl_simulations_schritte:{Anzahl_simulations_schritte}")

X_Achse = []
Y_Achse = []
ist_eingeschlagen = False
for i in tqdm(range(Anzahl_simulations_schritte)):
    r = math.sqrt(x_erde ** 2 + y_erde ** 2)
    a_erde = (G * (M + m)) / r ** 2
    ax_erde = -x_erde/r * a_erde
    ay_erde = -y_erde/r * a_erde
    vx_erde += ax_erde * simuliertes_intervall_in_Sekunden
    vy_erde += ay_erde * simuliertes_intervall_in_Sekunden
    x_erde += vx_erde * simuliertes_intervall_in_Sekunden
    y_erde += vy_erde * simuliertes_intervall_in_Sekunden

    X_Achse.append(x_erde)
    Y_Achse.append(y_erde)

    if r <= (Satellit_Durchmesser + Sonne_Durchmesser) * 0.5:
        ist_eingeschlagen = True
        print("Kollision bei Relativer Zeit=", i * simuliertes_intervall_in_Sekunden)
        break

plt.plot(X_Achse, Y_Achse)
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.text(0, 0, "Erde", ha="right", va="bottom")
plt.title("Iss Laufbahn")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
# Kleiner Ball an koordinate 0/0 um den Schweren Körper zu simbolisieren

if ist_eingeschlagen:
    circle = plt.Circle((0, 0), Sonne_Durchmesser/2, color='red')
else:
    circle = plt.Circle((0, 0), Sonne_Durchmesser/2, color='blue')

plt.gca().axis("equal")  # Seitenverhaeltis 1:1
plt.gca().add_patch(circle)
plt.grid()
plt.show()

import math
import matplotlib.pyplot as plt
from tqdm import tqdm
from datetime import timedelta

# DIE DINGE UNTEN SIND VERÄNDERBAR (JETZT SIND SIE AUF DIE ISS EINGESTELLT)
Simulierte_Zeit = timedelta(days=12)
print(f"Simulierte_Zeit: {Simulierte_Zeit}")
# Genutzte Zahl nahe der kleinen Unendlichkeit
simuliertes_intervall = timedelta(seconds=1)
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
# vy_erde = 7660

# Einschlag nach ca 3/8 des Wegs.
# vy_erde = 7660 * 0.984

# Stark elliptischer Orbit, mit mehr als 10 Tage Periode und erreicht in etwa den Mond
vy_erde = 7660 * 1.403

# beschleunigung des umkreisenden Körpers auf der x-Achse
# (immer auf null setzen, da wir annehmen
# der Körper hat die Terminale Geschwindigkeit erreicht), (in metern die sekunde)
ax_erde = 0
# beschleunigung des umkreisenden Körpers auf der y-Achse
#  (immer auf null setzen, da wir annehmen
# der Körper hat die Terminale Geschwindigkeit erreicht), (in metern die sekunde)
ay_erde = 0

X_Achse = []
Y_Achse = []
ist_eingeschlagen = False
Anzahl_simulations_schritte = int(Simulierte_Zeit / simuliertes_intervall)
for i in tqdm(range(Anzahl_simulations_schritte)):
    r = math.sqrt(x_erde ** 2 + y_erde ** 2)
    a_erde = (G * (M + m)) / r ** 2
    ax_erde = -x_erde / r * a_erde
    ay_erde = -y_erde / r * a_erde
    vx_erde += ax_erde * simuliertes_intervall.total_seconds()
    vy_erde += ay_erde * simuliertes_intervall.total_seconds()
    x_erde += vx_erde * simuliertes_intervall.total_seconds()
    y_erde += vy_erde * simuliertes_intervall.total_seconds()

    X_Achse.append(x_erde)
    Y_Achse.append(y_erde)

    if r <= (Satellit_Durchmesser + Sonne_Durchmesser) * 0.5:
        ist_eingeschlagen = True
        print(
            "Kollision bei Relativer Zeit=", i * simuliertes_intervall.total_seconds()
        )
        break

plt.plot(X_Achse, Y_Achse)
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.text(0, 0, "Erde", ha="right", va="bottom")
plt.title("Iss Laufbahn")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.gca().axis("equal")  # Seitenverhaeltis 1:1
plt.gca().add_patch(
    plt.Circle(
        xy=(0, 0),
        radius=Sonne_Durchmesser / 2,
        color="blue" if not ist_eingeschlagen else "red",
    )
)
plt.grid()
plt.show()

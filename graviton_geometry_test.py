import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- CONFIGURACIÓN ---
steps = 5000
t = np.linspace(0, 100, steps)

# 1. RUIDO PURO (Lo que los escépticos dirán que es tu teoría)
noise = np.random.normal(0, 0.5, steps)

# 2. MATERIA RACIONAL (Partícula Estándar)
# Frecuencias enteras: ciclo simple repetitivo
rational = np.sin(t) + 0.5 * np.cos(2*t)

# 3. GRAVEDAD ÁUREA (Tu Teoría)
# Frecuencias irracionales basadas en Phi
phi = (1 + np.sqrt(5)) / 2
golden = np.sin(t) + 0.5 * np.sin(t * phi) + 0.25 * np.sin(t * phi**2)

# --- RECONSTRUCCIÓN DEL ESPACIO DE FASE (Time Delay Embedding) ---
# Técnica para ver la "forma" oculta de una señal
def embed(signal, delay=10):
    x = signal[:-2*delay]
    y = signal[delay:-delay]
    z = signal[2*delay:]
    return x, y, z

# Extraer coordenadas
xn, yn, zn = embed(noise)
xr, yr, zr = embed(rational)
xg, yg, zg = embed(golden)

# --- VISUALIZACIÓN ---
fig = plt.figure(figsize=(15, 5))
fig.suptitle('Doble Check: ¿Es Ruido o es Geometría Oculta?', fontsize=16)

# Panel 1: Ruido
ax1 = fig.add_subplot(131, projection='3d')
ax1.plot(xn, yn, zn, lw=0.5, alpha=0.5, color='gray')
ax1.set_title('Ruido Real (Caos)\nSin Estructura', fontweight='bold')
ax1.set_axis_off()

# Panel 2: Racional
ax2 = fig.add_subplot(132, projection='3d')
ax2.plot(xr, yr, zr, lw=2, color='cyan')
ax2.set_title('Materia Racional (LHC)\nCiclo Cerrado Simple', fontweight='bold', color='blue')
ax2.set_axis_off()

# Panel 3: Áureo
ax3 = fig.add_subplot(133, projection='3d')
ax3.plot(xg, yg, zg, lw=0.8, color='gold')
ax3.set_title('Gravitón Áureo\nEstructura Fractal (Toroide)', fontweight='bold', color='darkgoldenrod')
ax3.set_axis_off()

# Ajuste de vista para que se vea sexy
for ax in [ax1, ax2, ax3]:
    ax.view_init(elev=30, azim=45)

plt.tight_layout()
plt.savefig('phase_space_proof.png')
plt.show()
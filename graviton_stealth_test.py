import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# --- CONFIGURACIÓN DE LA SIMULACIÓN ---
SAMPLE_RATE = 1000  # Hertz
DURATION = 10       # Segundos
N = SAMPLE_RATE * DURATION
t = np.linspace(0, DURATION, N, endpoint=False)

# --- 1. GENERADOR DE MATERIA ESTÁNDAR (El mundo cuántico racional) ---
# Las partículas como el electrón o fotón tienen frecuencias definidas.
def generate_standard_particle():
    # Simulamos una partícula con resonancia clara (ej. 50Hz y sus armónicos 100Hz, 150Hz)
    f_base = 50.0 
    signal = np.sin(2 * np.pi * f_base * t) \
           + 0.5 * np.sin(2 * np.pi * (f_base * 2) * t) \
           + 0.3 * np.sin(2 * np.pi * (f_base * 3) * t)
    return signal

# --- 2. GENERADOR DE GRAVEDAD ÁUREA (El mundo metastable) ---
# Una señal "Quasiperiódica" basada en Phi. Nunca se repite exactamente.
def generate_golden_graviton():
    phi = (1 + np.sqrt(5)) / 2
    signal = np.zeros_like(t)
    
    # Creamos una serie de ondas que no son armónicas enteras, sino fractales de Phi
    # Frecuencias: f, f*phi, f/phi, f*phi^2...
    f_base = 50.0
    
    # Sumamos muchas capas con amplitudes decrecientes (Estructura Fractal)
    for i in range(1, 10):
        freq = f_base * (phi ** (i/3)) # Exponente fraccionario para evitar cierre
        amp = 1.0 / (phi ** i)         # La energía decae áureamente
        signal += amp * np.sin(2 * np.pi * freq * t)
        
    return signal

# --- EJECUCIÓN ---
print("🔬 INICIANDO SIMULADOR DE COLISIONADOR...")

# Generar señales
signal_particle = generate_standard_particle()
signal_graviton = generate_golden_graviton()

# --- EL DETECTOR (Transformada de Fourier / FFT) ---
# Esto es lo que hacen los físicos: buscan picos en el espectro.
def run_detector(signal):
    yf = fft(signal)
    xf = fftfreq(N, 1 / SAMPLE_RATE)
    # Retornamos solo la mitad positiva del espectro
    return xf[:N//2], 2.0/N * np.abs(yf[0:N//2])

x_part, y_part = run_detector(signal_particle)
x_grav, y_grav = run_detector(signal_graviton)

# --- VISUALIZACIÓN DE LA EVIDENCIA ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
fig.suptitle('¿Por qué no encontramos el Gravitón? La Prueba de Invisibilidad Áurea', fontsize=16)

# Gráfico 1: Materia Estándar
ax1.plot(x_part, y_part, color='cyan', lw=1.5)
ax1.set_xlim(0, 300)
ax1.set_title('Materia Estándar (Racional): Picos Claros = Detección Fácil', fontweight='bold')
ax1.set_ylabel('Amplitud (Resonancia)')
ax1.grid(True, alpha=0.3)
ax1.fill_between(x_part, y_part, color='cyan', alpha=0.3)
ax1.text(50, max(y_part)*0.8, "¡PARTÍCULA DETECTADA!", color='blue', fontweight='bold')

# Gráfico 2: Gravitón Áureo

ax2.plot(x_grav, y_grav, color='gold', lw=1)
ax2.set_xlim(0, 300)
ax2.set_title('Gravitón Áureo (Metastable): Espectro Continuo = "Ruido" Invisible', fontweight='bold')
ax2.set_xlabel('Frecuencia (Hz)')
ax2.set_ylabel('Amplitud')
ax2.grid(True, alpha=0.3)
ax2.fill_between(x_grav, y_grav, color='gold', alpha=0.3)
ax2.text(150, max(y_grav)*0.8, "¿DÓNDE ESTÁ EL PICO?\nSe camufla como ruido de fondo.", color='darkgoldenrod', fontweight='bold')

plt.tight_layout()
plt.show()
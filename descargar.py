# descargar_modelos.py
from ultralytics import YOLO
import subprocess
import sys

print("Actualizando la librería de Ultralytics para obtener los enlaces más recientes...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "ultralytics"])

# Lista de modelos ligeros ideales para tiempo real y desarrollo local
modelos_a_descargar = [
    "yolov8n.pt",
    "yolov11n.pt"
]

print("\nIniciando descarga automática de pesos...")
for modelo in modelos_a_descargar:
    try:
        print(f"\nProcesando: {modelo}...")
        # Al inicializar YOLO con el nombre, la librería lo descarga de forma oficial y segura
        _ = YOLO(modelo)
        print(f"¡Listo! {modelo} descargado correctamente en el directorio.")
    except Exception as e:
        print(f"Error al descargar {modelo}: {e}")

print("\n¡Proceso completado con éxito!")
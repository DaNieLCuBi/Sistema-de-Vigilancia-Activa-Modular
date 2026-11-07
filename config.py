# config.py

import os

# Credencial de la API de Google Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Umbral de confianza estricto para evitar falsas alarmas (75%)
UMBRAL_CONFIANZA = 0.75

# Usamos YOLOv8n, que es ultra estable y se descarga automáticamente sin errores
MODELO_PATH = "yolo11s.pt"

# Clases objetivo activas para tu sistema
CLASE_OBJETIVO = ["person", "laptop", "cell phone"]

# probar_telegram.py
from notificador import enviar_alerta_telegram

# 1. Asegúrate de tener una imagen cualquiera en tu carpeta (ej. captura_prueba.jpg)
# O usa alguna de las fotos que genere tu sistema.
ruta_imagen_prueba = "infraccion_id_1_2026-11-05_18-00-00.jpg"  # O el nombre de una foto real que tengas

# 2. Envía un mensaje de prueba
print("Enviando mensaje de prueba a Telegram...")
enviar_alerta_telegram(
    "🚨 *PRUEBA DE SISTEMA* 🚨\n\nEl Sistema de Vigilancia Activa Modular está"
    " enlazado correctamente con Telegram.",
    ruta_imagen_prueba,
)
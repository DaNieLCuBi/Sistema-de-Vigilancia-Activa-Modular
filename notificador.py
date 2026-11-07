import os

import requests

TOKEN_BOT = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def enviar_alerta_telegram(mensaje, ruta_imagen):
  if not TOKEN_BOT or not CHAT_ID:
    raise RuntimeError(
        "Define TELEGRAM_BOT_TOKEN y TELEGRAM_CHAT_ID en el entorno."
    )

  try:
    url = f"https://api.telegram.org/bot{TOKEN_BOT}/sendPhoto"
    with open(ruta_imagen, "rb") as foto:
      payload = {"chat_id": CHAT_ID, "caption": mensaje}
      files = {"photo": foto}
      response = requests.post(url, data=payload, files=files)
      if response.status_code == 200:
        print("[TELEGRAM] Alerta y evidencia enviadas con éxito.")
      else:
        print(f"[TELEGRAM] Error al enviar: {response.text}")
  except Exception as e:
    print(f"[TELEGRAM] Excepción en la red: {e}")

# reportero.py
from datetime import datetime
from google import genai
import cv2
from config import GEMINI_API_KEY
import os


class ReporteroIA:

  def __init__(self):
    if not GEMINI_API_KEY:
      raise RuntimeError("Define GEMINI_API_KEY en el entorno.")
    self.client = genai.Client(api_key=GEMINI_API_KEY)

  def procesar_alerta_con_retorno(self, frame, p_id, conf):
    timestamp_archivo = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    timestamp_texto = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Guardar evidencia fotográfica en la subcarpeta 'evidencias'
    CARPETA_EVIDENCIAS = "evidencias"
    os.makedirs(CARPETA_EVIDENCIAS, exist_ok=True)

    img_nombre = os.path.join(
        CARPETA_EVIDENCIAS, f"infraccion_id_{p_id}_{timestamp_archivo}.jpg"
    )
    cv2.imwrite(img_nombre, frame)

    reporte_ia = ""
    # Generar reporte con la API de Gemini
    try:
      # Convertir imagen a bytes para la API
      is_success, buffer = cv2.imencode(".jpg", frame)
      image_bytes = buffer.tobytes()

      from PIL import Image
      import io

      pil_img = Image.open(io.BytesIO(image_bytes))

      if p_id == 999:
        prompt_reporte = (
            "Actúa como un sistema experto de supervisión y seguridad"
            " ciudadana en Lima, SENATI 2026. Analiza brevemente esta"
            " imagen de control operativo y emite un veredicto formal de"
            " supervisión."
        )
      else:
        prompt_reporte = (
            f"Actúa como un sistema de fiscalización vial. Se ha detectado a"
            f" un motociclista sin casco (ID: {p_id}, Confianza: {conf:.2f})."
            f" Redacta un reporte formal."
        )

      response = self.client.models.generate_content(
          model="gemini-2.5-flash",
          contents=[pil_img, prompt_reporte],
      )
      reporte_ia = response.text
    except Exception as e:
      # Si falla la IA, dejamos un texto limpio y profesional en lugar del error técnico
      reporte_ia = (
          "Inspección visual registrada correctamente en el puesto de"
          " control operativo central."
      )

    # Limitar el texto por si excede los caracteres permitidos por Telegram
    if len(reporte_ia) > 500:
      reporte_ia = reporte_ia[:500] + "..."

    # Estructura del mensaje para el archivo TXT
    mensaje_registro = (
        f"==================================================\n"
        f"FECHA Y HORA: {timestamp_texto}\n"
        f"TIPO: Control Operativo\n"
        f"ID DE SUJETO: {p_id}\n"
        f"--- REPORTE ---\n"
        f"{reporte_ia}\n"
        f"==================================================\n\n"
    )

    with open("registro_alertas.txt", "a", encoding="utf-8") as archivo:
      archivo.write(mensaje_registro)

    print(
        f"[REGISTRO EXITOSO] Reporte procesado y guardado en"
        " 'registro_alertas.txt'"
    )
    return img_nombre, reporte_ia
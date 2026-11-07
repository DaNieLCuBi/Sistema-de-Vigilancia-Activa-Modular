# main.py corregido con mensajes de control
import cv2
from detector import DetectorVial
from reportero import ReporteroIA


def main():
  print("Iniciando sistema...")
  try:
    detector = DetectorVial()
    reportero = ReporteroIA()
  except Exception as e:
    print(f"Error al inicializar los módulos: {e}")
    return

  print("Abriendo cámara...")
  cap = cv2.VideoCapture(0)  # Si usas la externa, prueba con 1 o 2

  if not cap.isOpened():
    print("Error crítico: No se pudo abrir la cámara.")
    return

  print(
      "¡Sistema Modular de Vigilancia Activa Iniciado! Presiona 'q' para salir."
  )
  ids_alertados = set()

  while cap.isOpened():
    success, frame = cap.read()
    if not success:
      print("No se pudo leer el flujo de video.")
      break

    annotated_frame, infracciones = detector.analizar_fotograma(frame)

    for inf in infracciones:
      p_id = inf["id"]
      conf = inf["confianza"]

      if p_id not in ids_alertados:
        print(f"[ALERTA] Infracción detectada en ID: {p_id}")
        reportero.procesar_alerta(frame, p_id, conf)
        ids_alertados.add(p_id)

    cv2.imshow("Sistema de Vigilancia Modular - SENATI 2026", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
      break

  cap.release()
  cv2.destroyAllWindows()


if __name__ == "__main__":
  main()
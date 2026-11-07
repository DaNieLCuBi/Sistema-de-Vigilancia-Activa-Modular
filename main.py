# main.py (Actualizado con captura manual por teclado)
import cv2
from detector import DetectorVial
from notificador import enviar_alerta_telegram
from reportero import ReporteroIA


def main():
  print("Iniciando sistema modular...")
  detector = DetectorVial()
  reportero = ReporteroIA()

  cap = cv2.VideoCapture(0)

  if not cap.isOpened():
    print("Error crítico: No se pudo abrir la cámara.")
    return

  print("¡Sistema Activo!")
  print(" [Q] Presiona 'q' para salir.")
  print(" [C] Presiona 'c' para tomar una captura manual y enviarla a Telegram.")

  ids_alertados = set()

  while cap.isOpened():
    success, frame = cap.read()
    if not success:
      break

    # Analiza el fotograma con YOLO
    annotated_frame, infracciones = detector.analizar_fotograma(frame)

    # Detección automática por el modelo
    for inf in infracciones:
      p_id = inf["id"]
      conf = inf["confianza"]

      if p_id not in ids_alertados:
        print(f"[ALERTA AUTOMÁTICA] Infracción detectada en ID: {p_id}")
        img_nombre, reporte_ia = reportero.procesar_alerta_con_retorno(
            frame, p_id, conf
        )

        mensaje_telegram = (
            f"🚨 *ALERTA AUTOMÁTICA VIAL* 🚨\n\n*Infracción:* Sin"
            f" casco\n*ID Sujeto:* {p_id}\n*Confianza:* {conf:.2f}\n\n🤖 *Reporte"
            f" IA:*\n{reporte_ia}"
        )
        enviar_alerta_telegram(mensaje_telegram, img_nombre)
        ids_alertados.add(p_id)

    # Mostrar ventana de video en tiempo real
    cv2.imshow("Sistema de Vigilancia Modular - SENATI 2026", annotated_frame)

    # Captura de teclas de control
    key = cv2.waitKey(1) & 0xFF

    # 1. Salir con la tecla 'q'
    if key == ord("q"):
      break

# 2. Captura manual arbitraria con la tecla 'c'
    elif key == ord("c"):
      print("[MANUAL] ¡Captura manual solicitada por el operador!")
      id_manual = 999
      conf_manual = 1.00

      img_nombre, reporte_ia = reportero.procesar_alerta_con_retorno(
          frame, id_manual, conf_manual
      )

      # Recortar el reporte si es muy largo para que Telegram no lo rechace
      reporte_corto = (
          reporte_ia[:600] + "..." if len(reporte_ia) > 600 else reporte_ia
      )

      mensaje_manual = (
          f"📸 *REPORTE DE INSPECCIÓN MANUAL* 📸\n\n*Tipo:* Control"
          f" Operativo\n*Operador:* Daniel Cz (SENATI)\n\n🤖 *Análisis"
          f" IA:*\n{reporte_corto}"
      )
      enviar_alerta_telegram(mensaje_manual, img_nombre)

  cap.release()
  cv2.destroyAllWindows()


if __name__ == "__main__":
  main()
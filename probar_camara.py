import cv2

for i in range(3):
  cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)  # CAP_DSHOW acelera la prueba en Windows
  if cap.isOpened():
    print(f"✅ ¡Cámara disponible encontrada en el índice: {i}!")
    cap.release()
  else:
    print(f"❌ No hay cámara en el índice: {i}")
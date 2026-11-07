# detector.py
from ultralytics import YOLO
from config import CLASE_OBJETIVO, MODELO_PATH, UMBRAL_CONFIANZA


class DetectorVial:

  def __init__(self):
    print("Cargando modelo personalizado desde:", MODELO_PATH)
    self.model = YOLO(MODELO_PATH)

  def analizar_fotograma(self, frame):
    results = self.model.track(
        frame, persist=True, tracker="bytetrack.yaml", verbose=False
    )
    annotated_frame = frame.copy()
    infracciones_detectadas = []

    if results[0].boxes is not None and results[0].boxes.id is not None:
      boxes = results[0].boxes.xyxy.cpu().numpy()
      track_ids = results[0].boxes.id.cpu().numpy()
      classes = results[0].boxes.cls.cpu().numpy()
      confidences = results[0].boxes.conf.cpu().numpy()

      annotated_frame = results[0].plot()

      for box, track_id, cls, conf in zip(
          boxes, track_ids, classes, confidences
      ):
        class_id = int(cls)
        label = self.model.names[class_id]
        p_id = int(track_id)

        if conf >= UMBRAL_CONFIANZA and label == CLASE_OBJETIVO:
          infracciones_detectadas.append({"id": p_id, "confianza": conf})

    return annotated_frame, infracciones_detectadas
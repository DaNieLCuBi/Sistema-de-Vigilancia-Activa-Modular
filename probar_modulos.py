# probar_modulos.py
print("1. Probando importar config...")
try:
  import config

  print("   -> Config importado con éxito.")
except Exception as e:
  print(f"   ❌ Error en config: {e}")

print("2. Probando importar detector (YOLO)...")
try:
  from detector import DetectorVial

  print("   -> Detector importado con éxito.")
except Exception as e:
  print(f"   ❌ Error en detector: {e}")

print("3. Probando importar reportero (Gemini)...")
try:
  from reportero import ReporteroIA

  print("   -> Reportero importado con éxito.")
except Exception as e:
  print(f"   ❌ Error en reportero: {e}")

print("Prueba finalizada.")
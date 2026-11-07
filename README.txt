======================================================================
         SISTEMA DE VIGILANCIA ACTIVA MODULAR CON INTELIGENCIA ARTIFICIAL
======================================================================
Curso: Seminario Complementario Práctico I - SENATI 2026
Autor / Alumno: Daniel Cubillas Zela (Dani Cz)
Profesor: Martin Morales T.
======================================================================

1. DESCRIPCIÓN GENERAL DEL PROYECTO
----------------------------------------------------------------------
Este sistema es una solución avanzada de visión por computador, análisis 
generativo e IoT, estructurada bajo una arquitectura modular profesional. 
Su objetivo principal es la fiscalización vial y de seguridad ciudadana, 
detectando infracciones en tiempo real (como motociclistas circulando 
sin casco) utilizando un modelo personalizado de YOLOv8, generando reportes 
formales mediante Google Gemini y enviando alertas automáticas con evidencia 
fotográfica directamente a un Bot de Telegram.

2. ARQUITECTURA DEL PROYECTO (MODULARIZACIÓN)
----------------------------------------------------------------------
El proyecto está desacoplado profesionalmente en los siguientes módulos:

- `main.py`: Archivo orquestador principal. Controla el bucle de captura 
  de video mediante OpenCV, gestiona los fotogramas e integra en tiempo real 
  el flujo de detección, redacción con IA y notificación.
- `detector.py`: Módulo dedicado a cargar el modelo de pesos entrenados 
  (`best.pt`), ejecutar YOLOv8 con tracking persistente (ByteTrack) y 
  filtrar las infracciones superando el umbral estricto de confianza.
- `reportero.py`: Módulo encargado de conectarse a la API de Google Gemini 
  para redactar reportes formales de fiscalización, almacenar las evidencias 
  fotográficas (`.jpg`) y registrar el historial en `registro_alertas.txt`.
- `notificador.py`: Módulo responsable de la comunicación en la nube con la 
  API HTTP de Telegram para despachar de forma inmediata las alertas activas 
  con fotos y texto enriquecido.
- `config.py`: Archivo de configuración global que lee la credencial de Gemini
  desde la variable de entorno `GEMINI_API_KEY` y define los parámetros del
  modelo y la clase objetivo.
- `best.pt`: Archivo de pesos entrenados a medida para la detección precisa 
  de infracciones viales.

3. REQUISITOS Y DEPENDENCIAS
----------------------------------------------------------------------
Asegúrate de tener instaladas las siguientes librerías de Python en tu entorno:

    pip install ultralytics opencv-python google-genai requests

4. CONFIGURACIÓN DE CREDENCIALES
----------------------------------------------------------------------
- Configura las variables de entorno `GEMINI_API_KEY`, `TELEGRAM_BOT_TOKEN`
  y `TELEGRAM_CHAT_ID` antes de iniciar el sistema. En PowerShell:

    $env:GEMINI_API_KEY = "tu_clave_de_gemini"
    $env:TELEGRAM_BOT_TOKEN = "tu_token_de_telegram"
    $env:TELEGRAM_CHAT_ID = "tu_chat_id"

- No guardes credenciales reales en el código ni en el repositorio. Los archivos
  `.pt`, las evidencias y la caché de Python se excluyen del control de versiones;
  coloca localmente los pesos necesarios para ejecutar el detector.

5. INSTRUCCIONES DE EJECUCIÓN
----------------------------------------------------------------------
1. Conecta tu cámara web (ej. dispositivo local o Logitech Brio 500).
2. Abre la terminal en la carpeta raíz del proyecto.
3. Ejecuta el script principal con el comando:

    python main.py

4. Para salir del sistema y liberar los recursos de video, haz clic 
   dentro de la ventana de visualización y presiona la tecla 'q'.

6. MECANISMO DE AUDITORÍA Y ALERTAS EN TIEMPO REAL
----------------------------------------------------------------------
Ante cada infracción detectada bajo el umbral de confianza establecido:
- Se realiza una captura automática de la evidencia en formato `.jpg`.
- Se consulta a Gemini AI para la redacción inteligente del reporte.
- Se despacha de forma instantánea la notificación al chat de Telegram.
- Se consolida un registro persistente en el archivo `registro_alertas.txt`.
======================================================================
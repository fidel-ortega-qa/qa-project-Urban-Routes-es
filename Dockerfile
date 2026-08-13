# Imagen base con Python 3.14
FROM python:3.14-slim-trixie

# Evita archivos .pyc y mejora la salida de logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalar Chromium y ChromeDriver
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    chromium \
    chromium-driver && \
    rm -rf /var/lib/apt/lists/*

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiar primero las dependencias
COPY requirements.txt .

# Instalar pytest y selenium
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el proyecto
COPY . .

# Ejecutar las pruebas al iniciar el contenedor
CMD ["python", "-m", "pytest", "main.py", "-v"]
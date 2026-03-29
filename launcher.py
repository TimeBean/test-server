import requests
import subprocess
import os

server_file = "kernel"

# читаем ссылку
with open(server_file, "r") as f:
    url = f.read().strip()

if not url:
    print("URL пустой")
    exit()

filename = "purpur.jar"  # сохраняем как .jar

# скачиваем JAR
try:
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"{filename} успешно скачан с {url}")
except requests.RequestException as e:
    print(f"Ошибка при загрузке: {e}")
    exit()

# запускаем сервер через java
try:
    subprocess.run(["java", "-Xmx2G", "-Xms1G", "-jar", filename, "nogui"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Ошибка при запуске сервера: {e}")

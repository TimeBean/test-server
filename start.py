import subprocess

JAVA = "java"
JAR_FILE = "purpur.jar"

XMS = "4G"
XMX = "32G"

JVM_FLAGS = [
    f"-Xms{XMS}",
    f"-Xmx{XMX}",
]

SERVER_ARGS = [
    "nogui"
]

cmd = [
    JAVA,
    *JVM_FLAGS,
    "-jar",
    JAR_FILE,
    *SERVER_ARGS
]

print("Запуск:", " ".join(cmd))
subprocess.run(cmd)

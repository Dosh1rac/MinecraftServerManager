import json

from app.services.rcon import MinecraftRcon
from app.models.server import MinecraftServer
from app.services.sftp import SFTPService


with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

sftp_client = SFTPService(
    host=config["server"]["host"],
    port=config["sftp"]["port"],
    username=config["sftp"]["username"],
    password=config["sftp"]["password"]
)

server = MinecraftServer(
    config["server"]["name"],
    config["server"]["host"],
    config["rcon"]["port"]
)

rcon = MinecraftRcon(
    server.ip,
    server.port,
    config["rcon"]["password"]
)


if rcon.connect():
    try:
        while True:
            command = input("Введите команду (или 'exit' для выхода): ")
            if command.lower() == "exit":
                break
            response = rcon.send_command(command)
            print(f"Ответ {response}")

    except KeyboardInterrupt:
                print("\nВыход из программы.")
    finally:
                rcon.disconnect()

if sftp_client.connect():
    try:
        while True:
            action = input("Введите действие (upload/download/exit): ")
            if action.lower() == "exit":
                break
            elif action.lower() == "upload":
                local_path = input("Введите локальный путь к файлу: ")
                remote_path = input("Введите удаленный путь для загрузки: ")
                sftp_client.upload_file(local_path, remote_path)
            elif action.lower() == "download":
                remote_path = input("Введите удаленный путь к файлу: ")
                local_path = input("Введите локальный путь для сохранения: ")
                sftp_client.download_file(remote_path, local_path)
            else:
                print("Неизвестное действие. Пожалуйста, выберите upload, download или exit.")
            
    except KeyboardInterrupt:
        print("\nВыход из программы.")
    finally:
        sftp_client.disconnect()
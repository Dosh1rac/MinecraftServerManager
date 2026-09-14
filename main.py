import json

from app.services.rcon import MinecraftRcon
from app.models.server import MinecraftServer


with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

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
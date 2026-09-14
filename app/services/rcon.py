from rcon import Console


class MinecraftRcon:
    def __init__(self, host, port, password):
        self.host = host
        self.port = int(port)
        self.password = password
        self.console = None

    def connect(self):
        try:
            self.console = Console(
                host=self.host,
                password=self.password,
                port=self.port
            )

            print("Подключение к Minecraft серверу успешно.")
            return True

        except Exception as e:
            self.console = None
            print(f"Ошибка подключения: {e}")
            return False

    def send_command(self, command):
        if not self.console:
            print("RCON не подключён.")
            return None

        try:
            return self.console.command(command)

        except Exception as e:
            print(f"Ошибка выполнения команды: {e}")
            return None

    def disconnect(self):
        if self.console:
            self.console.close()
            self.console = None
            print("Отключено от Minecraft сервера.")
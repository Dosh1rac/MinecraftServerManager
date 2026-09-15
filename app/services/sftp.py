import paramiko

class SFTPService:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.transport = None
        self.sftp = None

    def connect(self):
        try:
            self.transport = paramiko.Transport((self.host, self.port))
            self.transport.connect(username=self.username, password=self.password)
            self.sftp = paramiko.SFTPClient.from_transport(self.transport)
            print("Подключение к SFTP серверу успешно.")
        except Exception as e:
            print(f"Не удалось подключиться к SFTP серверу: {e}")

    def disconnect(self):
        if self.sftp:
            self.sftp.close()
        if self.transport:
            self.transport.close()
        print("Отключено от SFTP сервера.")

    def upload_file(self, local_path, remote_path):
        try:
            self.sftp.put(local_path, remote_path)
            print(f"Загружено {local_path} в {remote_path}.")
        except Exception as e:
            print(f"Не удалось загрузить файл: {e}")

    def download_file(self, remote_path, local_path):
        try:
            self.sftp.get(remote_path, local_path)
            print(f"Скачано {remote_path} в {local_path}.")
        except Exception as e:
            print(f"Не удалось скачать файл: {e}")

    def list_dir(self, remote_path):
        try:
            files = self.sftp.listdir(remote_path)
            print(f"Содержимое {remote_path}: {files}")
            return files
        except Exception as e:
            print(f"Не удалось получить список файлов: {e}")
            return []

    def delete_file(self, remote_path):
        try:
            self.sftp.remove(remote_path)
            print(f"Удален файл {remote_path}.")
        except Exception as e:
            print(f"Не удалось удалить файл: {e}")

    
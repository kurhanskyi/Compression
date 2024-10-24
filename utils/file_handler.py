import os

class FileHandler:
    @staticmethod
    def read_file(file_path: str) -> bytes:
        with open(file_path, 'rb') as file:
            return file.read()

    @staticmethod
    def write_file(file_path: str, data: bytes) -> None:
        with open(file_path, 'wb') as file:
            file.write(data)

    @staticmethod
    def get_file_size(file_path: str) -> int:
        return os.path.getsize(file_path)

    @staticmethod
    def delete_file(file_path: str) -> None:
        os.remove(file_path)
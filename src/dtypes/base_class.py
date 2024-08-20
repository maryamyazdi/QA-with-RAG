class DataFile:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = None

    def load(self):
        raise NotImplementedError

    def save(self, path: str):
        pass

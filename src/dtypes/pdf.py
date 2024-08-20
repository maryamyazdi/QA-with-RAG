from pypdf import PdfReader
from src.dtypes.base_class import DataFile
import ntpath


class PDF(DataFile):
    def __init__(self, file_path: str):
        super().__init__(file_path)
        self.filename = ntpath.basename(file_path)
        self.data = self.load()
        self.pages = [page.extract_text() for page in self.data.pages]
        self.full_text = " ".join(self.pages)

    def load(self) -> PdfReader:
        return PdfReader(self.file_path)

    def save(self, path: str):
        raise NotImplementedError

    def __len__(self):
        return len(self.pages)

    def __bool__(self):
        return self.data and bool(len(self))

    def __getitem__(self, page_index):
        return self.pages[page_index]

    def __repr__(self):
        return f"PDF file at {self.file_path}"

from glob import glob
from typing import List

from src.dtypes import PDF


def load_pdfs(dir: str = "src/user_docs/") -> List[PDF]:
    pdf_files = []
    file_paths = glob(dir + "/*.pdf")
    for fpath in file_paths:
        pdf_files.append(PDF(file_path=fpath))
    return pdf_files

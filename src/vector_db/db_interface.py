from typing import List
import pickle
import os

from src.dtypes import PDF
from src.vector_db import Faiss


class FaissInterface:
    def __init__(self, db_path: str = "./store/") -> None:
        self.db_path = db_path

    def load_db(self, path: str):
        with open(path, "rb") as f:
            db = pickle.load(f)
        return db

    def save_db(self, path: str, db: Faiss):
        with open(path, "wb") as f:
            pickle.dump(db, f)

import os
from pathlib import Path
from typing import List, Union, Tuple
import faiss
import logging

from src.dtypes import PDF
from src.utils.helper_functions import texts_to_embeddings, split_text


class Faiss:
    def __init__(self, dimension: int = 384, db_path: str = "./store/faiss.db"):
        self.db_path = db_path
        self.source_files = None

        if os.path.exists(self.db_path):
            os.remove(self.db_path)

        if Path(self.db_path).is_file():
            self.index = faiss.read_index(
                self.db_path
            )  # retrieve the index of the available vector store
            logging.info("Database loaded.")
        else:
            self.index = faiss.IndexFlatL2(dimension)  # create new index
        self.chunks = []

    def add(self, input_data: Union[List[str], List[PDF]]):
        chunks = []
        source_files = []
        for data in input_data:
            if isinstance(data, str):
                L = len(chunks)
                chunks += split_text(data)
            if isinstance(data, PDF):
                L = len(chunks)
                chunks += split_text(data.full_text)
                source_files += [data.file_path] * (len(chunks) - L)
        vectors = texts_to_embeddings(texts=chunks)[0]
        logging.info(f"Successfully vectorized.")
        self.index.add(vectors)
        self.chunks = chunks
        self.source_files = source_files

        Path(self.db_path).parent.mkdir(exist_ok=True, parents=True)
        Path(self.db_path).touch(exist_ok=True)
        faiss.write_index(self.index, self.db_path)
        logging.info(f"{len(input_data)} items added to database.")

    def query(
        self, query: str, n_results: int = 1
    ) -> Tuple[List[str], List[str], List[float]]:
        query_vectors = texts_to_embeddings([query])
        D, I, V = self.index.search_and_reconstruct(query_vectors, n_results)
        return (
            [
                self.chunks[i]
                for i in I.reshape(
                    n_results,
                )
            ],
            [
                self.source_files[i]
                for i in I.reshape(
                    n_results,
                )
            ],
            D.reshape(
                n_results,
            ).tolist(),
        )

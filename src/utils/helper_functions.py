from typing import List
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from langchain_text_splitters import SentenceTransformersTokenTextSplitter


def split_text(text_input: str, model_name="all-MiniLM-L6-v2"):
    splitter = SentenceTransformersTokenTextSplitter(
        chunk_overlap=0,
        model_name=f"sentence-transformers/{model_name}",
    )
    chunks = splitter.split_text(text_input)
    return chunks


def texts_to_embeddings(
    texts: List[str],
    model_name="all-MiniLM-L6-v2",
    do_tfidf: bool = False,
    trained_tfidf: TfidfVectorizer = None,
):
    model = SentenceTransformer(model_name)
    bert_vectors = model.encode(texts)
    if not do_tfidf:
        return bert_vectors, None

    if trained_tfidf is not None:
        tfidf = trained_tfidf
        clean_texts = [text for text in texts]
        tfidf_vectors = tfidf.transform(clean_texts).toarray()
        concatenated_vectors = np.concatenate([bert_vectors, tfidf_vectors], axis=1)
    else:
        tfidf = TfidfVectorizer(max_features=600)
        clean_texts = [text for text in texts]
        tfidf_vectors = tfidf.fit_transform(clean_texts).toarray()
        concatenated_vectors = np.concatenate([bert_vectors, tfidf_vectors], axis=1)

    return concatenated_vectors, tfidf

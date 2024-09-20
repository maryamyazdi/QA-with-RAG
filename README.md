# Question Answering with Retrieval-Augmented Generation

QA-with-RAG is a free, containerised question-answer framework that allows you to ask questions about your documents and get accurate answers.

This app uses a method called retrieval-augmented generation (RAG) to retrieve information that is relevant to your question from your uploaded documents. It then uses a large language model (LLM) to answer the question with the retrieved context.

## Preview
<div align="center">
  <img width="90%" height="auto" alt="" src="https://github.com/user-attachments/assets/d3010bd6-bc6e-46e7-85cb-8fe090441c38" />
</div>

## Technical Components

The current implementation uses the following components:

- **Language Models:** [Google Gemma2 (2B)](https://ai.google.dev/) and [Microsoft Phi 3 Mini (3.8B)](https://azure.microsoft.com/en-us/blog/introducing-phi-3-redefining-whats-possible-with-slms/)
- **Embedding Model:** [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- **Vector Database:** [Faiss DB](https://faiss.ai/)
- **Frontend:** [Streamlit](https://streamlit.io/)
- **Maintenance:** [Docker](https://www.docker.com/)


## Getting Started

1. [Install poetry](https://python-poetry.org/docs/#installing-with-pipx) on your machine

2. Creat a virtual environment and install the dependencies specified in the `pyproject.toml` file by running
```
poetry install
```
3. Run the project using the command
```
docker compose up
```
> Note: The first time you run this, it might take a while to build the image and download the embedding model.

4. The UI (as showed in the snapshot in the [Preview](#preview) section) should open up in your default browser running on the `port 8501`.

## Usage
I.  Select the directory containing your pdf file(s).

II. Type your question

III. Choose a language model used for final inference

VI. Choose the number of retrieved chunks from the database. The higher this number, the more complex your result may be.

V. Run and enjoy!
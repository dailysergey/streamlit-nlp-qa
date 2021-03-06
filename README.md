# [streamlit-nlp-qa](https://share.streamlit.io/dailysergey/streamlit-nlp-qa/main/app.py) <-- click to check the app
![main image](https://github.com/dailysergey/streamlit-nlp-qa/blob/main/main.png)
Question Answering models can retrieve the answer to a question from a given text, which is useful for searching for an answer in a document. Some question answering models can generate answers without context!

Stack:

-   [Streamlit](https://streamlit.io/) - the fastest way to build and share data apps
-   [Pinecone](https://www.pinecone.io/) - makes it easy to build high-performance vector search applications
-   [squad_v2](https://huggingface.co/datasets/squad_v2) - dataset for pinecone index
-   [pinecone/mpnet-retriever-squad2](https://huggingface.co/pinecone/mpnet-retriever-squad2) - model to build vector embeddings index in pinecone

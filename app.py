import streamlit as st
import pinecone
from sentence_transformers import SentenceTransformer

st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">', unsafe_allow_html=True)


@st.experimental_singleton
def init_retriever():
    # initialize retriever model
    return SentenceTransformer('pinecone/mpnet-retriever-squad2')


@st.experimental_singleton
def init_pinecone():
    # initialize connection to Pinecone vector DB (app.pinecone.io for API key)
    with open('./secret', 'r') as fp:
        # get key from app.pinecone.io
        API_KEY = fp.read()
    pinecone.init(
        api_key=API_KEY,
        environment='us-west1-gcp'
    )
    index = pinecone.Index('qa-index')
    return index


def card(id_val, source, context):
    st.markdown(f"""
    <div class="card" style="margin:1rem; background-color:lightgrey;">
        <div class="card-body">
            <h5 class="card-title">{source}</h5>
            <h6 class="card-subtitle mb-2 text-muted">{id_val}</h6>
            <p class="card-text">{context}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)


# initialize the index and retriever components
index = init_pinecone()
retriever = init_retriever()

st.write("""
# AI Q&A
Ask me a question!
""")


query = st.text_input("Search!", "")

if query != "":
    # encode the query as sentence vector
    xq = retriever.encode([query]).tolist()
    # print(xq)
    # get relevant contexts
    xc = index.query(xq, top_k=5, include_metadata=True)

    print(xc)
    # display each context (NEW PART)
    for context in xc['results'][0]['matches']:
        card(
            context['id'],
            context['score'],
            context['metadata']['text']
        )

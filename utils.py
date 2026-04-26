from nltk.tokenize import sent_tokenize
import nltk

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

def chunk_text(text, chunk_size=5):
    sentences = sent_tokenize(text)

    chunks = []
    for i in range(0, len(sentences), chunk_size):
        chunk = " ".join(sentences[i:i+chunk_size])
        chunks.append(chunk)

    return chunks
from sentence_transformers import CrossEncoder

reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def rerank(query, chunks):
    if len(chunks) == 0:
        return chunks

    pairs = [(query, chunk) for chunk in chunks]
    scores = reranker.predict(pairs)

    ranked = [x for _, x in sorted(zip(scores, chunks), reverse=True)]

    return ranked
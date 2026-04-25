from src.rag_chain import answer_question

print("Document Q&A Bot Started")
print("Type quit to exit")

while True:

    q = input("\nAsk: ")

    if q.lower() == "quit":
        break

    answer, sources, _ = answer_question(q)

    print("\nANSWER:")
    print(answer)

    print("\nSOURCES:")
    for s in sources:
        print(f"- {s.metadata['source']} | Page {s.metadata['page']}")
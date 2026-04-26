def keyword_filter(query, chunks):
    keywords = query.lower().split()
    filtered = []

    for c in chunks:
        if any(k in c.lower() for k in keywords):
            filtered.append(c)

    return filtered if filtered else chunks
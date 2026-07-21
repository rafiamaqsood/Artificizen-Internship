
def build_prompt(query, chunks):
    prompt = "Context:\n"
    for i, chunk in enumerate(chunks, start=1):
        prompt += f"{i}. {chunk}\n"
    prompt += f"Question:\n{query}\n"
    prompt += (
        "Answer using only the context above.\n"
        "If the answer is not in the context, say: I don't know."
    )
    return prompt
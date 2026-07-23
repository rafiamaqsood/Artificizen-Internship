
def build_prompt(context, history, query):
    prompt = f"""You are a helpful assistant. \n Only answer from the provided context. \n If the answer isn't present, reply exactly:
    I don't know. \n Chat History:\n {history} \n Context:\n {context} \n User Question: \n {query} \n Answer:
    """
    return prompt
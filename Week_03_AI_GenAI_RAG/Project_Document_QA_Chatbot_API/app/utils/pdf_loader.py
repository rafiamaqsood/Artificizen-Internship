import pymupdf4llm

def read_pdf(pdf):
    text = pymupdf4llm.to_markdown(str(pdf))
    return text
                                   
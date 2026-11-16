# from langchain_text_splitters import RecursiveCharacterTextSplitter


# def split_text(content: str) -> list[str]:
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=50
#     )

#     return splitter.split_text(content)







from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(content: str) -> list[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    return splitter.split_text(content)
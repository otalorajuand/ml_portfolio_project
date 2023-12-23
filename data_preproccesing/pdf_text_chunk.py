import os
import PyPDF2


def chunk_text(text, chunk_size):
    """Splits the input text into chunks based on the specified chunk size.

    Args:
    - text (str): The input text to be chunked.
    - chunk_size (int): The maximum size of each chunk in terms of characters.

    Returns:
    - chunks (list): A list of chunks where each chunk is a string not 
      exceeding the chunk size.
    """
    chunks = []
    words = text.split()
    current_chunk = ''
    for word in words:
        if len(current_chunk) + len(word) + 1 <= chunk_size:
            current_chunk += word + ' '
        else:
            chunks.append(current_chunk)
            current_chunk = word + ' '
    if current_chunk:
        chunks.append(current_chunk)
    return chunks


def extract_and_chunk_text(file_path, chunk_size):
    """Extracts text from a PDF file, chunks it based on a specified size,
    and returns information about the text chunks.

    Args:
    - file_path (str): The path to the PDF file.
    - chunk_size (int): The desired size (approximate) for each text chunk.

    Returns:
    - A list containing information about text chunks extracted from the PDF.
      Each element in the list represents a chunk and its associated 
      information.
    """

    chunks_info = []
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            # Split text into chunks approximately the size of a page
            # Adjust the chunk size as needed
            chunks = chunk_text(text, chunk_size)
            chunks_info.extend(chunks)
    return chunks_info


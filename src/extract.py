from pypdf import PdfReader
import re
import sys

def get_text_from(pdf):
    '''
    Read the pdf from the given path
    Remove unwanted headings, lines and spaces
    Return the whole pdf as a single string
    '''
    try:
        reader = PdfReader(pdf)
        whole_pdf = []
        for idx, page in enumerate(reader.pages):
            lines = page.extract_text().split('\n')
            if idx == 0:
                # Remove the table header and pdf headers on page 1
                lines = lines[1:-1]
                lines[-1] = lines[-1].split('NORMAN')[0]
            elif idx == len(reader.pages) - 1:
                # Remove the pdf creation date on the last page
                lines = lines[:-1]
            whole_pdf.append(' '.join(lines))
        return ' '.join(whole_pdf)
    except Exception as e:
        print(f"Error reading the PDF, {pdf}: {e}", file=sys.stderr)
        return

def parse(pdf):
    '''
    Extract table content from the pdf and return a list of rows
    '''
    # Get the pdf as text
    pdf_text = get_text_from(pdf)
    if not pdf_text:
        return
    
    pattern = r"\s?(\d{1,2}\/\d{1,2}\/\d{2,4}\s\d{1,2}:\d{2})\s*" # Date / Time pattern
    pattern += r"(\d+-\d+)\s*" # Incident Number Pattern
    pattern += r"(?:((?:[A-Z0-9\-\,\<\>\/\s]+)|[0-9\.\-;]+)?\s*)?" # Location Pattern
    pattern += r"(?:([A-Z][a-z]+\s?[A-Za-z\d\s\/]+)\s)?" # Nature pattern
    pattern += r"(EMSSTAT|OK0140200|14005|14009)\s*" # Incident ORI pattern

    result = re.findall(pattern, pdf_text)

    ## Pattern to extract some edge cases in Nature
    pattern = r"\s?(\d{1,2}\/\d{1,2}\/\d{4}\s\d{1,2}:\d{2})\s*" # Date / Time pattern
    pattern += r"(\d+-\d+)\s*" # Incident Number Pattern
    pattern += r"(?:((?:[A-Z0-9\-\,\<\>\/\s]+)|[0-9\.\-;]+)?\s*)?" # Location Pattern
    pattern += r"((?:MVA |EMS |COP |911 [A-Z][a-z]+\s)[A-Za-z\d\s\/]+)\s" # Nature pattern
    pattern += r"(EMSSTAT|OK0140200|14005)\s*" # Incident ORI pattern

    result.extend(re.findall(pattern, pdf_text))

    return result
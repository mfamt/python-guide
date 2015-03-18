def extract_text_from_pdfs():
    """ Extract plaintext from each narrative PDF

    Pre:
          - fetch_pdfs() has successfully executed, and
            PDF_DIR contains several .pdf pages
          - pdftotext is installed on the system

    Post:
          - PDF_DIR contains a .txt file for corresponding .pdf
            file

    Returns: Nothing
    """
    for pdf_name in glob(os.path.join(PDF_DIR, '*.pdf')):
        txt_name = os.path.splitext(pdf_name)[0]
        print("pdftotext '%s' '%s'" % (pdf_name, txt_name))
#        os.system("pdftotext '%s' '%s'" % (input1, output))


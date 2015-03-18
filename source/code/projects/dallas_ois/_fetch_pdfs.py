def fetch_pdfs(incidents):
    """ Download each PDF for each Dallas OIS record

    Args:
          - incidents: a list of dicts, presumably from extract_incidents()
    Post:
          - PDF_DIR contains a .pdf file for every OIS record
          - Each PDF filename is the basename of the original URL
            e.g. /ois/docs/narrative/2003/OIS_2003_804107M.pdf
             is saved as: PDF_DIR/OIS_2003_804107M.pdf

    Returns: Nothing
    """
    for incident in incidents:
        pdf_url = incident['pdf_url']
        resp = requests.get(pdf_url)
        # designate a filename
        pdf_savename = PDF_FILE.format(
            os.path.splitext(os.path.basename(pdf_url))[0]
        )
        with open(pdf_savename, 'wb') as f:
            f.write(resp.content)
            # notify the user and sleep
            print("Saving {0} to {1}".format(pdf_url, pdf_savename))
            sleep(0.3)

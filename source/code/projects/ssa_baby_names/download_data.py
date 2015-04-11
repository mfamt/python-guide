from os.path import basename, splitext
from os import makedirs
from tempfile import NamedTemporaryFile
import shutil
import requests
SITEURL = 'http://www.ssa.gov/OACT/babynames/{0}'
babypaths = ('nationwide', 'names.zip'), ('state', 'state/namesbystate.zip')
for path, zipurl in babypaths:
    # Download the files
    print("Downloading:", zipurl, 'Saving to: ',  path)
    makedirs(path, exist_ok = True)
    with NamedTemporaryFile(suffix = '.zip') as zipfile:
        # Download the data
        data = requests.get(SITEURL.format(zipurl)).content
        # Write to the temporary file and rewind the file handler
        zipfile.write(data)
        zipfile.seek(0)
        # Unzip the zipfile into /path
        shutil.unpack_archive(zipfile.name, path)

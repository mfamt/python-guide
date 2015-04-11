---
title: Download and Unzip a File Without Saving the Zip
ordernum: 1200
references:
  - url: http://stackoverflow.com/a/5711095/160863
    title: 'Answer to "Python: downloading and unzipping a .zip file without writing to disk"'  
  - url: https://docs.python.org/3/library/io.html#text-i-o
---


## Downloading a zip and unzipping it 

Using the most basic steps

~~~py
from urllib.request import urlopen
from zipfile import ZipFile
zipurl = 'http://stash.compjour.org/data/1800ssa.zip'
# Download the file from the URL
zipresp = urlopen(zipurl)
# Create a new file on the hard drive
tempzip = open("/tmp/tempfile.zip", "wb")
# Write the contents of the downloaded file into the new file
tempzip.write(zipresp.read())
# Close the newly-created file
tempzip.close()
# Re-open the newly-created file with ZipFile()
zf = ZipFile("/tmp/tempfile.zip")
# Extract its contents into /tmp/mystuff
# note that extractall will automatically create the path
zf.extractall(path = '/tmp/mystuff')
# close the ZipFile instance
zf.close()
~~~


## Using temp file and shutil

Why go through the process of naming a temporary file?

~~~py
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
from shutil import unpack_archive
zipurl = 'http://stash.compjour.org/data/1800ssa.zip'
zipresp = urlopen(zipurl)
tfile = NamedTemporaryFile()
tfile.write(zipresp.read())
tfile.seek(0)
unpack_archive(tfile.name, '/tmp/mystuff2', format = 'zip')
zipresp.close()
tfile.close()
~~~

A little shorter:

~~~py
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
from shutil import unpack_archive
zipurl = 'http://stash.compjour.org/data/1800ssa.zip'
with urlopen(zipurl) as zipresp, NamedTemporaryFile() as tfile:
    tfile.write(zipresp.read())
    tfile.seek(0)
    unpack_archive(tfile.name, '/tmp/mystuff3', format = 'zip')
~~~


## Unzipping without saving the zip

Solution via [StackOverflow user Vishal](http://stackoverflow.com/a/5711095/160863):

~~~py
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
zipurl = 'http://stash.compjour.org/data/1800ssa.zip'
with urlopen(zipurl) as zipresp:
    with ZipFile(BytesIO(zipresp.read())) as zfile:
        zfile.extractall('/tmp/mystuff4')
~~~




## Why you should write to disk

For personal, non-enterprise projects, you should almost always write to disk. The chance that you're in a situation in which a file is too big to be saved to the hard drive but not too big to save in memory is going to be rare. Let's face it, if you're on your last GB of desktop/laptop HD space, you have a rather pressing issue to deal with even before you download the file.


## Why you should not write to disk


It's _often_ good to keep tasks separate. And downloading and unzipping a file are clearly separate tasks and even have their own complete modules. But if the combined process is simple enough, then sometimes it's useful to keep both independent tasks in the same things.

Organization clutter is a very real problem. An obvious solution is to have a different subroutine that cleans out old files. But sometimes that script fails, forcing the programmer to dig out the problem. And if the tasks are split across different files, that programmer will be inconvenienced TK.





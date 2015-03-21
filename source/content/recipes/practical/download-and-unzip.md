---
title: Download and Unzip a File Without Saving the Zip
ordernum: 1200
references:
  - url: http://stackoverflow.com/a/5711095/160863
    title: 'Answer to "Python: downloading and unzipping a .zip file without writing to disk"'  
  - url: https://docs.python.org/3/library/io.html#text-i-o
---


## Downloading a zip and unzipping it 

~~~py
with ZipFile(zipname) as zf:
    zf.extractall(path = '/tmp')
~~~


## Using temp file

~~~py
from urlib.request import urlretrieve
tmpname, headers = urlretrieve('http://python.org') 
with ZipFile(tmpname) as zf:
    zf.extractall(path = '/tmp')
~~~




## Unzipping without saving the zip

Solution via [StackOverflow user Vishal](http://stackoverflow.com/a/5711095/160863):

~~~py
from StringIO import StringIO
from zipfile import ZipFile
# assuming this step has happened:
# resp = urlopen("http://www.example.com/a.zip")
with ZipFile(StringIO(resp.read())) # TK
~~~




## Why you should write to disk

For personal, non-enterprise projects, you should almost always write to disk. The chance that you're in a situation in which a file is too big to be saved to the hard drive but not too big to save in memory is going to be rare. Let's face it, if you're on your last GB of desktop/laptop HD space, you have a rather pressing issue to deal with even before you download the file.


## Why you should not write to disk


It's _often_ good to keep tasks separate. And downloading and unzipping a file are clearly separate tasks and even have their own complete modules. But if the combined process is simple enough, then sometimes it's useful to keep both independent tasks in the same things.

Organization clutter is a very real problem. An obvious solution is to have a different subroutine that cleans out old files. But sometimes that script fails, forcing the programmer to dig out the problem. And if the tasks are split across different files, that programmer will be inconvenienced TK.





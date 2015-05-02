# A translation of crismdp/s3.sh
# Uploading to S3 in 18 lines of Shell
# https://gist.github.com/chrismdp/6c6b6c825b07f680e710
from os.path import expanduser, join
import requests
from base64 import b64encode
from datetime import datetime
from hashlib import sha1
import hmac

DEFAULT_S3_AUTH_FILE = '~/.creds/s3'

def open_aws_creds(auth_file):
    with open(expanduser(auth_file), 'r') as af:
        return af.read().splitlines()

def put_s3(local_path, bucket, s3_path, auth_file = DEFAULT_S3_AUTH_FILE):
    key, secret = open_aws_creds(auth_file)
    s3_canonical_path = (bucket + '/' + s3_path).replace('//', '/', 1)
    headers = {}
    headers['Host'] = "%s.s3.amazonaws.com" % bucket
    headers['Date'] = datetime.strftime(datetime.now(), '%a, %d %b %Y %T +0000')
    headers['Content-Type'] ='text/plain; charset=us-ascii'
    headers['x-amz-acl'] = "public-read"
    headers["Authorization"] = 'AWS %s:%s' % (key, signature(secret, s3_canonical_path, headers))

    requests.put("https://" + s3_canonical_path, headers = headers,
                                data = {'filename': expanduser(local_path)})


def signature(secret, fpath, headers):
    pstr = "PUTS\n\n" + \
    headers['Content-Type'] + '\n' + \
    headers['Date'] + '\n' + \
    'x-amz-acl:public-read' + '\n' + fpath
    # http://stackoverflow.com/questions/8338661/implementaion-hmac-sha1-in-python
    hashed = hmac.new(secret.encode('utf-8'), pstr.encode('utf-8'), sha1)
    return b64encode(hashed.digest())




fpath = "/tmp/sup.txt"
auth_file = DEFAULT_S3_AUTH_FILE

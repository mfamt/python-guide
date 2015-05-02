# A translation of crismdp/s3.sh
# Uploading to S3 in 18 lines of Shell
# https://gist.github.com/chrismdp/6c6b6c825b07f680e710
from os.path import expanduser, splitext
from datetime import datetime
from hashlib import sha1
from urllib.parse import urljoin
import base64
import hmac
import requests
import six
import mimetypes

DEFAULT_S3_AUTH_FILE = '~/.creds/s3'

def open_aws_creds(auth_file):
    with open(expanduser(auth_file), 'r') as af:
        return af.read().splitlines()

def put_s3_file(local_path, bucket, s3_path, auth_file = DEFAULT_S3_AUTH_FILE,
        acl = "public-read", content_type = None ):
    key, secret = open_aws_creds(auth_file)
    s3_canonical_path = (bucket + '/' + s3_path).replace('//', '/', 1)
    headers = {}
    headers['Host'] = "%s.s3.amazonaws.com" % bucket
    headers['Date'] = datetime.utcnow().strftime("%a, %d %b %Y %T +0000")
    headers['Content-Type'] = content_type if content_type is not None else determine_mime(local_path)
    headers['x-amz-acl'] = acl
    signature = sign_request(secret = secret, s3_canonical_path = s3_canonical_path,
        content_type = headers['Content-Type'], date = headers['Date'], acl = acl)
    headers["Authorization"] = 'AWS %s:%s' % (key,signature)
    s3_full_path = urljoin('http://%s.s3.amazonaws.com' % bucket, s3_path)
    resp = requests.put(s3_full_path,
                                headers = headers,
                                data = open(expanduser(local_path), 'rb'))

    return resp


def put_s3(local_path, bucket, s3_path, auth_file = DEFAULT_S3_AUTH_FILE):
    """
    Wrapper method that can handle directories. TODO
    """

    return None


def sign_request(secret, s3_canonical_path, content_type, date, acl):
    """
    Signs the request as specified in AWS REST docs
    http://docs.aws.amazon.com/AmazonS3/latest/dev/RESTAuthentication.html
    """
    pstr = """
PUT

{content_type}
{date}
x-amz-acl:{acl}
/{s3_canonical_path}""".format(content_type = content_type,
    date = date, acl = acl, s3_canonical_path = s3_canonical_path).strip()
    hashed = hmac.new(secret.encode('utf-8'), digestmod = sha1)
    hashed.update(six.b(pstr))
    return base64.encodestring(hashed.digest()).strip().decode('utf-8')



def determine_mime(fname):
    mimes = mimetypes.guess_type(fname)
    return mimes[0] if mimes[0] is not None else 'application/octet-stream'



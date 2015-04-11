---
title: Sending a Text Message via Twilio's API
ordernum: 5200
references:
  - title: Twilio Python Helper Library documentation
    url: https://www.twilio.com/docs/python/install
---


## Sign up with Twilio

[Sign up](https://www.twilio.com/try-twilio)

Check [out the API explorer](https://www.twilio.com/user/account/developer-tools/api-explorer/message-create)

## Installation

~~~sh
pip install twilio
~~~

## Code

via [Twilio Python Helper Library documentation](https://www.twilio.com/docs/python/install):

~~~py
from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
ACCOUNT_SID = "YOURACCOUNTSID" 
AUTH_TOKEN = "YOURACCOUTAUTHTOKEN" 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
#    to = "+15556667777",    # Replace with the number you want to text
#    from_ ="+15558675309")  # Replace with your Twilio number
#    Note that the parameter is named `from_`, not `from`
message = client.messages.create(to = "+15558675309", from_ = "+15556667777",
  body = "Oh, you don't know me, but you make me so happy")
~~~



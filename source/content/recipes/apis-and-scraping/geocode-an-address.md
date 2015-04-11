---
title: Geocode an address with Google Maps API
ordernum: 1450
---





- Translate address to URL
- Get response from Google
- Parse response as JSON
- Deal with edge cases



[Sample geocoding result](https://developers.google.com/maps/documentation/geocoding/#GeocodingRequests):

`http://maps.googleapis.com/maps/api/geocode/output?parameters`


Base endpoint:

      https://maps.googleapis.com/maps/api/geocode/json

Required `address` parameter:

      address=450+Serra+Mall+Stanford+CA


Using Requests:

payload = {'address': '450 Serra Mall Stanford CA'}
resp = requests.get("http://www.example.com", params = payload)

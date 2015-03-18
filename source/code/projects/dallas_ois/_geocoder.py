
# bad address: 2009 - 282646W
# double incident:
#  2004: 280895N, 281418N, rowspan = 2
def geocode_incidents(incidents):
    """ Get geo-coordinates for every incident using Google Geocoder API v3
    Args:
          - incidents: a list of dicts, presumably from extract_incidents(),
              each one having a 'location' key

    Pre:  None
    Post:
          - GEOCODE_DIR contains a .json file for every incident
          - each .json file is named according to "case_number"

    Returns: Nothing
    """

    for incident in incidents:
        addr = incident['location']
        full_addr = ", ".join([addr, 'Dallas', 'TX'])
        dest_name = GEOCODE_FILE.format(incident['case_number'])
        req_resp = geocode_address(full_addr)

        print("Geocoded '{0}' and saving to {1}".format(full_addr, dest_name))



def geocode_address(addr_string):
    """ Get geo-coordinates for every incident using Google Geocoder API v3
    Args:
          - addr_string: A full address, such as "400 Broadway, Springfield, IL"

    Pre:  Google Geocoding API is functional
    Post: None
    Returns: An object of type `requests.models.Response`

    Google API is documented here:
    https://developers.google.com/maps/documentation/geocoding/#GeocodingRequests
    """

    return "{TODO}"


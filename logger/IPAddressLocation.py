import requests

def getGeoData(ip):
    # Getting geolocation data from 'ipwhois.io'
    # Free version only allow 10,000 requests / month
    geolocate_url = 'http://free.ipwhois.io/json/{}'.format(ip)

    try:
        # Getting geolocation of IP
        geolocate_response = requests.get(geolocate_url) 
        geolocate_response.raise_for_status()

    except requests.exceptions.HTTPError as errh:
        print ("Http Error: ", errh)

    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting: ",errc)

    except requests.exceptions.Timeout as errt:
        print ("Timeout Error: ",errt)

    except requests.exceptions.RequestException as err:
        print ("Something went wrong: ",err)
        
    # Converting response to list
    geoData = geolocate_response.json()

    return geoData
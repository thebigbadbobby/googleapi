from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import time

def simple_get(url):
    print(url)
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    outFile = open("html.txt",'w+')
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'From': 'flowservices@gmail.com'  # This is another valid field
}
    try:
        with closing(get(url, stream=True, headers=headers)) as resp:
            if is_good_response(resp):
                html=str(resp.content)
                outFile.write(html)
                marker=html.index(":0x")+22 #whatever it is find out
                address=""
                while(True):
                    if html[marker] =='"':
                        break
                    address+=html[marker]
                    marker+=1
                return address
            else:
                print(is_good_response(resp))
                print("get failed")
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None
def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """

    content_type = resp.headers['Content-Type'].lower()
    #print(resp)
    print(content_type)
    return ((resp.status_code == 200 or resp.status_code == 204)
            and content_type is not None)
def verify(address):
    verified=simple_get("https://www.google.com/maps/search/" + address)
    print(verified)
    if "]" in verified:
        verified="No Results"
    print(verified)
    return verified
verify("1179 Barbara Avenue")
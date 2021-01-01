
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import time

def simple_get(url, double):
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
                marker=html.index(":0x")+21 #whatever it is find out
                if html[marker] =='"':
                    marker+=1
                address=""
                while(True):
                    if html[marker] =='"':
                        break
                    address+=html[marker]
                    marker+=1
                options=[]
                while(True):
                    try:
                        html=html[html.index("http://www.google.com/search?q\\\\\\\\u003d")+39:]
                        option=""
                        while(True):
                            if html[0]=="\\":
                                options.append(option)
                                #print(option)
                                break
                            option+=html[0]
                            html=html[1:]         
                    except:
                        break
                args=[]
                args.append(address)
                if double:
                    return args
                for opt in options:
                    args.append(verify(opt, True))
                return args
            else:
                #print(is_good_response(resp))
                #print("get failed")
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
    #print(content_type)
    return ((resp.status_code == 200 or resp.status_code == 204)
            and content_type is not None)
def verify(address, double=False):
    try:
        verified=simple_get("https://www.google.com/maps/search/" + address, double)
    except:
        verified=["Are you sure that's a real address? Please try different search terms and try again."]
    #print(verified)
    #print("apple")
    #print(verified[0])
    if "]" in verified[0] or verified[0]== "California":
        verified[0]="Something looks a bit off. Please check for typos."
    elif "[" in verified[0]:
        #print("ekans")
        #print(verified)
        new=[]
        for entry in verified:
            new.append(entry.replace("\\","").replace("u0026",""))
        
        return new[1:]
            # while(True):
            #         if html[marker] =='"':
            #             break
            #         address+=html[marker]
            #         marker+=1
    return verified[0]
print(verify("3241 Crystal Springs Dr, Soquel, CA"))
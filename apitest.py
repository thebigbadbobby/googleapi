from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import time

<<<<<<< Updated upstream
def simple_get(url, double):
=======
def simple_get(url):
    addressOff=True #sometimes, their address is a little off.
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
                marker=html.index(":0x")+21 #whatever it is find out
                if html[marker] =='"':
                    marker+=1
=======
                marker=html.index(":0x")+22 #whatever it is find out
                if 'Building' in html:
                    addressOff=False
>>>>>>> Stashed changes
                address=""
                while(True):
                    if html[marker] =='"':
                        break
                    address+=html[marker]
                    marker+=1
<<<<<<< Updated upstream
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
=======
                return [address,addressOff]
>>>>>>> Stashed changes
            else:
                #print(is_good_response(resp))
                #print("get failed")
                return None

    except RequestException as e:
<<<<<<< Updated upstream
        print('Error during requests to {0} : {1}'.format(url, str(e)))
=======
        #print('Error during requests to {0} : {1}'.format(url, str(e)))
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
def verify(address, double=False):
    try:
        print("start")
        verified=simple_get("https://www.google.com/maps/search/" + address, double)
        print(verified)
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
            print(entry)
            new.append(entry.replace("\\","").replace("u0026",""))
        print("arbok")
        return new[1:]
            # while(True):
            #         if html[marker] =='"':
            #             break
            #         address+=html[marker]
            #         marker+=1
    print("result", verified[0])
    return verified
exact_test_cases=[
    "8405 Barton Road, Granite Bay, CA 95746",
    "14720 Mcelroy Road, Auburn, CA ",
    "2242 Langview Drive, Roseville, CA",
    "3241 Crystal Heights Drive, Soquel, CA, 95073",
    "2270 Benson Avenue, Santa Cruz, CA 95065",
    "111 Laurent Street, Santa Cruz, CA 95060",
    "5541 McMahon Dr, Sacramento CA 95824",
    "220 Mary Street, Auburn, CA, 95604",
    "2040 Camp Whitney Circle, Rocklin, CA 95765",
    "411 Olive St, Santa Cruz, CA 95060",
    "202 Oakdale Drive, Aptos",
    "947 Windsor St, Santa Cruz, CA 95060",
    "22980 E Cliff Dr, Santa Cruz",
    "1750 41st Ave Capitola",
    "1343 Greenborough Dr, Roseville, CA 95661",
    "5665 Montclair circle, Rocklin, CA 95677",
    "112 Earl Avenue, Roseville, ca 95678"
]
nozip_test_cases=[
    "8405 Barton Road, Granite Bay, CA",
    "14720 Mcelroy Road, Auburn, CA ",
    "2242 Langview Drive, Roseville, CA",
    "3241 Crystal Heights Drive, Soquel, CA",
    "2270 Benson Avenue, Santa Cruz, CA",
    "111 Laurent Street, Santa Cruz, CA",
    "5541 McMahon Dr, Sacramento CA",
    "220 Mary Street, Auburn, CA",
    "2040 Camp Whitney Circle, Rocklin, CA",
    "411 Olive St, Santa Cruz, CA",
    "202 Oakdale Drive, Aptos",
    "947 Windsor St, Santa Cruz, CA",
    "22980 E Cliff Dr, Santa Cruz",
    "1750 41st Ave Capitola",
    "1343 Greenborough Dr, Roseville, CA",
    "5665 Montclair circle, Rocklin, CA",
    "112 Earl Avenue, Roseville, ca"
]
fake_test_cases=[
        "1234 Sesame Street, Fakeland, Oregon, 09876",
        "412 Olive St, Santa Cruz, CA 95060",
        "203 Oakdale Drive, Aptos",
        "3242 Crystal Heights Drive, Soquel, CA, 95073",
        "113 Earl Avenue, Roseville, ca"
]
# for test_case in nozip_test_cases:
#     print(verify(test_case))
print(verify("7 mile"))
print("ekans")
=======
def verify(address):
    notFound=False #returned generic state or city, usually means street address is considerably off
    verified=simple_get("https://www.google.com/maps/search/" + address)
    #print(verified)
    if "]" in verified[0]:
        verified="No Results"
    if not any(char.isdigit() for char in verified[0]):
        notFound=True
    verified.append(notFound)
    #print(verified)
    return verified
>>>>>>> Stashed changes

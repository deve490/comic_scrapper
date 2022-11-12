import requests
from bs4 import BeautifulSoup



def catalog(url =  "https://vercomicsporno.xxx/"):

    # Making a GET request
    r = requests.get(url)
    
    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')
    
    images_list = []
    
    divs_tag = soup.find_all("div", class_ = "c-blog_item")

    #print(divs_tag)

    for div  in divs_tag:
        image = div.select('img')[0]
        src = image.get('src')
        alt = image.get('alt')
        alb = div.find("a")
        images_list.append({"src": str(src), "alt": str(alt), "tittle": alb.attrs["title"], "href": alb.attrs["href"]})

    return images_list



def getSources(url):
    # Making a GET request
    r = requests.get(url)
    
    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')
    
    images_list = []
    
    divs_tag = soup.find_all("div", class_ = "wp-block-image")

    #print(divs_tag)

    for div  in divs_tag:
        image = div.select('img')[0]
        src = image.get('src')
        alt = image.get('alt')

        images_list.append({"src": str(src), "alt": str(alt)})

    return images_list
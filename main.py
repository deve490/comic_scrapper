
from flask import Flask, Response, request
import requests
from services import catalog, getSources

app = Flask("app")


@app.get("/")
def inedex():
    try:
        url = request.query_string.decode().split("value__=")[1]
        return catalog(url)
    except:
        return catalog()

    
@app.get("/source")
def getCatalog():
    try:
        url = request.query_string.decode().split("value__=")[1]
        resp = {
            "resources" : getSources(url),
            "catalog" : catalog(url)
        }
        return resp
    except:
        return "ERRROR", 400

@app.get("/image")
def img():
    url = request.query_string.decode().split("value__=")[1]
    r = requests.get(url)
    contennt = r.content
    r.close()
    return Response( contennt, mimetype=f"image/png")

if __name__ == "__main__":
    app.run(port=8001, debug=True)
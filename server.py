from flask import Flask
from flask import request
import json
import glob
from main import fonveri_guncelle
import socket


def internet_check(host="8.8.8.8", port=53, timeout=3): #check internet connection with googles DNS server
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        return False


while not internet_check():
    continue


fonveri_guncelle()
app = Flask(__name__)


def get_actions():
    returnVal = []
    for file in glob.glob("D:\\phyton\\scrap\\webscrapping\\*.json"):
        returnVal = file

    return returnVal


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        file_name = get_actions()
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
            returnVal = json.dumps(data["data"])
        return returnVal
    else:
        return '404'


if __name__ == "__main__":
    app.run(host='localhost', port='43560', debug=False)
import requests
from bs4 import BeautifulSoup
import json
import os
import time
import glob

def fonveri_guncelle():
    #timetoday = "17.01.2025"
    timetoday = time.strftime("%d.%m.%Y")
    URL = 'https://www.tefas.gov.tr/FonAnaliz.aspx?FonKod='
    URL2 = 'https://www.tefas.gov.tr/api/DB/BindHistoryInfo/'

    headers = {
        "User-Agent":
            ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"),
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Origin": "https://www.tefas.gov.tr",
        "Referer": "https://www.tefas.gov.tr/TarihselVeriler.aspx"
    }
    data = {
        "fontip": "YAT",
        "sfontur": "",
        "fonkod": "",
        "fongrup": "",
        "bastarih": timetoday,
        "bittarih": timetoday,
        "fonturkod": "",
        "fonunvantip": "",
    }
    r = requests.post(URL2, headers=headers, data=data)

    #print(r.text)

    soup = BeautifulSoup(r.content, 'html.parser') # If this line causes an error, run 'pip install html5lib' or install html5lib
    str_ = soup.prettify()
    str_tojson = json.loads(str_)

    fonverisi_okundumu = 1
    if str_tojson["recordsTotal"] == 0:
        #print("Fon verisi okunamadı!!")
        fonverisi_okundumu = 0

    if fonverisi_okundumu:
        for file in glob.glob('D:\\phyton\\scrap\\webscrapping\\*.json'):
            os.remove(file)

        with open('D:\\phyton\\scrap\\webscrapping\\'+timetoday+'_fon.json', 'w', encoding='utf-8') as f:
            json.dump(str_tojson, f, ensure_ascii=False, indent=4)


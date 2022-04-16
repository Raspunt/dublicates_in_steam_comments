import steamreviews
import json
import re
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from dbCon import reviewsDb
import time


request_params = dict()
url = "https://steamid.io/lookup/"



revDb = reviewsDb()

revDb.create_table()



def download_steam_reviews():
    app_id =  [1085660]
    steamreviews.download_reviews_for_app_id_batch(app_id)



def parse_SteamJson():

    f = open("data/review_1085660.json")
    data = json.load(f)

    comment_ids = []

    for line in data['reviews']:
        comment_ids.append(line)


    for comment_id in comment_ids:


        

        steamId = data['reviews'][comment_id]["author"]["steamid"]
        timestamp = data['reviews'][comment_id]["timestamp_created"]
        language = data['reviews'][comment_id]["language"]
        review = data['reviews'][comment_id]["review"]


        dt = datetime.fromtimestamp(timestamp)

        formated_dt = f"{dt.hour}:{dt.minute}:{dt.second} {dt.day}.{dt.month}.{dt.year}"


        username = steamid_to_username(steamId)


        print("\n")
        print(username)
        print(formated_dt)
        print(language)
        print(review)

        revDb.insert_rewiews(f"{username} {steamId}",formated_dt,language,review)

        # print(full_steamId)



def steamid_to_username(steamid):
    print(url+steamid)
    time.sleep(1) # иногда возвращает пустую строку. ждем конца прошлый запрос
    r = requests.get(url=url+steamid)

    soup = BeautifulSoup(r.text, "html.parser")
    count = 0
    rword = ""

    for dd in soup.find_all('dd'):
        count = count + 1

        if count==7:
            
            word = re.findall(">.+<",str(dd))
            word = str(word).replace("<","").replace(">","").replace("['","").replace("']","")
            rword = word


    return rword


parse_SteamJson()

# print(steamid_to_username("76561198978157802"))




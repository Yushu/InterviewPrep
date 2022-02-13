from urllib.request import urlopen
import json
def solution(stations):
    d1 = {}
    d2 = {}
    url1='http://transportapi.com/v3/uk/places.json?query='
    url2="&type=train_station&app_id=ae6d5a90&app_key=5c6b8d92f7c423c588ab1ef7a03c1bce"
    stations = [x.lower().replace(" ", "+") for x in stations]
    for i in stations:
        url = (url1+i+url2)
        #print(json.load(urlopen(url))["member"][0])
        output = json.load(urlopen(url))["member"]
        d1[i] = [output[0]['latitude'], output[0]['longitude']]
    temp = []
    for i in range(len(stations) - 1):
        for j in range(i+1, len(stations)):
            temp += [((d1[stations[i]][0] - d1[stations[j]][0])**2 + (d1[stations[i]][1] - d1[stations[j]][1])**2)**(0.5)]
    return min(temp)
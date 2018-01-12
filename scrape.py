import json
import urllib
from time import sleep
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 \
    as Features

url1 = "https://www.googleapis.com/customsearch/v1?key=AIzaSyAlzkqHjDj7mHkWQvnE0IThbKYkmf3cdCc&cx=007531734862368908526:wwmdlctwpp4&q=kkr+vs+mi+ipl+2017+match+7+9th+april+2017"
url2 = "https://www.googleapis.com/customsearch/v1?key=AIzaSyAlzkqHjDj7mHkWQvnE0IThbKYkmf3cdCc&cx=007531734862368908526:wwmdlctwpp4&q=kkr+vs+mi+ipl+2017+match+7+9th+april+2017&start=11"
url3 = "https://www.googleapis.com/customsearch/v1?key=AIzaSyAlzkqHjDj7mHkWQvnE0IThbKYkmf3cdCc&cx=007531734862368908526:wwmdlctwpp4&q=kkr+vs+mi+ipl+2017+match+7+9th+april+2017&start=21"
url4 = "https://www.googleapis.com/customsearch/v1?key=AIzaSyAlzkqHjDj7mHkWQvnE0IThbKYkmf3cdCc&cx=007531734862368908526:wwmdlctwpp4&q=kkr+vs+mi+ipl+2017+match+7+9th+april+2017&start=31"
url5 = "https://www.googleapis.com/customsearch/v1?key=AIzaSyAlzkqHjDj7mHkWQvnE0IThbKYkmf3cdCc&cx=007531734862368908526:wwmdlctwpp4&q=kkr+vs+mi+ipl+2017+match+7+9th+april+2017&start=41"
url6 = "https://www.googleapis.com/customsearch/v1?key=AIzaSyAlzkqHjDj7mHkWQvnE0IThbKYkmf3cdCc&cx=007531734862368908526:wwmdlctwpp4&q=kkr+vs+mi+ipl+2017+match+7+9th+april+2017&start=51"
url7 = "https://www.googleapis.com/customsearch/v1?key=AIzaSyAlzkqHjDj7mHkWQvnE0IThbKYkmf3cdCc&cx=007531734862368908526:wwmdlctwpp4&q=kkr+vs+mi+ipl+2017+match+7+9th+april+2017&start=61"
url8 = "https://www.googleapis.com/customsearch/v1?key=AIzaSyAlzkqHjDj7mHkWQvnE0IThbKYkmf3cdCc&cx=007531734862368908526:wwmdlctwpp4&q=kkr+vs+mi+ipl+2017+match+7+9th+april+2017&start=71"
url9 = "https://www.googleapis.com/customsearch/v1?key=AIzaSyAlzkqHjDj7mHkWQvnE0IThbKYkmf3cdCc&cx=007531734862368908526:wwmdlctwpp4&q=kkr+vs+mi+ipl+2017+match+7+9th+april+2017&start=81"
url10 = "https://www.googleapis.com/customsearch/v1?key=AIzaSyAlzkqHjDj7mHkWQvnE0IThbKYkmf3cdCc&cx=007531734862368908526:wwmdlctwpp4a&q=kkr+vs+mi+ipl+2017+match+7+9th+april+2017&start=91"

resp1= urllib.urlopen(url1).read()
print ('done1')
resp2= urllib.urlopen(url2).read()
print ('done2')
resp3= urllib.urlopen(url3).read()
print ('done3')
resp4= urllib.urlopen(url4).read()
print ('done4')
resp5= urllib.urlopen(url5).read()
print ('done5')
resp6= urllib.urlopen(url6).read()
print ('done6')
resp7= urllib.urlopen(url7).read()
print ('done7')
resp8= urllib.urlopen(url8).read()
print ('done8')
resp9= urllib.urlopen(url9).read()
print ('done9')
resp10= urllib.urlopen(url10).read()
print ('done10')


jsonResp1= json.loads(resp1)
jsonResp2= json.loads(resp2) 
jsonResp3= json.loads(resp3)
jsonResp4= json.loads(resp4)
jsonResp5= json.loads(resp5)
jsonResp6= json.loads(resp6)
jsonResp7= json.loads(resp7)
jsonResp8= json.loads(resp8)
jsonResp9= json.loads(resp9)
jsonResp10= json.loads(resp10)

jsonResps=[jsonResp1, jsonResp2,jsonResp3,jsonResp4, jsonResp5,jsonResp6,jsonResp7, jsonResp8,jsonResp9,jsonResp10]


done=0

for i in jsonResps:
    items=i["items"]
    #print i
    for j in items:
        done+=1
        print (done)
        link=j["link"]
        natural_language_understanding = NaturalLanguageUnderstandingV1(
        username="0a780fa1-f63d-4ea7-967f-1ef07af94c67",
        password="02ODWkVtSuEc",
        version="2017-02-27")

        response = natural_language_understanding.analyze(url=str(link), features=[Features.Keywords(emotion=True,limit=1)], return_analyzed_text="true")
        print(response)

        #print(alchemyRes["text"].encode('utf8'))
        file_object=open(str(done)+ '.html', 'w')
        file_object.write(response["analyzed_text"].encode('utf8'))
        file_object.close()
    sleep(1.5)



import os.path

import requests
import json
import csv
def setHeroCsv(url='https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2747878'):
    headers={
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39"
    }
    respone=requests.get(url,headers=headers)
    text=respone.text
    lst=json.loads(text)['hero']
    with open('doc/lol.csv','w',newline='') as csvfile:
        fieldnames=["index",'heroId','name','title','goldPrice','keywords','mainImg']
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()
        for index,hero_item in enumerate(lst):
            if not os.path.exists(f"lol_pic/{hero_item['heroId']}"):
                os.mkdir(f"lol_pic/{hero_item['heroId']}")
            writer.writerow({
                "index": f"0{index+1}"  if (index+1)<10 else  f"0{index+1}",
                "heroId": hero_item['heroId'],
                "name": hero_item['name'],
                "title": hero_item['title'],
                "goldPrice": hero_item['goldPrice'],
                "keywords": hero_item['keywords'] or hero_item['title']
            })
            mainImgDict=setHeroHero(hero_item['heroId'])

            for k in mainImgDict:
                for item in mainImgDict[k]:
                    pic_data = requests.get(item['mainImg'],headers=headers).content
                    with open(f"lol_pic/{hero_item['heroId']}/{item['name']}.jpg", mode='wb') as f:
                        f.write(pic_data)
            print('下载完成')
def setHeroHero(id=1):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39"
    }
    resource = requests.get(f'https://game.gtimg.cn/images/lol/act/img/js/hero/{id}.js?ts=2747886', headers=headers)
    text = resource.text
    lst = json.loads(text)['skins']
    mainImgDict={}
    mainImgDict[id] = []
    for index,item in enumerate(lst):
        if(item['mainImg']):
            # end=item['mainImg'].split('/')[-1].split('.')
            # print(item['mainImg'])
            # replace= str(end[0]).replace(end[0],item['name']+'.'+end[1])
            #str(end[0]).replace(end[0],item['name']+'.'+end[1]),item['mainImg'],item['name']

            mainImgDict[id].append({'mainImg':item['mainImg'],'name':item['name']})
    return mainImgDict
  
setHeroCsv()

import requests
import json
from requests.cookies import RequestsCookieJar




url=r"https://api.xueqiu.com/provider/oauth/token"

data={"client_id":"JtXbaMn7eP",
      "client_secret":"txsDfr9FphRSPov5oQou74",
      "grant_type":"password",
      "telephone":"18222703032",
      "areacode":"86",
      "password":"yuxiyan12"
      }
headers={"user-Agent":"Xueqiu Android 12.6.1",
        "Accept-Language":"en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        }


r= requests.post(url,headers=headers,data=data)
result=json.loads(r.content.decode())
cookies=r.cookies
print(cookies)

#print(result)
access_token=result['access_token']
id_token=result["id_token"]
uid=str(result["uid"])






url1 =r"https://stock.xueqiu.com/v5/stock/portfolio/list.json"

#cookie_jar=RequestsCookieJar()
#cookie_jar.set("access_token",access_token)
#cookie_jar.set("u",uid)
cookies={'xq_a_token':access_token,'u':uid}
print(cookies)

data={"category":1
      }
headers={
        "user-Agent":"Xueqiu Android 12.6.1",
        "Accept-Language":"en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        }
r1= requests.get(url1,headers=headers,data=data,cookies=cookies)

print(r1.content.decode())


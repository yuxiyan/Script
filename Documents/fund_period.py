

import requests


result_id_list = []



#批量上传卡片配置
def diff_period(symbol,day):
    for key,value in symbol.items():
        #print (key,int(value))
        headers = {
            'Accept': "application/json, text/plain, */*",
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': "username=yuxiyan; wid=undefined; xq_crm_token=6cda63987703812d8d4696446bb09b7c; _ga=GA1.2.1856906410.1590054992; experimentation_subject_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6IklqSmxPVFpsWXpSaUxUVTNZVFl0TkRNeE9TMWhPR1F6TFRReFkyTmpNVEl4TURFME15ST0iLCJleHAiOm51bGwsInB1ciI6ImNvb2tpZS5leHBlcmltZW50YXRpb25fc3ViamVjdF9pZCJ9fQ%3D%3D--17fb7a9946509732afce2e8e04b21ab1bafcc3aa",
            'Content-Length': '779',
            "Accept-Language": "zh-cn",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15",
            'Accept-Encoding': 'gzip,deflate'

        }
        for day_period in day:
            #print(int(day_period))
            body = {

                "card_name": "测试场外基金",
                "type": value,
                "symbol":key,
                'day': day_period,
                'slogan': "测试场外基金F008975",
                'notice': "测试场外基金公告测试测测试场外基金公告测试测试测试场外基金公告测试测试测试场外基金公告测试测试试",
                'notice_link': "http://static.cninfo.com.cn/finalpage/2020-08-03/1208116587.PDF",
                'weight': 10,
                'start_time': 1596432049011,
                'end_time': 1600924849011,
                'uid': 3029025214,
                'state': 0,

            }
            url_post = 'http:****/internal/lightsnow/card/update.json'
            rqs = requests.post(url=url_post, headers=headers, data=body)
            print(rqs.text)
            get_nav()




#获取卡片配置
def get_nav():
    get_headers = {
        'User-Agent': 'Xueqiu iPhone 11.8',
        'accept': 'application/json',
        'ept-language': 'zh-Hans-CN;q=1',
        'accept-encoding': 'br, gzip, deflate',
        'Cookie': 'u=1970552355; xq_a_token=XqTest04df0d006155d3d69c6e01106b0be706bf53f735'
    }
    url_get = "https://*****/snowpard/card/query.json?uid=3029025214"
    rqs1 = requests.get(url=url_get, headers=get_headers, timeout=1).json()
    print(rqs1)


    for result_nav in rqs1['data']['items']:

        #if result_nav['nav']==0:
        print('id=%s,symbol=%s,type=%s,day=%s,day_name=%s,nav=%s'%(result_nav['id'],result_nav['symbol'],result_nav['type'],result_nav['day'],result_nav['day_name'],result_nav['nav']))
        result_id_list.append(result_nav['id'])

    print(result_id_list)



#根据uid批量删除卡片配置

def del_user(id_list):


    for sid in id_list:

        post_headers = {
            'User-Agent': 'Xueqiu iPhone 11.8',
            'accept': 'application/json',
            'ept-language': 'zh-Hans-CN;q=1',
            'accept-encoding': 'br, gzip, deflate',
            'Cookie': 'u=1970552355; xq_a_token=XqTest04df0d006155d3d69c6e01106b0be706bf53f735'
        }
        body={
            'id':sid,
            'uid':'3029025214'
              }
        url_post = "http://****/internal/lightsnow/card/delete.json"
        rqs1 = requests.post(url=url_post, headers=post_headers,data=body)




if __name__ == '__main__':
    result_id_list = []
    symbol={'CSI1014':'1','F008264':'0','SZ150284':'0','F168601':'0'}
    day=[1,7,30,90,180,360,720,1080,1800,-1]
    diff_period(symbol, day)
    print(result_id_list)
    del_user(result_id_list)


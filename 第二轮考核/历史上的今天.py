import requests,logging

mon = 1

headers_UA = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69'
}

def scrape_get(url,params={},headers= {}):
    logging.info('正在爬取%s',url)
    try:
        response = requests.get(url,params =params,headers=headers)
        if response.status_code == 200:
            print('爬取%s正常'%url)
            response.encoding='utf-8'
            return response
        logging.error('爬取%s网页时得到%s状态码',url,response.status_code)
    except:
        logging.error('爬取%s网页时出现错误',url)
        return ''


import pymysql,re
db = pymysql.connect(host='localhost',user = 'root',password='996931',port=3306,db='baidu')
cursor = db.cursor()
re_ = '(</?a.*?>)'

def dellink(s):
            dl = re.findall('%s'%(re_),s,re.S)#[(),()]
            for i in dl:#('','')
                for j in i:
                    s = s.replace('%s'%(j),'')
            return s


#数据量太大，只爬前三个月，后几个月的同理
for mon in range(1,4):
    ur = 'https://baike.baidu.com/cms/home/eventsOnHistory/%02d.json?_='%mon
    rp = scrape_get(url = ur,headers=headers_UA)
    jsbk = rp.json()
    for i in jsbk:
        #i是月份
        for j in jsbk[i]:#j是日期
            data = jsbk[i][j]#data是每天的数据，列表形式
            for event in data:
                year = event['year']
                title = dellink(event['title'])
                type_ = event['type']
                desc = dellink(event['desc']) 
                table = '%s历史上的今天'%(i)
                sql = """INSERT INTO %s(日期, 年份, 事件类型, 标题, 简要内容) VALUES ('%s', '%s', '%s', '%s', '%s');"""%(table,j,year,type_,title,desc)
                try:
                    cursor.execute(sql)
                    db.commit()
                except:
                    pass


print('存储完成')
db.close()


import requests,logging,time,pymysql
from lxml import etree
base_url = 'https://jwch.fzu.edu.cn/'
url1 = 'https://jwch.fzu.edu.cn/jxtz.htm'
url2 = 'https://jwch.fzu.edu.cn/jxtz/'
headers_UA = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69'
}
num=0
page = 183
l=[0]

def scrape_page_get(url,params={},headers= {}):
    logging.info('正在爬取%s',url)
    try:
        response = requests.get(url,params =params,headers=headers)
        if response.status_code == 200:
            response.encoding='utf-8'
            return response.text
        logging.error('爬取%s网页时得到%s状态码',url,response.status_code)
    except:
        logging.error('爬取%s网页时出现错误',url)
        return ''

def parse(html,atr,xpath1,xpath2=''):
    '''
    给定html文档和xpath格式
    '''
    global l,num,page,base_url#num是总通知序号
    html=etree.HTML(html)
    count=1
    for number in range(1,21):#number是每个页面内的序号
        try:
            result = html.xpath(xpath1)[number-1].text.strip()
        except:
            result = html.xpath(xpath1)[number-1].strip()
        
        if xpath1=='//ul[@class="list-gl"]/li/text()':
            result = html.xpath(xpath1)[1+3*(number-1)].strip()

        try:
            if result[0]=='.':
                pre_url=result[2:]
                result=f'{base_url}{pre_url}'
            elif result[0:4]=='info':
                pre_url=result
                result=f'{base_url}{pre_url}'
        except:
            pass
        

        if not result:
            #print('格式1未找到，使用格式2第%d次'%(count))
            result = html.xpath(xpath2)[count-1].text.strip()
            count+=1 #count是格式2第count次使用
        
        try:#给有序列表中的字典增加键值对

            l[20*(page-183)+number][atr]=result
        
        except:#新建字典，序号加一，且创建键值对
            num+=1
            l.append({'序号':num})
            l[num][atr]=result
        
xpath = {
    'time_xpath' : '//ul[@class="list-gl"]/li/span',
    'time_xpath2' : '//ul[@class="list-gl"]/li/span/font',
    'header' : '//ul[@class="list-gl"]/li/a',
    'url':'//ul[@class="list-gl"]/li/a/@href',
    'anous':'//ul[@class="list-gl"]/li/text()',
    'append_name':'//ul[@style="list-style-type:none;"]/li/a',
    'append_time':'//ul[@style="list-style-type:none;"]/li/span',
    'append_url':'//ul[@style="list-style-type:none;"]/li/a/@href'
}
r = scrape_page_get(url1,headers=headers_UA)

parse(r,'时间',xpath['time_xpath'],xpath['time_xpath2'])
parse(r,'标题',xpath['header'])
parse(r,'链接',xpath['url'])
parse(r,'通知人',xpath['anous'])


for i in range(1,5):
    url_page=f'{url2}{page}.htm'
    
    r = scrape_page_get(url_page,headers=headers_UA)
    page+=1
    parse(r,'时间',xpath['time_xpath'],xpath['time_xpath2'])
    parse(r,'标题',xpath['header'])
    parse(r,'链接',xpath['url'])
    parse(r,'通知人',xpath['anous'])

def parse2(html,atr,xpath):#爬取附件相关
    global l,i
    try:
        html=etree.HTML(html)
    except:
        pass
    result=''
    try:
        result = html.xpath(xpath)[0].text.strip()
    except:
        try:
            result = html.xpath(xpath)[0].strip()
        except:
            pass
    
    try:
        if result[1]=='s':
            result = 'https://jwch.fzu.edu.cn' + result
    except:
        pass
    
    if not result:#没有附件则跳过
        pass
    else :
        l[i][atr]=result
    

for i in range(1,101):
    r = scrape_page_get(l[i]['链接'],headers=headers_UA)
    parse2(r,'附件名',xpath['append_name'])
    parse2(r,'附件下载次数',xpath['append_time'])
    parse2(r,'附件链接',xpath['append_url'])
    time.sleep(0.03)

#print(l)

db = pymysql.connect(host='localhost',user = 'root',password='996931',port=3306,db='fzujwc')
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
for i in l[1:]:

    if i.get('附件名'):
        sql = """INSERT INTO 教务处通知
            (序号,时间,标题,链接,通知人,附件名,附件链接)
            VALUES
            (%d, '%s', '%s', '%s', '%s', '%s', '%s')"""%(i['序号'],i['时间'],i['标题'],i['链接'],i['通知人'],i['附件名'],i['附件链接'])
    else:
        sql = """INSERT INTO 教务处通知
            (序号,时间,标题,链接,通知人)
            VALUES
            (%d, '%s', '%s', '%s', '%s')"""%(i['序号'],i['时间'],i['标题'],i['链接'],i['通知人'])

    cursor.execute(sql)
    db.commit()
db.close()


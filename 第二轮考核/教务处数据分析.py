import numpy,pandas,pymysql
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']

db = pymysql.connect(host='localhost',user = 'root',password='996931',port=3306,db='fzujwc')
cursor = db.cursor()

def dltimes_an():
    '''分析通知人与下载次数的关系'''
    sql = 'select 通知人,下载次数 from 教务处通知 where 下载次数;'
    df = pandas.read_sql(sql,con=db)
    
    average_downloads = df.groupby('通知人')['下载次数'].mean()
    print('不同通知人的附件平均下载次数\n',average_downloads)
    average_downloads.plot(kind='bar', title='不同通知人的附件平均下载次数')
    plt.xlabel('通知人')
    plt.ylabel('平均下载次数')
    plt.show()
    input() 
    
    median_downloads = df.groupby('通知人')['下载次数'].median()
    print('不同通知人的附件下载次数中位数\n',median_downloads)
    median_downloads.plot(kind='bar', title='不同通知人的附件下载次数中位数')
    plt.xlabel('通知人')
    plt.ylabel('下载次数中位数')
    plt.show()
    input() 
    
    max_downloads = df.groupby('通知人')['下载次数'].max()
    print('不同通知人的附件下载次数最大值\n',max_downloads)
    max_downloads.plot(kind='bar', title='不同通知人的附件下载次数最大值')
    plt.xlabel('通知人')
    plt.ylabel('下载次数最大值')
    plt.show()
    
def everyday_times():
    '''分析每天的通知数'''
    sql = 'select 日期 from 教务处通知 ;'
    df = pandas.read_sql(sql, con=db)
    df['日期'] = pandas.to_datetime(df['日期'])
    date_counts = df.groupby('日期').size()
    print(date_counts)
    input()
    date_counts.plot(title='日期密集度')
    plt.xlabel('日期')
    plt.ylabel('出现次数')
    plt.show()


dltimes_an()
input()
everyday_times()
db.close()
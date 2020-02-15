#！ /usr/bin/env python
#  -*- coding: utf-8 -*-
# __author__:"yestolife"
# github:https://github.com/yestolife
import schedule#用于定时任务
from os import getcwd#用于获取文件所在目录
from load_data import load_data_fun#自编函数，用于数据获取
from plot_data import plot_data_fun#自编函数，用于数据可视化
from merge_pdfs import merge_pdf_fun#自编函数，用于合并pdf文件
from sendemail import send_email_fun#自编函数，用于发送邮件

def job():#设置任务
    data_infos = {"China":load_data_fun(url_cn), "JiangXi":load_data_fun(url_jx), "HuBei":load_data_fun(url_hb)}#获取全国、江西、湖北数据
    plot_data_fun(data_infos)#数据可视化
    merge_pdf_fun(getcwd(), "nCov_Data.pdf")#合并pdf文件
    send_email_fun()#发送邮件

if __name__ == '__main__':
    schedule.every().day.at('05:00').do(job)#设置定时任务，每天执行一次job
    #schedule.every(1).minutes.do(job)#设置定时任务，每分钟执行一次job
    url_cn = "https://lab.ahusmart.com/nCoV/api/overall?latest=0"#全国数据获取的url
    url_jx = "https://lab.ahusmart.com/nCoV/api/area?province=江西省&latest=0"#江西数据获取的url
    url_hb = "https://lab.ahusmart.com/nCoV/api/area?province=湖北省&latest=0"#湖北数据获取的url
    while True:
        schedule.run_pending()#启动定时任务



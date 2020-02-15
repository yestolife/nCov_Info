#！ /usr/bin/env python
#  -*- coding: utf-8 -*-
# __author__:"yestolife"
# github:https://github.com/yestolife

import requests
import json
import time
#从接口地址url导入数据，返回数据字典
def load_data_fun(url):
    #从接口地址获取数据，将文本导出为json格式处理
    r = requests.get(url)
    data_json=json.loads(r.text)
    #确诊人数、疑似人数、治愈人数、死亡人数、日期按列表存储
    data_confirmedCount_list = []
    data_suspectedCount_list = []
    data_curedCount_list = []
    data_deadCount_list = []
    data_time_list = []
    #遍历一遍json格式的数据，取出关心的数据
    for data_dic in data_json['results']:
        time_data=time.strftime("%Y-%m-%d", time.gmtime(data_dic['updateTime'] // 1000)) #获得格式化的日期
        if len(data_time_list) == 0 :#如果日期列表为空，则表明是访问第一个元素
            data_time_list.append(time_data)
            data_confirmedCount = data_dic['confirmedCount']
            data_suspectedCount = data_dic['suspectedCount']
            data_curedCount = data_dic['curedCount']
            data_deadCount = data_dic['deadCount']
        elif time_data in data_time_list:#如果日期已经在日期列表中了，说明json数据在该日期下保存了多条数据，更新数据至日期的最新
            data_confirmedCount = data_dic['confirmedCount']
            data_suspectedCount = data_dic['suspectedCount']
            data_curedCount = data_dic['curedCount']
            data_deadCount = data_dic['deadCount']
            continue
        else:#如果日期不在日期列表中，则说明是访问了新的日期数据，将上一条最新的数据添加至存储列表中
            data_time_list.append(time_data)
            data_confirmedCount_list.append(data_confirmedCount)
            data_suspectedCount_list.append(data_suspectedCount)
            data_curedCount_list.append(data_curedCount)
            data_deadCount_list.append(data_deadCount)
    data_confirmedCount_list.append(data_confirmedCount)#由于最后一条数据后面没有日期更新了，在循环中未添加至存储列表，所以推出循环时添加
    data_suspectedCount_list.append(data_suspectedCount)
    data_curedCount_list.append(data_curedCount)
    data_deadCount_list.append(data_deadCount)
    #将各数据存储列表组合为字典返回
    data_info = {"confirmedCount":data_confirmedCount_list, "suspectedCount":data_suspectedCount_list,
                 "curedCount":data_curedCount_list, "deadCount":data_deadCount_list,"date":data_time_list}
    return data_info
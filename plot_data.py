#！ /usr/bin/env python
#  -*- coding: utf-8 -*-
# __author__:"yestolife"
# github:https://github.com/yestolife

#数据可视化，将数据绘制为折线图，并保存为svg和pdf格式
import pygal
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

def plot_data_fun(data_infos):
    for key, value in data_infos.items():#读取将要展示的数据
        line_chart = pygal.Line(x_label_rotation=20)#创建折线图及配置
        line_chart.title = key + '_nCov_Data'
        line_chart.x_labels = value["date"]
        line_chart.add('confirmedCount', value["confirmedCount"])
        line_chart.add('suspectedCount', value["suspectedCount"])
        line_chart.add('curedCount', value["curedCount"])
        line_chart.add('deadCount', value["deadCount"])
        line_chart.render_to_file(line_chart.title+".svg")#折线图出为svg格式
        drawing = svg2rlg(line_chart.title+".svg")#svg图转换为pdf格式
        renderPDF.drawToFile(drawing, line_chart.title+".pdf")
    print("图像绘制完成")

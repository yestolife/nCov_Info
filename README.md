# Python实现疫情信息订阅

**综述**：2020年初湖北疫情爆发，获取信息成为了关键，而铺天盖地的疫情数据信息让人难以分辨。本案例主动从公开数据接口获取数据，进行处理可视化展现后，每日发送邮件至订阅邮箱，避免刷新闻、刷微博的信息焦虑，主动获取自己想要的信息。案例中综合应用python爬虫、数据处理、数据可视化、pdf操作、邮件操作等方面，串联相关的各类python常用库，可帮助熟练使用这些工具。

## 一，实验环境

本地测试使用：Windows10系统，Python3.7.4

## 二，实验思路

1.从公开疫情数据接口获取相关数据；

2.进行数据分析处理；

3.绘制数据分析结果；

4.保存可视化展示结果至pdf；

5.每日定时讲分析结果pdf通过邮件发送给自己邮箱；

## 三，实验过程

1.数据获取

可以搜索到比较多的数据源接口，比如天行数据的[数据接口](https://www.tianapi.com/apiview/169)，有在线测试接口，使用起来非常方便。但是json中的字段时常变动，无法在代码中固定下来。还有手工做爬虫获取数据的[案例](https://blog.csdn.net/xufive/article/details/104093197)，如果网站做了反爬虫或者网站内容做了变更，容易失效。还有爬取丁香园的数据，并记录了时序数据的，如github上的[案例](https://github.com/hack-fang/nCov/blob/master/API.md)。我们就用这个github上的数源做实验。测试过程中返回的json数据可使用在线浏览[工具](http://www.kjson.com/jsonparser/?f=1)查看数据的结构，以便编写代码。查看案例中的说明，很容易编写处获取数据的测试代码，如下：

```python
import requests
import json

url = "https://lab.ahusmart.com/nCoV/api/area?province=江西省&latest=0"
r = requests.get(url)
print(r.status_code)

print(json.loads(r.text))
```

返回结果如下：

```json
200
{'results': [{'country': '中国', 'provinceName': '江西省', 'provinceShortName': '江西', 'confirmedCount': 900, 'suspectedCount': 0, 'curedCount': 187, 'deadCount': 1, 'cities': [{'cityName': '南昌', 'confirmedCount': 217, 'curedCount': 68, 'currentConfirmedCount': 149...
```

200表示返回成功，json格式的数据是返回当日江西省各地市确诊人数、疑似人数（这个数据貌似已经不使用了）、治愈人数和死亡人数。

2.数据分析

从接口获取的数据比较规范，无需做数据预处理，所以就直接拉去我关心的地区数据进行处理。我比较关心全国、武汉市、江西省这几个区域的历史和当日数据。json数据中的时间使用UNIX时间戳，可通过在线[工具](https://unixtime.51240.com/)查看。具体代码查看load_data.py

3.数据展示

使用Pygal库很方便地展示数据，并生成可放缩的矢量图形svg，可以在不同尺寸的屏幕上显示。可参考《Python编程从入门到实践》中P329的案例。具体代码查看plot_data.py。

4.转换pdf

使用svglib和reportlab库将数据可视化生成的svg图像可转换为pdf，[参考](https://stackoverflow.com/questions/5835795/generating-pdfs-from-svg-input)。但是这个方法对中文现实无法转换。具体代码查看plot_data.py。最后将生成的多个pdf文件合并为一个pdf，[参考](https://www.jianshu.com/p/82485e3e46e1)和merge_pdfs.py

5.发送邮件

使用smtplib和email库将前面生成的pdf文件作为邮件附件发送到订阅邮箱，可以参考这篇[文章](https://www.runoob.com/python/python-email.html)。具体代码查看sendemail.py。







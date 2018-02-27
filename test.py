#coding=utf-8
import xml.dom.minidom
import xlwt
import time

#打开xml文档
dom = xml.dom.minidom.parse('task log.xml')
root = dom.documentElement
w = xlwt.Workbook()
ws = w.add_sheet('task log')

test = root.getElementsByTagName('Initialized')
test2 = ['StartTime','EndTime','Turns','PlayerVictory','InGameRank']

for i in range(len(test2)):
    ws.write(0,i,test2[i])

for i in range(len(test)):
    for key in test2:
        tmp = root.getElementsByTagName(key)
        text = tmp[i].firstChild.data
        if key == 'StartTime' or key == 'EndTime':
            abc = tmp[i].firstChild.data[:10]+' '+tmp[i].firstChild.data[11:19]
            text = time.mktime(time.strptime(abc,"%Y-%m-%d %H:%M:%S"))
        if key == 'PlayerVictory':
            if text == 'true':
                text = 1
            else:
                text = 0
        ws.write(i+1,test2.index(key),int(text))
filename = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())+'.xls'
w.save(filename)
print 'success'

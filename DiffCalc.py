#Author: Sam Liu
import csv
import json
import os.path
import statistics
files = os.listdir('H:\\calc') #Change directory here
files=sorted(files, key=lambda x: int(x.split(' ',2)[0]))

HandledCtr=0
data=[]

def CalcAve(ObjProp, data, printfile, printdata):
    List1=[]
    List2=[]
    ave1=0
    ave2=0
    for i in range(1,9,2):
        if printfile:
            print(data[i-1])
        if ObjProp in data[i]:
            if printdata:
                print(ObjProp,data[i][ObjProp])
            List1.append(data[i][ObjProp])
    if len(List1)>0:
        ave1=statistics.mean(List1)
    for i in range(9,17,2):
        if printfile:
            print(data[i-1])
        if ObjProp in data[i]:
            if printdata:
                print(ObjProp,data[i][ObjProp])
            List2.append(data[i][ObjProp])
    if len(List2)>0:
        ave2=statistics.mean(List2)
    return ave2-ave1


    

with open(os.path.join('H:\\', 'diff.csv'), mode='w',newline='') as output: #Change firectory here
    output_writer=csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    output_writer.writerow(['FileName','road','sidewalk', 'building','wall','fence','pole','traffic light','traffic sign','vegetation','terrain','sky','person','rider','car','truck','bus','train','motorcycle','bicycle'])
    for FileName in files:
        with open(os.path.join('H:\\calc', FileName)) as f: #Change firectory here
            data.append(FileName)
            data.append(json.load(f))
        if len(data)==16:
            Name=FileName.split(' ',2)[0]#+' '+(FileName.split(' ',2)[1]).split('_',2)[0]
            print('road Average:',CalcAve('road',data, True, False))
            print('sidewalk Average:',CalcAve('sidewalk',data, False, False))
            print('building Average:,',CalcAve('building',data, False, False))
            print('wall Average:,',CalcAve('wall',data, False, False))
            print('fence Average:,',CalcAve('fence',data, False, False))
            print('pole Average:',CalcAve('pole',data, False, False))
            print('traffic light Average:,',CalcAve('traffic light',data, False, False))
            print('traffic sign Average:,',CalcAve('traffic sign',data, False, False))
            print('vegetation Average:',CalcAve('vegetation',data, False, False))
            print('terrain Average:,',CalcAve('terrain',data, False, False))
            print('sky Average:,',CalcAve('sky',data, False, False))
            print('person Average:,',CalcAve('person',data, False, False))
            print('rider Average:',CalcAve('rider',data, False, False))
            print('car Average:',CalcAve('car',data, False, False))
            print('truck Average:',CalcAve('truck',data, False, False))
            print('bus Average:',CalcAve('bus',data, False, False))
            print('train Average:',CalcAve('train',data, False, False))
            print('motorcycle Average:',CalcAve('motorcycle',data, False, False))
            print('bicycle Average:',CalcAve('bicycle',data, False, False))
            output_writer.writerow([Name,CalcAve('road',data, False, False),CalcAve('sidewalk',data, False, False),CalcAve('building',data, False, False),CalcAve('wall',data, False, False),CalcAve('fence',data, False, False),
                                    CalcAve('pole',data, False, False),CalcAve('traffic light',data, False, False),CalcAve('traffic sign',data, False, False),CalcAve('vegetation',data, False, False),CalcAve('terrain',data, False, False),
                                    CalcAve('sky',data, False, False),CalcAve('person',data, False, False),CalcAve('rider',data, False, False),CalcAve('car',data, False, False),CalcAve('truck',data, False, False),CalcAve('bus',data, False, False),
                                    CalcAve('train',data, False, False),CalcAve('motorcycle',data, False, False),CalcAve('bicycle',data, False, False)])
            data.clear()
            HandledCtr+=1
print('已处理',HandledCtr,'组图片')


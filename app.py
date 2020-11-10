from flask import Flask, render_template

import csv
import json

app = Flask(__name__, static_url_path='/static')

# kakao map api token
with open('secrets.json') as json_file:
    json_data = json.load(json_file)

KAKAO_MAP_API_KEY = json_data["KAKAO_MAP_API_KEY"]


# read smoking level data function
def read_data(data_file, labels, values):
    #time_interval = 46546
    time_interval = 21600

    cnt = 0
    tmp_sum = 0
    total_cnt = 0 # 3600:1시간, 18000:5시간, 21600:6시간, 46546:대략13시간
    
    f = open(data_file, 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        tmp_sum += float(line[1]) # ppm 수치 기준
        cnt += 1
        if cnt==60:
            labels.append(str(int(line[0])//60))
            values.append(str(tmp_sum/60))
            cnt = 0
            tmp_sum = 0
        total_cnt += 1
        if total_cnt==time_interval:
            break
    f.close()
    return


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('map.html', KAKAO_MAP_API_KEY=KAKAO_MAP_API_KEY)

@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/chart_jisun')
def chart_jisun():

    labels = [] # 가로: sec
    values = [] # 세로: ppm
    read_data('static/data/1026_jisun2.txt', labels, values)

    labelss = []
    valuess = []
    read_data('static/data/1027_jisun2.txt', labelss, valuess)

    labelsss = []
    valuesss = []
    read_data('static/data/1028_jisun2.txt', labelsss, valuesss)

    return render_template('chart_jisun.html', values=values, labels=labels, valuess=valuess, labelss=labelss, valuesss=valuesss, labelsss=labelsss)

@app.route('/chart_jeongja')
def chart_jeongja():
    return render_template('chart_jeongja.html')

@app.route('/chart_cheonmak')
def chart_cheonmak():
    return render_template('chart_cheonmak.html')


if __name__ == '__main__':
    app.run()
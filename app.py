from flask import Flask, render_template
import csv

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/chart_jisun')
def chart_jisun():
    #time_interval = 46546
    time_interval = 21600

    labels = [] # 가로: sec
    values = [] # 세로: ppm
    cnt = 0
    tmp_sum = 0
    total_cnt = 0 # 3600:1시간, 18000:5시간, 21600:6시간, 46546:대략13시간
    min_value = 100000000
    max_value = 0
    

    f = open('static/data/1026_jisun2', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        if int(line[2]) < min_value:
            min_value = int(line[2])
        if int(line[2]) > max_value:
            max_value = int(line[2])
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

    labelss = []
    valuess = []
    cnt = 0
    tmp_sum = 0
    total_cnt = 0 # 3600:1시간, 18000:5시간, 21600:6시간, 46546:대략13시간
    min_value = 100000000
    max_value = 0
    f = open('static/data/1027_jisun2', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        if int(line[2]) < min_value:
            min_value = int(line[2])
        if int(line[2]) > max_value:
            max_value = int(line[2])
        tmp_sum += float(line[1]) # ppm 수치 기준
        cnt += 1
        if cnt==60:
            labelss.append(str(int(line[0])//60))
            valuess.append(str(tmp_sum/60))
            cnt = 0
            tmp_sum = 0
        total_cnt += 1
        if total_cnt==time_interval:
            break
    f.close()

    labelsss = []
    valuesss = []
    cnt = 0
    tmp_sum = 0
    total_cnt = 0 # 3600:1시간, 18000:5시간, 21600:6시간, 46546:대략13시간
    min_value = 100000000
    max_value = 0
    f = open('static/data/1028_jisun2.txt', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        if int(line[2]) < min_value:
            min_value = int(line[2])
        if int(line[2]) > max_value:
            max_value = int(line[2])
        tmp_sum += float(line[1]) # ppm 수치 기준
        cnt += 1
        if cnt==60:
            labelsss.append(str(int(line[0])//60))
            valuesss.append(str(tmp_sum/60))
            cnt = 0
            tmp_sum = 0
        total_cnt += 1
        if total_cnt==time_interval:
            break
    f.close()

    min_max = "min value : %d, max value: %d"%(min_value, max_value)
    return render_template('chart_jisun.html', min_max=min_max, values=values, labels=labels, valuess=valuess, labelss=labelss, valuesss=valuesss, labelsss=labelsss)

@app.route('/chart_jeongja')
def chart_jeongja():
    return render_template('chart_jeongja.html')

@app.route('/chart_cheonmak')
def chart_cheonmak():
    return render_template('chart_cheonmak.html')


if __name__ == '__main__':
    app.run()
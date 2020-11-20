from flask import Flask, render_template

import csv
import json

app = Flask(__name__, static_url_path='/static')

# kakao map api token
with open('secrets.json') as json_file:
    json_data = json.load(json_file)

KAKAO_MAP_API_KEY = json_data["KAKAO_MAP_API_KEY"]


# read smoking level data function
def read_data(data_file, labels, values, time_interval):
    cnt = 0
    tmp_sum = 0
    total_cnt = 0 # 3600:1시간, 14400:4시간, 18000:5시간, 21600:6시간, 46546:대략13시간
    
    f = open(data_file, 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        total_cnt += 1
        if total_cnt < 900: # 15분 skip
            continue
        tmp_sum += float(line[1]) # ppm 수치 기준
        cnt += 1
        if cnt==60:
            labels.append(str(int(line[0])//60)) # per minutes
            values.append(str(round(tmp_sum/60, 2))) # ppm
            cnt = 0
            tmp_sum = 0
        if total_cnt==time_interval:
            break
    f.close()
    return

# calculate average
def calc_avg(data_file):
    f = open(data_file, 'r', encoding='utf-8')
    rdr = csv.reader(f)

    total_sum = 0
    total_cnt = 0
    for line in rdr:
        total_cnt += 1
        if total_cnt < 900:
            continue
        total_sum += float(line[1])
    return total_sum/(total_cnt-900)


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

    labels = []
    values = []
    read_data('static/data/jisun2/1026_jisun2.txt', labels, values, 14400)

    labels2 = []
    values2 = []
    read_data('static/data/jisun2/1027_jisun2.txt', labels2, values2, 14400)

    labels3 = []
    values3 = []
    read_data('static/data/jisun2/1028_jisun2.txt', labels3, values3, 14400)

    labels4 = []
    values4 = []
    read_data('static/data/jisun2/1029_jisun2.txt', labels4, values4, 14400)

    labels5 = []
    values5 = []
    read_data('static/data/jisun2/1030_jisun2.txt', labels5, values5, 14400)

    labels6 = []
    values6 = []
    read_data('static/data/jisun2/1031_jisun2.txt', labels6, values6, 14400)

    labels7 = []
    values7 = []
    read_data('static/data/jisun2/1101_jisun2.txt', labels7, values7, 14400)

    return render_template('chart_jisun.html', labels=labels, values=values, labels2=labels2, values2=values2, labels3=labels3, values3=values3, values4=values4, values5=values5, values6=values6, values7=values7)

@app.route('/chart_jeongja')
def chart_jeongja():

    labels = []
    values = []
    read_data('static/data/jeongja2/1026_jeongja2.txt', labels, values, 14400)

    labels2 = []
    values2 = []
    read_data('static/data/jeongja2/1027_jeongja1.txt', labels2, values2, 14400)

    labels3 = []
    values3 = []
    read_data('static/data/jeongja2/1028_jeongja2.txt', labels3, values3, 14400)

    labels4 = []
    values4 = []
    read_data('static/data/jeongja2/1029_jeongja2.txt', labels4, values4, 14400)

    labels5 = []
    values5 = []
    read_data('static/data/jeongja2/1030_jeongja2.txt', labels5, values5, 14400)

    labels6 = []
    values6 = []
    read_data('static/data/jeongja2/1031_jeongja2.txt', labels6, values6, 14400)

    labels7 = []
    values7 = []
    read_data('static/data/jeongja2/1101_jeongja2.txt', labels7, values7, 14400)

    return render_template('chart_jisun.html', labels=labels, values=values, labels2=labels2, values2=values2, labels3=labels3, values3=values3, values4=values4, values5=values5, values6=values6, values7=values7)


@app.route('/chart_cheonmak')
def chart_cheonmak():

    labels = []
    values = []
    read_data('static/data/cheonmak2/1026_cheonmak2.txt', labels, values, 14400)

    labels2 = []
    values2 = []
    read_data('static/data/cheonmak2/1027_cheonmak2.txt', labels2, values2, 14400)

    labels3 = []
    values3 = []
    read_data('static/data/cheonmak2/1028_cheonmak2.txt', labels3, values3, 14400)

    labels4 = []
    values4 = []
    read_data('static/data/cheonmak2/1029_cheonmak2.txt', labels4, values4, 14400)

    labels5 = []
    values5 = []
    read_data('static/data/cheonmak2/1030_cheonmak2.txt', labels5, values5, 14400)

    labels6 = []
    values6 = []
    read_data('static/data/cheonmak2/1031_cheonmak2.txt', labels6, values6, 14400)

    labels7 = []
    values7 = []
    read_data('static/data/cheonmak2/1101_cheonmak2.txt', labels7, values7, 14400)

    return render_template('chart_cheonmak.html', labels=labels, values=values, labels2=labels2, values2=values2, labels3=labels3, values3=values3, values4=values4, values5=values5, values6=values6, values7=values7)


@app.route('/statistics')
def statistics():
    jisun2_avg = calc_avg('static/data/jisun2/1026_jisun2.txt')
    jeongja2_avg = calc_avg('static/data/jeongja2/1026_jeongja2.txt')
    cheonmak2_avg = calc_avg('static/data/cheonmak2/1026_cheonmak2.txt')

    return render_template('statistics.html', jisun2_avg=jisun2_avg, jeongja2_avg=jeongja2_avg, cheonmak2_avg=cheonmak2_avg)


@app.route('/forum')
def forum():
    return render_template('forum.html')


if __name__ == '__main__':
    app.run()
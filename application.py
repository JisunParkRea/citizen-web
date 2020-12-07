from flask import Flask, render_template

import csv
import json

application = Flask(__name__, static_url_path='/static')

# kakao map api token
with open('secrets.json') as json_file:
    json_data = json.load(json_file)

KAKAO_MAP_API_KEY = json_data["KAKAO_MAP_API_KEY"]


# read smoking level data function
def read_data(hours, minutes, data_file, labels, values, time_interval):
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
            #labels.append(str(int(line[0])//60)) # per minutes
            minutes += 1
            if minutes==60:
                hours += 1
                minutes = 0
            labels.append(str(hours)+"시"+str(minutes)+"분")
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

# calculate max value
def calc_max(data_file):
    f = open(data_file, 'r', encoding='utf-8')
    rdr = csv.reader(f)

    total_cnt = 0
    max_value = 0
    for line in rdr:
        total_cnt += 1
        if total_cnt < 900:
            continue
        if float(line[1]) > max_value:
            max_value = float(line[1])
    return str(max_value)



@application.route('/')
def index():
    return render_template('index.html')

@application.route('/map')
def map():
    return render_template('map.html', KAKAO_MAP_API_KEY=KAKAO_MAP_API_KEY)

@application.route('/chart')
def chart():
    return render_template('chart.html')

@application.route('/chart_jisun')
def chart_jisun():
    time_interval = 46546

    labels = []
    values = []
    read_data(7, 30, 'static/data/jisun2/1026_jisun2.txt', labels, values, time_interval)
    before_labels = labels[:240]
    lunch_labels = labels[240:360]
    after_labels = labels[360:]
    before_values1 = values[:240]
    lunch_values1 = values[240:360]
    after_values1 = values[360:]

    labels2 = []
    values2 = []
    read_data(7, 30, 'static/data/jisun2/1027_jisun2.txt', labels2, values2, time_interval)
    before_values2 = values2[:240]
    lunch_values2 = values2[240:360]
    after_values2 = values2[360:]

    labels3 = []
    values3 = []
    read_data(7, 30, 'static/data/jisun2/1028_jisun2.txt', labels3, values3, time_interval)
    before_values3 = values3[:240]
    lunch_values3 = values3[240:360]
    after_values3 = values3[360:]

    labels4 = []
    values4 = []
    read_data(7, 30, 'static/data/jisun2/1029_jisun2.txt', labels4, values4, time_interval)
    before_values4 = values4[:240]
    lunch_values4 = values4[240:360]
    after_values4 = values4[360:]

    labels5 = []
    values5 = []
    read_data(7, 30, 'static/data/jisun2/1030_jisun2.txt', labels5, values5, time_interval)
    before_values5 = values5[:240]
    lunch_values5 = values5[240:360]
    after_values5 = values5[360:]

    labels6 = []
    values6 = []
    read_data(7, 30, 'static/data/jisun2/1031_jisun2.txt', labels6, values6, time_interval)
    before_values6 = values6[:240]
    lunch_values6 = values6[240:360]
    after_values6 = values6[360:]

    labels7 = []
    values7 = []
    read_data(7, 30, 'static/data/jisun2/1101_jisun2.txt', labels7, values7, time_interval)
    before_values7 = values7[:240]
    lunch_values7 = values[240:360]
    after_values7 = values[360:]

    #return render_template('chart_jisun.html', labels=labels, values=values, labels2=labels2, values2=values2, labels3=labels3, values3=values3, values4=values4, values5=values5, values6=values6, values7=values7)
    return render_template('chart-details.html', where="벽산디지털밸리7차", min_y=1.7, max_y=3.1,  before_labels=before_labels, lunch_labels=lunch_labels, after_labels=after_labels, before_values1=before_values1, lunch_values1=lunch_values1, after_values1=after_values1, before_values2=before_values2, lunch_values2=lunch_values2, after_values2=after_values2, before_values3=before_values3, lunch_values3=lunch_values3, after_values3=after_values3, before_values4=before_values4, lunch_values4=lunch_values4, after_values4=after_values4, before_values5=before_values5, lunch_values5=lunch_values5, after_values5=after_values5, before_values6=before_values6, lunch_values6=lunch_values6, after_values6=after_values6, before_values7=before_values7, lunch_values7=lunch_values7, after_values7=after_values7)


@application.route('/chart_jeongja')
def chart_jeongja():
    time_interval = 46546

    labels = []
    values = []
    read_data(7, 30, 'static/data/jeongja2/1026_jeongja2.txt', labels, values, time_interval)
    before_labels = labels[:240]
    lunch_labels = labels[240:360]
    after_labels = labels[360:]
    before_values1 = values[:240]
    lunch_values1 = values[240:360]
    after_values1 = values[360:]

    labels2 = []
    values2 = []
    read_data(7, 30, 'static/data/jeongja2/1027_jeongja1.txt', labels2, values2, time_interval)
    before_values2 = values2[:240]
    lunch_values2 = values2[240:360]
    after_values2 = values2[360:]

    labels3 = []
    values3 = []
    read_data(7, 30, 'static/data/jeongja2/1028_jeongja2.txt', labels3, values3, time_interval)
    before_values3 = values3[:240]
    lunch_values3 = values3[240:360]
    after_values3 = values3[360:]

    labels4 = []
    values4 = []
    read_data(7, 30, 'static/data/jeongja2/1029_jeongja2.txt', labels4, values4, time_interval)
    before_values4 = values4[:240]
    lunch_values4 = values4[240:360]
    after_values4 = values4[360:]

    labels5 = []
    values5 = []
    read_data(7, 30, 'static/data/jeongja2/1030_jeongja2.txt', labels5, values5, time_interval)
    before_values5 = values5[:240]
    lunch_values5 = values5[240:360]
    after_values5 = values5[360:]

    labels6 = []
    values6 = []
    read_data(7, 30, 'static/data/jeongja2/1031_jeongja2.txt', labels6, values6, time_interval)
    before_values6 = values6[:240]
    lunch_values6 = values6[240:360]
    after_values6 = values6[360:]

    labels7 = []
    values7 = []
    read_data(7, 30, 'static/data/jeongja2/1101_jeongja2.txt', labels7, values7, time_interval)
    before_values7 = values7[:240]
    lunch_values7 = values[240:360]
    after_values7 = values[360:]

    return render_template('chart-details.html', where="ENC벤처드림타워3차", min_y=0, max_y=7, before_labels=before_labels, lunch_labels=lunch_labels, after_labels=after_labels, before_values1=before_values1, lunch_values1=lunch_values1, after_values1=after_values1, before_values2=before_values2, lunch_values2=lunch_values2, after_values2=after_values2, before_values3=before_values3, lunch_values3=lunch_values3, after_values3=after_values3, before_values4=before_values4, lunch_values4=lunch_values4, after_values4=after_values4, before_values5=before_values5, lunch_values5=lunch_values5, after_values5=after_values5, before_values6=before_values6, lunch_values6=lunch_values6, after_values6=after_values6, before_values7=before_values7, lunch_values7=lunch_values7, after_values7=after_values7)



@application.route('/chart_cheonmak')
def chart_cheonmak():
    time_interval = 46546

    labels = []
    values = []
    read_data(7, 30, 'static/data/cheonmak2/1026_cheonmak2.txt', labels, values, time_interval)
    before_labels = labels[:240]
    lunch_labels = labels[240:360]
    after_labels = labels[360:]
    before_values1 = values[:240]
    lunch_values1 = values[240:360]
    after_values1 = values[360:]

    labels2 = []
    values2 = []
    read_data(7, 30, 'static/data/cheonmak2/1027_cheonmak2.txt', labels2, values2, time_interval)
    before_values2 = values2[:240]
    lunch_values2 = values2[240:360]
    after_values2 = values2[360:]

    labels3 = []
    values3 = []
    read_data(7, 30, 'static/data/cheonmak2/1028_cheonmak2.txt', labels3, values3, time_interval)
    before_values3 = values3[:240]
    lunch_values3 = values3[240:360]
    after_values3 = values3[360:]

    labels4 = []
    values4 = []
    read_data(7, 30, 'static/data/cheonmak2/1029_cheonmak2.txt', labels4, values4, time_interval)
    before_values4 = values4[:240]
    lunch_values4 = values4[240:360]
    after_values4 = values4[360:]

    labels5 = []
    values5 = []
    read_data(7, 30, 'static/data/cheonmak2/1030_cheonmak2.txt', labels5, values5, time_interval)
    before_values5 = values5[:240]
    lunch_values5 = values5[240:360]
    after_values5 = values5[360:]

    labels6 = []
    values6 = []
    read_data(7, 30, 'static/data/cheonmak2/1031_cheonmak2.txt', labels6, values6, time_interval)
    before_values6 = values6[:240]
    lunch_values6 = values6[240:360]
    after_values6 = values6[360:]

    labels7 = []
    values7 = []
    read_data(7, 30, 'static/data/cheonmak2/1101_cheonmak2.txt', labels7, values7, time_interval)
    before_values7 = values7[:240]
    lunch_values7 = values[240:360]
    after_values7 = values[360:]

    return render_template('chart-details.html', where="삼성IT밸리", min_y=0.5, max_y=3.5,  before_labels=before_labels, lunch_labels=lunch_labels, after_labels=after_labels, before_values1=before_values1, lunch_values1=lunch_values1, after_values1=after_values1, before_values2=before_values2, lunch_values2=lunch_values2, after_values2=after_values2, before_values3=before_values3, lunch_values3=lunch_values3, after_values3=after_values3, before_values4=before_values4, lunch_values4=lunch_values4, after_values4=after_values4, before_values5=before_values5, lunch_values5=lunch_values5, after_values5=after_values5, before_values6=before_values6, lunch_values6=lunch_values6, after_values6=after_values6, before_values7=before_values7, lunch_values7=lunch_values7, after_values7=after_values7)



@application.route('/statistics-avg')
def statistics_avg():
    # 평균
    jisun2_avg_1026 = calc_avg('static/data/jisun2/1026_jisun2.txt')
    jeongja2_avg_1026 = calc_avg('static/data/jeongja2/1026_jeongja2.txt')
    cheonmak2_avg_1026 = calc_avg('static/data/cheonmak2/1026_cheonmak2.txt')

    jisun2_avg_1027 = calc_avg('static/data/jisun2/1027_jisun2.txt')
    jeongja2_avg_1027 = calc_avg('static/data/jeongja2/1027_jeongja1.txt')
    cheonmak2_avg_1027 = calc_avg('static/data/cheonmak2/1027_cheonmak2.txt')

    jisun2_avg_1028 = calc_avg('static/data/jisun2/1028_jisun2.txt')
    jeongja2_avg_1028 = calc_avg('static/data/jeongja2/1028_jeongja2.txt')
    cheonmak2_avg_1028 = calc_avg('static/data/cheonmak2/1028_cheonmak2.txt')

    jisun2_avg_1029 = calc_avg('static/data/jisun2/1029_jisun2.txt')
    jeongja2_avg_1029 = calc_avg('static/data/jeongja2/1029_jeongja2.txt')
    cheonmak2_avg_1029 = calc_avg('static/data/cheonmak2/1029_cheonmak2.txt')

    jisun2_avg_1030 = calc_avg('static/data/jisun2/1030_jisun2.txt')
    jeongja2_avg_1030 = calc_avg('static/data/jeongja2/1030_jeongja2.txt')
    cheonmak2_avg_1030 = calc_avg('static/data/cheonmak2/1030_cheonmak2.txt')

    jisun2_avg_1031 = calc_avg('static/data/jisun2/1031_jisun2.txt')
    jeongja2_avg_1031 = calc_avg('static/data/jeongja2/1031_jeongja2.txt')
    cheonmak2_avg_1031 = calc_avg('static/data/cheonmak2/1031_cheonmak2.txt')

    jisun2_avg_1101 = calc_avg('static/data/jisun2/1101_jisun2.txt')
    jeongja2_avg_1101 = calc_avg('static/data/jeongja2/1101_jeongja2.txt')
    cheonmak2_avg_1101 = calc_avg('static/data/cheonmak2/1101_cheonmak2.txt')

    return render_template('statistics-avg.html', jisun2_avg_1026=jisun2_avg_1026, jeongja2_avg_1026=jeongja2_avg_1026, cheonmak2_avg_1026=cheonmak2_avg_1026, jisun2_avg_1027=jisun2_avg_1027, jeongja2_avg_1027=jeongja2_avg_1027, cheonmak2_avg_1027=cheonmak2_avg_1027, jisun2_avg_1028=jisun2_avg_1028, jeongja2_avg_1028=jeongja2_avg_1028, cheonmak2_avg_1028=cheonmak2_avg_1028, jisun2_avg_1029=jisun2_avg_1029, jeongja2_avg_1029=jeongja2_avg_1029, cheonmak2_avg_1029=cheonmak2_avg_1029, jisun2_avg_1030=jisun2_avg_1030, jeongja2_avg_1030=jeongja2_avg_1030, cheonmak2_avg_1030=cheonmak2_avg_1030, jisun2_avg_1031=jisun2_avg_1031, jeongja2_avg_1031=jeongja2_avg_1031, cheonmak2_avg_1031=cheonmak2_avg_1031, jisun2_avg_1101=jisun2_avg_1101, jeongja2_avg_1101=jeongja2_avg_1101, cheonmak2_avg_1101=cheonmak2_avg_1101)

@application.route('/statistics-max')
def statistics_max():

    # 최대값
    jisun2_max = []
    jeongja2_max = []
    cheonmak2_max = []

    jisun2_max.append(calc_max('static/data/jisun2/1026_jisun2.txt'))
    jisun2_max.append(calc_max('static/data/jisun2/1027_jisun2.txt'))
    jisun2_max.append(calc_max('static/data/jisun2/1028_jisun2.txt'))
    jisun2_max.append(calc_max('static/data/jisun2/1029_jisun2.txt'))
    jisun2_max.append(calc_max('static/data/jisun2/1030_jisun2.txt'))
    jisun2_max.append(calc_max('static/data/jisun2/1031_jisun2.txt'))
    jisun2_max.append(calc_max('static/data/jisun2/1101_jisun2.txt'))

    jeongja2_max.append(calc_max('static/data/jeongja2/1026_jeongja2.txt'))
    jeongja2_max.append(calc_max('static/data/jeongja2/1027_jeongja1.txt'))
    jeongja2_max.append(calc_max('static/data/jeongja2/1028_jeongja2.txt'))
    jeongja2_max.append(calc_max('static/data/jeongja2/1029_jeongja2.txt'))
    jeongja2_max.append(calc_max('static/data/jeongja2/1030_jeongja2.txt'))
    jeongja2_max.append(calc_max('static/data/jeongja2/1031_jeongja2.txt'))
    jeongja2_max.append(calc_max('static/data/jeongja2/1101_jeongja2.txt'))

    cheonmak2_max.append(calc_max('static/data/cheonmak2/1026_cheonmak2.txt'))
    cheonmak2_max.append(calc_max('static/data/cheonmak2/1027_cheonmak2.txt'))
    cheonmak2_max.append(calc_max('static/data/cheonmak2/1028_cheonmak2.txt'))
    cheonmak2_max.append(calc_max('static/data/cheonmak2/1029_cheonmak2.txt'))
    cheonmak2_max.append(calc_max('static/data/cheonmak2/1030_cheonmak2.txt'))
    cheonmak2_max.append(calc_max('static/data/cheonmak2/1031_cheonmak2.txt'))
    cheonmak2_max.append(calc_max('static/data/cheonmak2/1101_cheonmak2.txt'))


    return render_template('statistics-max.html', jisun2_max=jisun2_max, jeongja2_max=jeongja2_max, cheonmak2_max=cheonmak2_max)


@application.route('/opensource')
def opensource():
    return render_template('opensource.html')


@application.route('/forum')
def forum():
    return render_template('forum.html')


if __name__ == '__main__':
    application.run()
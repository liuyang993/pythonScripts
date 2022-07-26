from datetime import datetime, timedelta
import pandas as pd

def print_annotations(plt,tablename):
    # if tablename == 'oi2105_20210326':
        # print('find')
        # tablename = 'ag2012_20200730'
    x = tablename.split("_")
    print(x)

    # print(x[1])
    # data_set = pd.read_csv('D:\\stock\\所有委托单_20210326.csv',encoding="utf-8")

    filename =  'D:\\stock\\所有委托单_' + x[1] + '.csv'
    print(filename)
    # data_set = pd.read_csv(filename,encoding="utf-8")

    try:
        # df_data = pd.read_csv(file, index_col=0)
        data_set = pd.read_csv(filename,encoding="utf-8")

    except FileNotFoundError: 
        return
    

    for singlerow in data_set.iterrows():
        # print(singlerow[1][1])
        #print('------------')
        #print(datetime.strptime(x[1] + ' ' + singlerow[1][9], '%Y%m%d %H:%M:%S'))
        # print(datetime.strptime(x[1] + ' ' + singlerow[1][9], '%Y%m%d %H:%M:%S') - timedelta(days=1))

        # print(datetime.strptime(x[1],'%Y%m%d'))

        # if datetime.strptime(x[1],'%Y%m%d').weekday() == 0:
        #     print("this is monday")

        # print(datetime.strptime(singlerow[1][9], '%H:%M:%S'))
        if(datetime.strptime(singlerow[1][9], '%H:%M:%S') > datetime.strptime('21:00:00', '%H:%M:%S')):
            # print('niht deal')   #说明是夜盘
            # print(str(singlerow[1][5]) + singlerow[1][2]  + singlerow[1][3] + str(singlerow[1][6])  + str(singlerow[1][4]))
            # print(datetime.strptime(x[1] + ' ' + singlerow[1][9], '%Y%m%d %H:%M:%S') - timedelta(days=1))
            # print(datetime.strptime(x[1] + ' '  + singlerow[1][9], '%Y%m%d %H:%M:%S') - timedelta(days=1))

            if datetime.strptime(x[1],'%Y%m%d').weekday() == 0:     # mean monday
                if(x[0].startswith('j2')):
                    plt.annotate(str(singlerow[1][5]) + singlerow[1][2]  + singlerow[1][3] + str(singlerow[1][6])  + str(singlerow[1][4])   , xy=(datetime.strptime(x[1] + ' ' + singlerow[1][9], '%Y%m%d %H:%M:%S'), singlerow[1][5]), xytext=(datetime.strptime(x[1] + ' '  + singlerow[1][9], '%Y%m%d %H:%M:%S'), singlerow[1][5] + singlerow[1][5] * 0.001),
                        arrowprops={'arrowstyle': '->', 'lw': 2, 'color': 'blue'},
                        va = "bottom", ha="center")
                else:        
                    plt.annotate(str(singlerow[1][5]) + singlerow[1][2]  + singlerow[1][3] + str(singlerow[1][6])  + str(singlerow[1][4])   , xy=(datetime.strptime(x[1] + ' ' + singlerow[1][9], '%Y%m%d %H:%M:%S') - timedelta(days=3), singlerow[1][5]), xytext=(datetime.strptime(x[1] + ' '  + singlerow[1][9], '%Y%m%d %H:%M:%S') - timedelta(days=3), singlerow[1][5] + singlerow[1][5] * 0.001),
                        arrowprops={'arrowstyle': '->', 'lw': 2, 'color': 'blue'},
                        va = "bottom", ha="center")
            else:
                if(x[0].startswith('j2')):
                    plt.annotate(str(singlerow[1][5]) + singlerow[1][2]  + singlerow[1][3] + str(singlerow[1][6])  + str(singlerow[1][4])   , xy=(datetime.strptime(x[1] + ' ' + singlerow[1][9], '%Y%m%d %H:%M:%S'), singlerow[1][5]), xytext=(datetime.strptime(x[1] + ' '  + singlerow[1][9], '%Y%m%d %H:%M:%S'), singlerow[1][5] + singlerow[1][5] * 0.001),
                        arrowprops={'arrowstyle': '->', 'lw': 2, 'color': 'blue'},
                        va = "bottom", ha="center")
                else:
                    # print("not monday , night , not j21XX")
                    plt.annotate(str(singlerow[1][5]) + singlerow[1][2]  + singlerow[1][3] + str(singlerow[1][6])  + str(singlerow[1][4])   , xy=(datetime.strptime(x[1] + ' ' + singlerow[1][9], '%Y%m%d %H:%M:%S') - timedelta(days=1), singlerow[1][5]), xytext=(datetime.strptime(x[1] + ' '  + singlerow[1][9], '%Y%m%d %H:%M:%S') - timedelta(days=1), singlerow[1][5] + 10 ),
                        arrowprops={'arrowstyle': '->', 'lw': 2, 'color': 'blue'},
                        va = "bottom", ha="center")
        else:
            # 白天盘
            plt.annotate(str(singlerow[1][5]) + singlerow[1][2]  + singlerow[1][3] + str(singlerow[1][6])  + str(singlerow[1][4])   , xy=(datetime.strptime(x[1] + ' ' + singlerow[1][9], '%Y%m%d %H:%M:%S'), singlerow[1][5]), xytext=(datetime.strptime(x[1] + ' '  + singlerow[1][9], '%Y%m%d %H:%M:%S'), singlerow[1][5] - 10),
                arrowprops={'arrowstyle': '->', 'lw': 2, 'color': 'blue'},
                va = "bottom", ha="center")      

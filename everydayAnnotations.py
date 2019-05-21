import datetime as dt

def print_annotations(plt,tablename):
    if tablename == 'if1906_20190509':

        plt.figtext(0,.93,'周四\n期初一空一多，if昨收长上影线，冲高回落， 收3652\n随波逐流单: 无\n逆市单: 4')

        plt.annotate(U'早高点3649', xy=(dt.datetime(2019,5,9,9,42,24)+dt.timedelta(minutes=90) , 3649), xytext=(dt.datetime(2019,5,9,9,42,24)+dt.timedelta(minutes=70) , 3649-5),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")

        plt.annotate(U'3626.2下多单， 犯了接飞刀的错误', xy=(dt.datetime(2019,5,9,9,50,9)+dt.timedelta(minutes=90) , 3626.2), xytext=(dt.datetime(2019,5,9,9,50,9)+dt.timedelta(minutes=70) , 3626.2-5),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")

        plt.annotate(U'3607止损平多', xy=(dt.datetime(2019,5,9,10,24,29)+dt.timedelta(minutes=90) , 3607), xytext=(dt.datetime(2019,5,9,10,24,29)+dt.timedelta(minutes=70) , 3607-5),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")


        plt.annotate(U'3583下多单，因为之前损失20点， 当时的想法是 ： 应该能回到 3600，这样20点就回来了', xy=(dt.datetime(2019,5,9,10,40,0)+dt.timedelta(minutes=90) , 3583), xytext=(dt.datetime(2019,5,9,10,40,0)+dt.timedelta(minutes=70) , 3583-5),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")

        plt.annotate(U'3594.8平多单', xy=(dt.datetime(2019,5,9,10,55,12)+dt.timedelta(minutes=90) , 3594.8), xytext=(dt.datetime(2019,5,9,10,55,12)+dt.timedelta(minutes=70) , 3594.8-5),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")

        plt.annotate(U'3564下多单，当时的想法是 ：之前的3558至少是短期低点，回到3564是2次回坐，是做多的机会.但还是老毛病， 盈利拿不住', xy=(dt.datetime(2019,5,9,11,3,38)+dt.timedelta(minutes=90) , 3564), xytext=(dt.datetime(2019,5,9,11,3,38)+dt.timedelta(minutes=70) , 3564-5),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")            

        plt.annotate(U'3576平多单，拿不住，但此时日内已经不输钱', xy=(dt.datetime(2019,5,9,11,5,17)+dt.timedelta(minutes=90) , 3576), xytext=(dt.datetime(2019,5,9,11,5,17)+dt.timedelta(minutes=70) , 3576-5),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")     

        plt.annotate(U'3603下空单，被盯盘误导了，此时应该想有2个可能， 如果这次上涨是诱多， 此时距离启动仅仅5分钟， 多数人没反应过来， 多方都没机会进场，如果不是诱多， 做空更错', xy=(dt.datetime(2019,5,9,13,13,45) , 3603), xytext=(dt.datetime(2019,5,9,13,13,45)-dt.timedelta(minutes=20) , 3603-5),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")                    

        plt.annotate(U'3622平空，总是这个毛病， 一旦空错，非要等到见高点， 而且从高点稍微下来一点就止损平空', xy=(dt.datetime(2019,5,9,13,20,44) , 3622), xytext=(dt.datetime(2019,5,9,13,20,44)-dt.timedelta(minutes=20) , 3622-5),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")      
    
    if tablename == 'if1906_20190508':
        plt.annotate(U'3657下空单，\n当时的想法是 366X是昨天的低点，而昨天的走势尤其是下午的急涨急落很让人联想到20190307，所以以为今天的高点也会和20190308一样是昨天低点366x附近\n但是怎么不想想20190308涨到了10点半', xy=(dt.datetime(2019,5,8,9,46,50)+dt.timedelta(minutes=90) , 3657), xytext=(dt.datetime(2019,5,8,9,46,50)+dt.timedelta(minutes=110) , 3657-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")

        plt.annotate(U'2分钟后3653平空，虽然结果是对的， 但还是太小了', xy=(dt.datetime(2019,5,8,9,48,50)+dt.timedelta(minutes=90) , 3653), xytext=(dt.datetime(2019,5,8,9,48,50)+dt.timedelta(minutes=70) , 3653-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")     
        
        plt.annotate(U'3674.2下空单，\n理由是判断急涨接近到顶，而且当时也正好是10点', xy=(dt.datetime(2019,5,8,10,2,32)+dt.timedelta(minutes=90) , 3674.2), xytext=(dt.datetime(2019,5,8,10,2,32)+dt.timedelta(minutes=70) , 3674.2-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")

        plt.annotate(U'1分钟后3670.4平空，太小,像这种程度的急涨，自高点（这里是 3676）回落10个点是起码的', xy=(dt.datetime(2019,5,8,10,3,20)+dt.timedelta(minutes=90) , 3670.4), xytext=(dt.datetime(2019,5,8,10,3,20)+dt.timedelta(minutes=110) , 3670.4-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")     

    if tablename == 'if1906_20190514':
        plt.annotate(U'3647下多单，\n当时的想法是 看到 ic1906急涨， 而 if 还没完全跟上', xy=(dt.datetime(2019,5,8,9,46,50)+dt.timedelta(minutes=90) , 3657), xytext=(dt.datetime(2019,5,8,9,46,50)+dt.timedelta(minutes=110) , 3657-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")

        plt.annotate(U'3651平多单，老毛病拿不住', xy=(dt.datetime(2019,5,8,9,46,50)+dt.timedelta(minutes=90) , 3657), xytext=(dt.datetime(2019,5,8,9,46,50)+dt.timedelta(minutes=110) , 3657-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center") 

        plt.annotate(U'3647下多单，当时感觉3648一线的底可能是假， 但是觉得也可能会再诱多一波， 尤其在11点半之前 ', xy=(dt.datetime(2019,5,8,9,46,50)+dt.timedelta(minutes=90) , 3657), xytext=(dt.datetime(2019,5,8,9,46,50)+dt.timedelta(minutes=110) , 3657-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")

        plt.annotate(U'3648平多单，机警', xy=(dt.datetime(2019,5,8,9,46,50)+dt.timedelta(minutes=90) , 3657), xytext=(dt.datetime(2019,5,8,9,46,50)+dt.timedelta(minutes=110) , 3657-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")                        

    if tablename == 'if1906_20190517':
        plt.figtext(0,.89,'周五\n期初一空一多，if昨收小红盘，收盘最高， 收3708\n本日美国宣布对华为供应链禁令\n随波逐流单: 无\n主动逆市单: 2')
        plt.annotate(U'3681下多单，\n当时的想法是ic1906有反弹， 而 if 还没，此外就是收昨天影响\n昨天在 3680有几次反弹\n但是，即使抢反弹也应该等到下破3680整数以后', xy=(dt.datetime(2019,5,17,9,56,49)+dt.timedelta(minutes=90) , 3681), xytext=(dt.datetime(2019,5,17,9,56,49)+dt.timedelta(minutes=70) , 3681-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")

        plt.annotate(U'3683平抄底多单，\n正确', xy=(dt.datetime(2019,5,17,9,58,39)+dt.timedelta(minutes=90) , 3683), xytext=(dt.datetime(2019,5,17,9,58,39)+dt.timedelta(minutes=110) , 3683+20),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")
        plt.annotate(U'3672下抄底多单，\n当时的想法是认为3670是短期底， 3672是2次确认\n判断错， 此后20分钟内，有机会无损走人， 但侥幸心理作祟', xy=(dt.datetime(2019,5,17,10,8,1)+dt.timedelta(minutes=90) , 3672), xytext=(dt.datetime(2019,5,17,10,8,1)+dt.timedelta(minutes=70) , 3672-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")
        plt.annotate(U'3652.4平多单，\n此时应该看出今天不反弹了', xy=(dt.datetime(2019,5,17,10,49)+dt.timedelta(minutes=90) , 3652.4), xytext=(dt.datetime(2019,5,17,10,49)+dt.timedelta(minutes=110) , 3652.4+20),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")

        plt.annotate(U'3637.4下抄底多单，\n不冷静\n3652刚平，怎么才跌了10个点又抄底了？\n这段是下跌的高潮期，距上次低点3647下跌了30个点到3617', xy=(dt.datetime(2019,5,17,10,59,48)+dt.timedelta(minutes=90) , 3637.4), xytext=(dt.datetime(2019,5,17,10,59,48)+dt.timedelta(minutes=70) , 3637.4-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")         

        plt.annotate(U'3634.4平多单，\n', xy=(dt.datetime(2019,5,17,11,28,25)+dt.timedelta(minutes=90) , 3634.4), xytext=(dt.datetime(2019,5,17,11,28,25)+dt.timedelta(minutes=110) , 3634.4+20),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")            
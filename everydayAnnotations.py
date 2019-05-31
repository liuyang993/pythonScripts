import datetime as dt

def print_annotations(plt,tablename):
    if tablename == 'if1906_20190509':
        plt.figtext(0,.93,'周四\n期初一空一多，if昨收长上影线，冲高回落， 收3652\n随波逐流单: 无\n逆市单: 4')

        plt.annotate(U'早高点3649', xy=(dt.datetime(2019,5,9,9,42,24)+dt.timedelta(minutes=90) , 3649), xytext=(dt.datetime(2019,5,9,9,42,24)+dt.timedelta(minutes=70) , 3649-5),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")

        plt.annotate(U'3626.2下多单， 犯了接飞刀的错误\n记住急跌的停止点不是做多点， 要等到2次低点', xy=(dt.datetime(2019,5,9,9,50,9)+dt.timedelta(minutes=90) , 3626.2), xytext=(dt.datetime(2019,5,9,9,50,9)+dt.timedelta(minutes=70) , 3626.2-5),
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

        plt.annotate(U'3603下空单，恨涨心态，因为之前的多单平早了\n此时应该想有2个可能， 如果这次上涨是诱多， 此时距离启动仅仅5分钟， 多数人没反应过来， 多方都没机会进场，如果不是诱多， 做空更错', xy=(dt.datetime(2019,5,9,13,13,45) , 3603), xytext=(dt.datetime(2019,5,9,13,13,45)-dt.timedelta(minutes=20) , 3603-5),
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

    if tablename == 'if1906_20190516':
         plt.annotate(U'3677.8下空单，\n错误， 是tips的 A型错误右图，这里不可以做空', xy=(dt.datetime(2019,5,16,10,7,11)+dt.timedelta(minutes=90) , 3677.8), xytext=(dt.datetime(2019,5,16,10,7,11)+dt.timedelta(minutes=70) , 3677.8-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")     
              
         plt.annotate(U'3673.4平空\n正确，及时挽回错误\n此时应该追多', xy=(dt.datetime(2019,5,16,10,8,38)+dt.timedelta(minutes=90) , 3673.4), xytext=(dt.datetime(2019,5,16,10,8,38)+dt.timedelta(minutes=110) , 3673.4-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center") 

         plt.annotate(U'3698下空单\n为什么这么执着的下空， 可能是因为今天是周四\n这次做空时机选的正确', xy=(dt.datetime(2019,5,16,10,43,50)+dt.timedelta(minutes=90) , 3698), xytext=(dt.datetime(2019,5,16,10,43,50)+dt.timedelta(minutes=70) , 3698-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")   
         plt.annotate(U'(10:45:15) 3695.4平空\n错误，太小了,可能是怕午盘冲高', xy=(dt.datetime(2019,5,16,10,45,15)+dt.timedelta(minutes=90) , 3695.4), xytext=(dt.datetime(2019,5,16,10,45,15)+dt.timedelta(minutes=110) , 3695.4-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
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

    if tablename == 'if1906_20190520':
        plt.figtext(0,.90,'周一 ，周日晚传出消息：刘士余自首\nGoogle遵守对华为的禁令，以后华为手机将不能使用 google产品包括gmail , youtube google store 等\n期初一空一多，if昨单边跌无反弹(所以今天有反弹)， \n今开3622 收3587 高3625  低 3551\n随波逐流单: 无\n逆市单: 3')
        plt.annotate(U'09：48：58. 3579.2下多单，\n当时的想法是 看到 ic1906急反弹， 而 if 还没完全跟上\n但是，这个位置是急跌停止点， 有反弹也不会太大', xy=(dt.datetime(2019,5,20,9,48,58)+dt.timedelta(minutes=90) , 3579.2), xytext=(dt.datetime(2019,5,20,9,48,58)+dt.timedelta(minutes=70) , 3579.2-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")
        plt.annotate(U'09：49：16. 3586.2平多单，\n正确，此后6分钟是急跌后的横盘阶段，应于此点位转空', xy=(dt.datetime(2019,5,20,9,49,16)+dt.timedelta(minutes=90) , 3586.2), xytext=(dt.datetime(2019,5,20,9,49,16)+dt.timedelta(minutes=110) , 3586.2-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center")
        plt.annotate(U'09：57：28 . 3569.4下多单，\n理由是2次低点， 而且破了整数位', xy=(dt.datetime(2019,5,20,9,57,28)+dt.timedelta(minutes=90) , 3569.4), xytext=(dt.datetime(2019,5,20,9,57,28)+dt.timedelta(minutes=70) , 3569.4-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")      

        plt.annotate(U'09：58：22. 3579平多单，\n正确，不贪，很难超过上次的横盘位置 3580 ，但是， 还是应该转空', xy=(dt.datetime(2019,5,20,9,58,22)+dt.timedelta(minutes=90) , 3579), xytext=(dt.datetime(2019,5,20,9,58,22)+dt.timedelta(minutes=110) , 3579-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center")                 
        plt.annotate(U'10：25：16. 3556附近 全天最低点\n为什么这个时候又不抄底了？？？', xy=(dt.datetime(2019,5,20,10,25,16)+dt.timedelta(minutes=90) , 3556), xytext=(dt.datetime(2019,5,20,10,25,16)+dt.timedelta(minutes=110) , 3556-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center")   

        plt.annotate(U'3577下空单，\n收昨天影响， 以为尾盘还会跌\n这个位置做空很危险，因为3580的高点下午在此之前至少出现过3次(这也是做空的原因，思路被主力引导)，还做空是刻舟求剑', xy=(dt.datetime(2019,5,20,14,0,6), 3577), xytext=(dt.datetime(2019,5,20,14,0,6)-dt.timedelta(minutes=20) , 3577-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")              
        plt.annotate(U'3573.4平空单，\n虽然过早-之后有3568的低点，但仍正确， 3580是高点是主力故意引导的，如果持这个观点至尾盘会被杀空', xy=(dt.datetime(2019,5,20,14,1,36), 3577), xytext=(dt.datetime(2019,5,20,14,1,36)+dt.timedelta(minutes=20) , 3573.4-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center")    
    if tablename == 'if1906_20190521':
        plt.figtext(0,.90,'周二，\n期初一空一多\n消息： 前一天盘后： 20日A股延续调整成交明显萎缩-新华网 \n今开3597 收3625 高 3673  低 3590\n随波逐流单: 无\n逆市单: 3')
        plt.annotate(U'09：46：15. 3618.8下空单，\n错误，之前1到2分钟出过3620的高点，就算做空也要等到2次高点超过3620，为什么在3618.8空？', xy=(dt.datetime(2019,5,21,9,46,15)+dt.timedelta(minutes=90) , 3618.8), xytext=(dt.datetime(2019,5,21,9,46,15)+dt.timedelta(minutes=80) , 3618.8+10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")

        plt.annotate(U'09：46：32. A点 3623', xy=(dt.datetime(2019,5,21,9,46,32)+dt.timedelta(minutes=90) , 3623), xytext=(dt.datetime(2019,5,21,9,46,32)+dt.timedelta(minutes=90), 3623+2),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center")
        plt.annotate(U'09：52：54. B点 3625', xy=(dt.datetime(2019,5,21,9,52,54)+dt.timedelta(minutes=90) , 3625), xytext=(dt.datetime(2019,5,21,9,52,54)+dt.timedelta(minutes=90), 3625+2),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center")     
        plt.annotate(U'10：0：2. C点 3627.8, A,B,C三点构成五分钟级别的三连阳，又正逢10点钟， 所以C点是做空好点', xy=(dt.datetime(2019,5,21,10,0,2)+dt.timedelta(minutes=90) , 3627.8), xytext=(dt.datetime(2019,5,21,10,0,2)+dt.timedelta(minutes=90), 3627.8+20),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center")                        

        plt.annotate(U'09：48：39. 3618平空单，\n正确，之前做错了，此时退出没问题', xy=(dt.datetime(2019,5,21,9,48,39)+dt.timedelta(minutes=90) , 3618), xytext=(dt.datetime(2019,5,21,9,48,39)+dt.timedelta(minutes=100) , 3618-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center")
        plt.annotate(U'10：09：13. 3613下多单，\n因为正好在手机同花顺看到 建议股指期货持空单，觉得一定是害人的，所以做多\n但是时机不对， 当时算是急跌停止点，不能做多\n应该在略破早盘前一阶段高点3610的时候做多', xy=(dt.datetime(2019,5,21,10,9,13)+dt.timedelta(minutes=90) , 3613), xytext=(dt.datetime(2019,5,21,10,9,13)+dt.timedelta(minutes=80) , 3613-15),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")
        plt.annotate(U'10：18：14. 3617.8平多单，\n正确， 较五分钟之前3608低点反弹10个点', xy=(dt.datetime(2019,5,21,10,18,14)+dt.timedelta(minutes=90) , 3617.8), xytext=(dt.datetime(2019,5,21,10,18,14)+dt.timedelta(minutes=100) , 3617.8-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center")      
        plt.annotate(U'10：24：22. 3604.6 大涨前的洗盘，\n接近10点半', xy=(dt.datetime(2019,5,21,10,24,22)+dt.timedelta(minutes=90) , 3604.6), xytext=(dt.datetime(2019,5,21,10,24,22)+dt.timedelta(minutes=90) , 3604.6-15),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center")   
        plt.annotate(U'11：03：21. 3665下空单，\n急躁，虽然已经冲了半小时，可能冲不到午盘收盘，但即使做空也要等见到高点再横一段时间', xy=(dt.datetime(2019,5,21,11,3,21)+dt.timedelta(minutes=90) , 3665), xytext=(dt.datetime(2019,5,21,11,3,21)+dt.timedelta(minutes=70) , 3665),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")                        
        plt.annotate(U'11：11：13. 3662.6平空单，\n这种操作真的多余做， 2.4个点利润 ，减手续费就赚300块钱， 和风险完全不成比例\n此外， 为什么之后又不做空了？', xy=(dt.datetime(2019,5,21,11,11,13)+dt.timedelta(minutes=90) , 3662.6), xytext=(dt.datetime(2019,5,21,11,11,13)+dt.timedelta(minutes=100) , 3662.6-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center")  
        plt.annotate(U'13：16：42. 3637下多单，\n又是急跌停止点做多', xy=(dt.datetime(2019,5,21,13,16,42) , 3637), xytext=(dt.datetime(2019,5,21,13,16,42)-dt.timedelta(minutes=20) , 3637-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")      
        plt.annotate(U'13：19：33. 3640平多单，太小\n', xy=(dt.datetime(2019,5,21,13,19,33) , 3640), xytext=(dt.datetime(2019,5,21,13,19,33)+dt.timedelta(minutes=20) , 3640+10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center")                            

    if tablename == 'if1906_20190523':
        plt.figtext(0,.85,'周四，周三晚传出消息：茅台董事长被抓，但是今天茅台跌的不多---2% ，不过茅台越不跌， 大伙越害怕\narm遵守对华为的禁令\n东芝停供华为\n期初一空一多，if昨冲高回落尾盘反弹， 收362X\n随波逐流单: 1\n逆市单: 3')

        plt.annotate(U'9:35:55  3568是二次低点，此位置就应该有反弹， \n暂时没有是因为多数人没反应过来，还不肯割肉 ', xy=(dt.datetime(2019,5,23,9,35,55)+dt.timedelta(minutes=90), 3568), xytext=(dt.datetime(2019,5,23,9,35,55)+dt.timedelta(minutes=80) , 3568-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")           
        plt.annotate(U'9:37:34  3558.6  A点， \nA点之前是急跌， 杀胆小的昨天多方\nA点之后20多分钟是多次假反弹缓跌，杀性急的昨天多方， ', xy=(dt.datetime(2019,5,23,9,37,34)+dt.timedelta(minutes=90), 3558.6), xytext=(dt.datetime(2019,5,23,9,37,34)+dt.timedelta(minutes=80) , 3558.6-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")                
        plt.annotate(U'9:40:36  3569下空单， \n想法是3568就该上去， 既然没上去， 那么3568会成为一个短期顶，而且这里是一个二次高点', xy=(dt.datetime(2019,5,23,9,40,36)+dt.timedelta(minutes=90), 3569), xytext=(dt.datetime(2019,5,23,9,40,36)+dt.timedelta(minutes=80) , 3569+10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")      
        plt.annotate(U'9:42:30  3564.4平空单， \n太小了', xy=(dt.datetime(2019,5,23,9,42,30)+dt.timedelta(minutes=90), 3564.4), xytext=(dt.datetime(2019,5,23,9,42,30)+dt.timedelta(minutes=100) , 3564.4-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center")                         
        plt.annotate(U'10:15:55  3559.2下空单， \n错误， 此时不应再下空单， \n是受了之前几分钟故意显示无法冲过3560的影响', xy=(dt.datetime(2019,5,23,10,15,55)+dt.timedelta(minutes=90), 3559.2), xytext=(dt.datetime(2019,5,23,10,15,55)+dt.timedelta(minutes=80) , 3559.2-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")        
        plt.annotate(U'10:19:00  3555.6平空单， \n正确， 此时应该察觉出做空不对了，但是并没有', xy=(dt.datetime(2019,5,23,10,19)+dt.timedelta(minutes=90), 3555.6), xytext=(dt.datetime(2019,5,23,10,19)+dt.timedelta(minutes=110) , 3555.6-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center")    
        plt.annotate(U'10:24:09  3564.6下空单， \n当时是急涨到3565 ，所以下的空单', xy=(dt.datetime(2019,5,23,10,24,9)+dt.timedelta(minutes=90), 3564.6), xytext=(dt.datetime(2019,5,23,10,24,9)+dt.timedelta(minutes=70) , 3564.6-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")  
        plt.annotate(U'10:27:11  3560.4平空单， \n正确， 此时应该察觉出做空不对了，因为高点在逐渐上升', xy=(dt.datetime(2019,5,23,10,27,11)+dt.timedelta(minutes=90), 3560.4), xytext=(dt.datetime(2019,5,23,10,27,11)+dt.timedelta(minutes=110) , 3560.4-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center")     
        plt.annotate(U'10:46:17  3574下空单， \n因为之前3650底部时间太长， before再次上涨，需要洗盘，洗盘必然要做出无力突破的姿态， \n此时错把洗盘当做见顶', xy=(dt.datetime(2019,5,23,10,46,17)+dt.timedelta(minutes=90), 3574), xytext=(dt.datetime(2019,5,23,10,46,17)+dt.timedelta(minutes=70) , 3574-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")             
        plt.annotate(U'10:58:04  3591平空单， \n此时的心理是害怕午盘冲高，犯了和5月9号一样的错误\n这个点位看起来也可以理解为冲午盘之前的顿挫', xy=(dt.datetime(2019,5,23,10,58,4)+dt.timedelta(minutes=90), 3591), xytext=(dt.datetime(2019,5,23,10,58,4)+dt.timedelta(minutes=110) , 3591-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center")  
        plt.annotate(U'14:09:45  3562.4下多单， \n下午的高点是1点40的3583，到现在已经跌了半小时， 感觉可能会冲高一下， 吸引尾盘买家', xy=(dt.datetime(2019,5,23,14,9,45), 3562.4), xytext=(dt.datetime(2019,5,23,14,9,45)-dt.timedelta(minutes=20) , 3562.4-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")             
        plt.annotate(U'14:17:12  3565平多单， \n太小， 被洗，以为过不去3566，随后到了3575', xy=(dt.datetime(2019,5,23,14,17,12), 3565), xytext=(dt.datetime(2019,5,23,14,17,12)+dt.timedelta(minutes=20) , 3565-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center")              
    if tablename == 'if1906_20190524':   
        plt.figtext(0,.90,'周五，周四尾盘回落收 355X,今天反而高开在 3570 ,收盘证明仍是大户带节奏让散户冲\n有传言说股指期货要进一步松绑\n昨晚美股大跌， 今天反而高开了\n期初一空一多，\n随波逐流单: 1\n逆市单: 2')

        plt.annotate(U'9:33:1  3591下空单， \n想法是昨天下午3580是顶，现在涨到 3591差不多了', xy=(dt.datetime(2019,5,24,9,33,1)+dt.timedelta(minutes=90), 3591), xytext=(dt.datetime(2019,5,24,9,33,1)+dt.timedelta(minutes=80) , 3591+10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")      
        plt.annotate(U'9:33:28  3587平空单， \n正确，开盘刚3分钟， 不能说3591就是顶了，仍有破3600的可能', xy=(dt.datetime(2019,5,24,9,33,28)+dt.timedelta(minutes=90), 3587), xytext=(dt.datetime(2019,5,24,9,33,28)+dt.timedelta(minutes=100) , 3587-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center") 
        plt.annotate(U'9:39:38  3603下空单，正确', xy=(dt.datetime(2019,5,24,9,39,38)+dt.timedelta(minutes=90), 3603), xytext=(dt.datetime(2019,5,24,9,39,38)+dt.timedelta(minutes=80) , 3603+10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")      
        plt.annotate(U'9:43:44  3598.2平空单， \n错误，太小了，浪费了全天最正确的选择\n下空单后的5分钟内， 主力2次暗示 3600是底，破了很快能弹回来\n不过是5分钟的2次小花招，我就中计了', xy=(dt.datetime(2019,5,24,9,43,44)+dt.timedelta(minutes=90), 3598.2), xytext=(dt.datetime(2019,5,24,9,43,44)+dt.timedelta(minutes=100) , 3598.2+10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center")   
        plt.annotate(U'9:52:13  3589下空单未成\n此处做空有危险， 但是也可以做， 因为一般大跌后第三次出高点才有可能上去\n但是这里的空单如果成功了，必须有小利就走，因为也可以说是A型错误', xy=(dt.datetime(2019,5,24,9,52,13)+dt.timedelta(minutes=90), 3589), xytext=(dt.datetime(2019,5,24,9,52,13)+dt.timedelta(minutes=80) , 3589+10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")    
        plt.annotate(U'9:55:34  又假装冲高到 3599， 为什么在这里没敢做空？当时是怎么想的，\n是受昨天影响,觉得会出新高， 或者平前高吗？ ', xy=(dt.datetime(2019,5,24,9,55,34)+dt.timedelta(minutes=90), 3599), xytext=(dt.datetime(2019,5,24,9,55,34)+dt.timedelta(minutes=100) , 3599),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")                         
        plt.annotate(U'10:00:13  3588下空单，正确，随波逐流单，但是反应迟钝，早就该空', xy=(dt.datetime(2019,5,24,10,0,13)+dt.timedelta(minutes=90), 3588), xytext=(dt.datetime(2019,5,24,10,0,13)+dt.timedelta(minutes=100) , 3588+10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")    
        plt.annotate(U'10:02:52  3583.4 平空单，还是小， 这里的位置是高点浅跌之后的横盘， 还会下去', xy=(dt.datetime(2019,5,24,10,2,52)+dt.timedelta(minutes=90), 3583.4), xytext=(dt.datetime(2019,5,24,10,2,52)+dt.timedelta(minutes=100) , 3583.4-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center")    
        plt.annotate(U'10:28:14  3572.4下多单，错误，逆市单，这里是不服气空单没赚到大钱之后的逆反心理，要逆市做多了\n但是，即使做多也要等到破整数位比如到68，67之类\n所以这里反了2个错误\n最关键的是， 急跌后横盘， 不出新低不会反弹的', xy=(dt.datetime(2019,5,24,10,28,14)+dt.timedelta(minutes=90), 3572.4), xytext=(dt.datetime(2019,5,24,10,28,14)+dt.timedelta(minutes=100) , 3572.4+10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")    
        plt.annotate(U'10:43:07  3571 平多单\n被连续一小时的下跌吓住，害怕心理， 也因为之前的抄底点位不对， 当时的想法是少损退出', xy=(dt.datetime(2019,5,24,10,43,7)+dt.timedelta(minutes=90), 3571), xytext=(dt.datetime(2019,5,24,10,43,7)+dt.timedelta(minutes=100) , 3571-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center")                                                               

    if tablename == 'if1906_20190527':
        plt.figtext(0,.85,'周一，周五早盘涨，反复弹起 高3605，低3553 收3569\n周末消息： 中芯国际退美股，联想cdo就：可能会将生产线退出中国道歉\n郭树清称： 做空人民币将巨亏\n包商银行被接管\n期初一空一多，\n随波逐流单: 1\n逆市单: 3')
        
        plt.annotate(U'9:36:31  3569.4下空单， \n想法是昨天收3569就是翘尾盘， 今早冲高3578很勉强，果然很快就急跌到 3541 ，然后又急反弹到3569，此时冲动做空\n错误，这种程度的急涨必然齐前高或者超出', xy=(dt.datetime(2019,5,27,9,36,31)+dt.timedelta(minutes=90), 3569), xytext=(dt.datetime(2019,5,27,9,36,31)+dt.timedelta(minutes=70) , 3569+10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")                     
   
        plt.annotate(U'9:40:12  3571.6平空单， \n错误，害怕心理作祟，急反弹涨到略超前高已经是极限，当时已经想到了今天可能像20181019\n但即使是那天， 也2次探底了', xy=(dt.datetime(2019,5,27,9,40,12)+dt.timedelta(minutes=90), 3571.6), xytext=(dt.datetime(2019,5,27,9,40,12)+dt.timedelta(minutes=110) , 3571.6-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center") 

        plt.annotate(U'9:46:42  3563.6下多单， \nA型错误右图，这里不可以做多，这里可能是周一交易瘾', xy=(dt.datetime(2019,5,27,9,46,42)+dt.timedelta(minutes=90), 3563.6), xytext=(dt.datetime(2019,5,27,9,46,42)+dt.timedelta(minutes=70) , 3563.6-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")          

        plt.annotate(U'10:13:3  3554平多单， \n正确\n这时判断 3550守不住是对的， 没敢转空也对\n但是，之前为什么不平多， 还是有侥幸心理', xy=(dt.datetime(2019,5,27,10,13,3)+dt.timedelta(minutes=90), 3554), xytext=(dt.datetime(2019,5,27,10,13,3)+dt.timedelta(minutes=110) , 3554+10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center") 

        plt.annotate(U'13:06:19  3575下空单， \n被洗脑错误，在正V或者反V的后半段与趋势逆反，是主力的心理学陷阱\n此外， 这里是三分钟级别 3577顶点的第三次出现， 等于说主力已经2次诱导在这个位置做空了', xy=(dt.datetime(2019,5,27,13,6,19), 3575), xytext=(dt.datetime(2019,5,27,13,6,19)-dt.timedelta(minutes=10), 3575+10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'blue'},
            va = "bottom", ha="center")  
        plt.annotate(U'13:08:52  曾试图在 3569 平空， 但因3569停留时间过短未成功 ', xy=(dt.datetime(2019,5,27,13,8,52), 3569), xytext=(dt.datetime(2019,5,27,13,8,52)+dt.timedelta(minutes=10), 3569-10),
            arrowprops={'arrowstyle': '->', 'lw': 4, 'color': 'red'},
            va = "bottom", ha="center")             
    if tablename == 'if1906_20190529':
        plt.figtext(0,.85,'周三，缓涨到1点40至 3650 ， 急涨10分钟到 3670 之后下跌， 尾盘做出坚守姿态到最后10分钟，利用了昨天的尾盘涨20点，吸引抢反弹\n期初一空一多，\n随波逐流单: 1\n逆市单: 3')
        
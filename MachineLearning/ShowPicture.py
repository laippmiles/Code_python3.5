def show2d(x,y):
    import matplotlib.pyplot as plot
    #原称呼太鸡儿长了，用as起个外号
    plot.scatter(x,y,marker='.', color='dodgerblue', s=10)
    #  s为设置点大小的参数
    # 关于颜色与线型设定见 http://blog.csdn.net/qq_26376175/article/details/67637151
    plot.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    plot.rcParams['axes.unicode_minus']=False #用来正常显示负号
    #scatter:散点图
    plot.title("假装此处有网站流量数据")
    plot.xlabel('Time')
    plot.ylabel('Hits/hour')
    plot.xticks([W*7*24 for W in range(10)],['第 %i 周' %w for w in range(10)])
    #xtrick :第一个[]中表明设定的数字刻度，第二个[]写明显示的便签文本
    plot.autoscale(tight=True)
    plot.grid()

def ShowPlot():
    import matplotlib.pyplot as plot
    plot.show()
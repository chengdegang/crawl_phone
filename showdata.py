import pandas as pd
from pyecharts.charts import Pie
from pyecharts import options as opts

provinces = ['beijing','shanghai','zhejiang']
num = [1,2,3]
color_series = ['#FAE927','#E9E416','#C9DA36']

df = pd.DataFrame({'provinces':provinces,'num':num})
df.sort_values(by='num',ascending=False,inplace=True)

v = df['provinces'].values.tolist()
d = df['num'].values.tolist()

pie = Pie(init_opts= opts.InitOpts(width='1350px',height='750px'))

pie.set_colors(color_series)

pie.add('',[list(z) for z in zip(v,d)],
        radius=['10%','90%'],
        center=['50%','65%'],
        rosetype='area')

pie.set_global_opts(title_opts=opts.TitleOpts(title='示例'),
                    legend_opts=opts.LegendOpts(is_show=False),
                    toolbox_opts=opts.ToolboxOpts())

pie.set_series_opts(label_opts=opts.LabelOpts(is_show=True,
                                              position='inside',
                                              font_size=12,
                                              formatter='{b}:{c}day',
                                              font_style='italic',
                                              font_weight='bold',
                                              font_family='Microsoft YaHei'),
                    )

pie.render('示例.html')
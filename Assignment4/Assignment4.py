import pandas
import matplotlib.pyplot as plt
from plotly.offline import plot
import plotly.graph_objs as go

#dtypes = {'professor': 'float', 'lecture':'float', 'participants': 'float', 'professional expertise': 'float', 'motivation': 'float','clear presentation': 'float', 'overall': 'float'}
data = pandas.read_csv('DataWeierstrass.csv',sep=";")
data.professor=data.professor.str[4:].astype(float)
data.lecture=data.lecture.str[8:].astype(float)
#data = data.iloc[i],
from pandas.plotting import scatter_matrix,parallel_coordinates
scatter_matrix(data,figsize=(9,9),alpha=0.6,range_padding=0.05)
plt.show()








data1 = [
    go.Parcoords(
        line = dict(color = data['professor'],
                   colorscale = [[0,'#D7C16B'],[0.5,'#23D8C3'],[1,'#F3F10F']]),
        dimensions = list([
            dict(range = [0,45],

                label = 'professor', values = data['professor']),
            dict(range = [0,100],
                label = 'lecture', values = data['lecture']),
            dict(range = [3,330],
                label = 'participants', values = data['participants']),
            dict(range = [0,4.5],
                label = 'professional expertise', values = data['professional expertise']),
            dict(range = [0,4.5],
                label = 'motivation', values = data['motivation']),
            dict(range = [0,4.5],
                label = 'clear presentation', values = data['clear presentation']),
            dict(range = [0,4.5],
                label = 'overall impression', values = data['overall impression'])
        ])
    )
]

print(data1)
layout = go.Layout(
    plot_bgcolor = '#E5E5E5',
    paper_bgcolor = '#E5E5E5'
)


fig = go.Figure(data = data1, layout = layout)
#Ploting image offline that can then be downloaded as png
plot(fig, filename = 'parallel_cordinate.html', image='png')
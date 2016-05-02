from datetime import datetime
import plotly
from plotly.graph_objs import Bar, Scatter, Layout
import shutil
import random

def plot_ages(ages):
    plotly.offline.plot({
        "data":[Bar(x=ages,y=[ages.count(age) for age in ages],text="ages")],
        "layout":Layout(
            title="The frequency of ages of people applying for benefits"
            )
        })
    shutil.move("temp-plot.html","templates/ages.html")

if __name__ == '__main__':
    ages = [random.randint(0,100) for _ in range(1000)]
    plot_ages(ages)

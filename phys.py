import io
import pandas as pd
import panel as pn
import seaborn as sns
from matplotlib.figure import Figure
from pyodide.http import open_url


def to_plot():
    data = pd.read_csv("./survey.csv")
    x = data['phys_health_interview'] 
    
    fig = Figure(figsize=(6.5, 3.5))
    ax = fig.add_subplot(111)
    
    sns.countplot(x=x, data=data, ax=ax)
    
    return fig

pn.Column(
    to_plot
).servable(target="phys")
None # For some reason an error is raised if I end with .servable()




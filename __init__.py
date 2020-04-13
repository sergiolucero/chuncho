####################################  ESSENTIAL I/O LIBRARIES
import pandas as pd
import geopandas as gp
import folium
####################################  COMMONLY USED I/O LIBRARIES
import s3fs		# test if needed
import requests
from bs4 import BeautifulSoup as bs
####################################  COMMONLY USED I/O LIBRARIES
import altair
import seaborn
import plotly

def read_frame(source, *args):
    if source.contains('.csv'):     # comma separated values, could be gzipped!
        df = pd.read_csv(source, *args)     # eg: delimiter=';'
    elif source.endswith('.xlsx'):     # Excel
        df = pd.read_csv(source, *args)     # eg: sheet_name = None
    elif source.endswith('.json'):     # JSON
        df = pd.read_csv(source, *args)     # eg: orient='records'
    else:
        raise Exception('could not handle SOURCE:', source)
    return df
    
def plot(
        
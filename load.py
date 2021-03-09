from IPython.display import HTML
import pandas as pd
import numpy as np
import base64
import sqlite3


def create_download_link(df, title="Download CSV file", filename="nba.csv"):
    csv1 = df.to_csv()
    b64 = base64.b64encode(csv1.encode())
    payload = b64.decode()
    html = '<a download="{filename}" href="data:text/csv;base64,{payload}" target="_blank">{title}</a>'
    html = html.format(payload=payload, title=title, filename=filename)
    return HTML(html)


# create a random sample dataframe
df = pd.DataFrame(np.random.randn(23521, 11), columns=list('ABCDEFGHIJK'))


# create a link to download the dataframe
create_download_link(df)


con = sqlite3.connect('nba.sqlite')  # change to 'sqlite:///your_filename.db'
cur = con.cursor()
cur.execute("CREATE TABLE nbafirst (col1, col2,col3,col4,col5,col6,col7,col8,col9,col10,col11);")  # use your column names here





con.commit()
con.close()

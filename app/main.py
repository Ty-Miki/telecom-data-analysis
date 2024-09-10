from utils import StreamlitAPP

import os, sys
from pathlib import Path

current_directory = Path(__file__).parent
top_10_handset_path = str(current_directory) + '\\data\\top_10_handsets.pkl'

if __name__ == '__main__':
    app = StreamlitAPP()
    top_10_handset = app.load_dataframe(picke_path=top_10_handset_path)

    app.display_dataframe(df=top_10_handset,
                          title='Top 5 Handsets Used By Customers')
    app.plot_bar_chart(df=top_10_handset,
                       title='Bar Chart: Top 10 Handsets Used By Customers',
                       x_label='Handset Type',
                       y_label='Count')
    
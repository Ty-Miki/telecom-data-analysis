from utils import StreamlitAPP

import os, sys
from pathlib import Path

current_directory = Path(__file__).parent
top_10_handset_path = str(current_directory) + '\\dashboard_data\\top_10_handsets.pkl'
avearge_engagement_metric_path = str(current_directory) + '\\dashboard_data\\average_engagement.pkl'
top_10_satisfied_path = str(current_directory) + '\\dashboard_data\\top_10_satisfied.pkl'

if __name__ == '__main__':
    app = StreamlitAPP()

    # Deploy top 10 handsets
    top_10_handset = app.load_dataframe(picke_path=top_10_handset_path)

    app.display_dataframe(df=top_10_handset,
                          title='Top 10 Handsets Used By Customers')
    app.plot_bar_chart(df=top_10_handset,
                       title='Bar Chart: Top 10 Handsets Used By Customers',
                       x_label='Handset Type',
                       y_label='Count')
    
    # Deploy Average engagement metric
    avearge_engagement_metric = app.load_dataframe(picke_path=avearge_engagement_metric_path)

    app.display_dataframe(df=avearge_engagement_metric,
                          title='Average engagement metric per cluster')
    app.plot_bar_chart(df=avearge_engagement_metric,
                       title='Bar Chart: Average engagement metric per cluster',
                       x_label="Clusters",
                       y_label="Average Value")
    
    # Deploy top 10 satisfied customers
    top_10_satisfied_customers = app.load_dataframe(picke_path=top_10_satisfied_path)

    app.display_dataframe(df=top_10_satisfied_customers,
                          title='Top 10 Satisfied Customers')
    
    app.plot_melted_bar_chart(df=top_10_satisfied_customers,
                              title="Bar Chart: Top 10 Satisfied Customers",
                              x_label="MSISDN/Number",
                              y_label="Score",
                              id_vars='MSISDN/Number',
                              value_vars=['Engagement Score', 'Experience Score', 'Satisfaction Score'],
                              rotation=90)
    
    app.show_correlation_with_heatmap(df=top_10_satisfied_customers,
                                      columns=['Engagement Score', 'Experience Score', 'Satisfaction Score'],
                                      title='Heatmap of Correlations')
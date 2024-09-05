# Detailed Explanation of Tasks

## Task 1: User overview analysis

- This task focuses on understanding **user behavio**r by analyzing device usage and **xDR session data**.
- It involves identifying the top handsets, manufacturers, and user behaviors based on session data. The task requires exploratory data analysis (EDA), addressing missing values and outliers, performing variable transformations, and using both graphical and non-graphical analyses to extract meaningful insights about user activity across different applications.

## Task 2: User Engagement Analysis

- This task tracks user engagement through metrics such as session frequency, duration, and traffic (download/upload).
- It involves aggregating these metrics per customer, normalizing them, and clustering users based on engagement scores using k-means. Key insights are derived through visualizations, identifying top-engaged users, and exploring the most used applications to help optimize network resources and improve user experience.

## Task 3: **User Experience Analytics**

- This task explores customer experience by analyzing network parameters like TCP retransmission, RTT, and throughput, alongside handset characteristics.
- The goal is to identify top, bottom, and frequent values for each metric and segment users into experience-based clusters using k-means clustering. The task helps identify how different network conditions affect user experience and provides recommendations for service improvements.

## Task 4: User Satisfaction Analysis

- Building on engagement and experience scores, this task aims to quantify customer satisfaction.
- It calculates satisfaction scores as the average of engagement and experience scores, identifies top satisfied customers, and builds a regression model to predict satisfaction. The task also involves clustering users based on these scores, exporting the results to a database, and deploying a model using MlOps tools to track its performance over time.

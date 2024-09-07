# Task 2 Summary: User Engagement Analysis

In this task, you will measure and analyze customer engagement based on several metrics: session frequency, session duration, and total traffic (download and upload) per customer. By grouping users based on their engagement, you'll help identify where network resources should be concentrated.

## Sub-tasks

### **Data Aggregation**

* Aggregate the metrics per customer (MSISDN).
* Identify the **top 10 customers** for each metric: session frequency, session duration, and total traffic.

### **Normalization and Clustering**

* Normalize each engagement metric.
* Run a **k-means clustering** (with k=3) to classify customers into three engagement groups.
* Compute the **minimum, maximum, average, and total values** for each engagement metric per cluster.
* Visualize and interpret the results with accompanying explanations.

### **Application-Specific Engagement**

* Aggregate the total traffic per application.
* Find the **top 10 most engaged users** per application.
* Plot the **top 3 most used applications** with appropriate charts.

### **Optimized Clustering**

* Use the **elbow method** to determine the optimal number of clusters (k).
* Interpret findings for customer engagement clusters.

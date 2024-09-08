# **Task 3 Summary: User Experience Analysis**

- In this task, I will analyze the user experience based on network parameters such as TCP retransmission, Round Trip Time (RTT), and throughput. Additionally, I'll incorporate the characteristics of customer devices (handset type) to provide insights into their experiences.
- The goal is to aggregate data, perform clustering, and offer meaningful interpretations of how these network factors affect user experience.

## Sub-tasks

### **Data Aggregation**

 **Objective** : For each customer, aggregate the following metrics:

* **Average TCP retransmission**
* **Average Round Trip Time (RTT)**
* **Handset type**
* **Average throughput**

 **Approach** :

1. **Data Cleaning** : Handle missing values and outliers for these variables:

* Use the **mean** or **mode** (depending on the type of variable) to fill in missing or extreme values.
* This step ensures the aggregated metrics are calculated based on clean data.

2. **Aggregation** :

* For each user, compute the average values of  **TCP retransmission** ,  **RTT** , and  **throughput** .
* Also, extract the **handset type** used by each customer (non-numerical but essential for later analysis).

**Output** : A dataset where each row represents a user and their aggregated network experience data.

---

### **Computing Top, Bottom, and Most Frequent Values**

 **Objective** : Identify and list the top 10, bottom 10, and most frequent values for:

* **TCP retransmission**
* **RTT**
* **Throughput**

 **Approach** :

1. **Top 10** :

* Sort the values for TCP retransmission, RTT, and throughput in descending order and capture the top 10 highest values.

2. **Bottom 10** :

* Sort in ascending order and capture the 10 lowest values.

3. **Most Frequent** :

* For each metric, determine the most frequent values by checking the mode or counting occurrences in the dataset.

 **Output** : You will generate three lists for each metric (top, bottom, and most frequent values) that offer insight into the variability of these network parameters.

---

### **Reporting on Throughput and TCP per Handset**

 **Objective** : Analyze the distribution of user experience metrics per handset type:

1. **Average throughput per handset type** :

* Investigate the distribution of throughput (data speed) across different handset types and interpret whether certain devices have better or worse throughput performance.

2. **Average TCP retransmission per handset type** :

* Similar to throughput, calculate the average TCP retransmission rate for each handset type to understand how different handsets handle network errors.

 **Approach** :

1. **Group by Handset Type** :

* For both metrics (throughput and TCP retransmission), group the data by handset type and compute the average for each group.

2. **Interpretation** :

* Analyze the results to provide insights. For example, you might find that certain handsets consistently show lower throughput or higher retransmission rates, which could be linked to device limitations or network compatibility.

 **Output** : A report that explains the performance of different handsets concerning throughput and TCP retransmission.

---

**K-Means Clustering on User Experience**

 **Objective** : Segment users based on their experience using K-means clustering (with K = 3).

 **Approach** :

1. **Feature Selection** : Use the aggregated user experience metrics you calculated earlier (average TCP retransmission, RTT, and throughput) as input features for clustering.
2. **Perform K-Means Clustering** :

* Use the K-means algorithm with **K=3** to group users into 3 clusters based on their experience metrics.

3. **Cluster Interpretation** :

* Once the users are segmented, analyze the characteristics of each cluster. For example:
  * **Cluster 1** might represent users with high throughput but low TCP retransmission.
  * **Cluster 2** could show users with average metrics across the board.
  * **Cluster 3** may group users with high retransmission and poor throughput.

 **Output** :

* A brief description of each cluster, identifying what makes each user group unique in terms of network experience.

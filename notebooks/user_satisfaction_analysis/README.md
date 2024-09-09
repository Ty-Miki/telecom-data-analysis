# Task 4: User Satisfaction Analysis

- In this task, I will analyze the customer satisfaction in depth based on the engagement analysis and the experience analysis I have conducted before.

## Subtasks

### Top 10 most satisfied customers

#### Steps

- Assign **engagement score** using Euclidean distance from the user to the least engaged cluster.
- Assign **experience score** using Euclidean distance from the user to the worst experience cluster.
- Calculate **satisfaction score** as the average of both engagement and experience scores.
- Extract the **top 10 most satisfied customers** based on the satisfaction score.

### Regression model

- In this subtask I will build a **regression model** to predict the satisfaction score of a customer based on engagement and experience data.

### Kmeans clustering (k=2)

#### Steps

- Perform **k-means clustering (k=2)** using the engagement and experience scores to segment users.
- **Aggregate the average satisfaction and experience scores** per cluster and report the results.
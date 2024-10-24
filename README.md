### Efficient Data Stream Anomaly Detection

### Overview
    This project simulates a continuous data stream and detects anomalies using a Z-Score-based method. 
    The data stream includes noise, seasonal patterns, and injected anomalies (outliers).

### Algorithm
    The project uses a Z-Score-based anomaly detection method,
    where anomalies are defined as data points whose Z-Score exceeds a defined threshold 
    (e.g., 3 standard deviations from the mean)


### What is Z-Score?
- The Z-Score algorithm is a simple statistical method that helps measure how far a particular data point is from the average (mean) of a dataset. It does this by calculating a score called the Z-Score, which tells us how many standard deviations (a measure of how spread out the numbers are) the data point is away from the mean.
The formula for calculating the Z-Score for a data point is:

##      Z-Score = (Data Point - Mean) / Standard Deviation

- A Z-Score of 0 means the data point is exactly at the mean.
- A positive Z-Score means the data point is above the mean.
- A negative Z-Score means the data point is below the mean.

For example:
- If a Z-Score is 2, it means the data point is 2 standard deviations above the average.
- If a Z-Score is -2, it means the data point is 2 standard deviations below the average.

### Why use Z-Score for Anomaly Detection?
The idea is simple:
In anomaly detection, normal data points are typically clustered around the mean, with Z-Scores close to 0. Anomalies, on the other hand, will have Z-Scores that are much larger (positive or negative), meaning they deviate significantly from the mean.

- Normal data points will have Z-Scores close to 0 (because they are close to the average).
- Anomalies (outliers) will have Z-Scores that are much higher or lower than the average (far from 0).
We set a threshold (e.g., Z-Score > 3 or Z-Score < -3). Any data point whose Z-Score exceeds this threshold is flagged as an anomaly because it's much higher or lower than what we would expect from normal data.

### How the Algorithm Works:
1. Rolling Window: We use a window of recent data points (e.g., the last 50 points).
2. Calculate Mean and Standard Deviation: We calculate the mean and standard deviation of the data points in that window.
3. Compute Z-Score: For each new data point, we calculate its Z-Score based on the current mean and standard deviation.
4. Flag Anomalies: If the Z-Score exceeds the threshold, we flag it as an anomaly.

### Why We Need This?
- In real-world data (like financial transactions, sensor readings, or system metrics), unexpected behavior can occur. These unexpected points are called anomalies.
- Anomalies could indicate important events (fraud, system malfunction, or unusual spikes).
- Detecting these anomalies is crucial to respond to them quickly and appropriately.

### Why Use Z-Score?
- Simplicity: Z-Score is easy to understand and compute. It’s based on basic statistics (mean and standard deviation).
- Real-Time Capability: Since it works with a rolling window, it can easily be applied to real-time data streams.
- Efficient: The Z-Score calculation is fast and can work well even for large data streams.
  
### Why Prefer This Method?
- Straightforward: You don’t need to train complex models or use lots of historical data. It works well for continuous data.

- Real-Time Detection: The Z-Score method is great for streaming or continuous data. By using a rolling window (i.e., looking at the most recent data points), you can calculate the Z-Score in real-time and flag anomalies as they happen. It adapts quickly to new data and is computationally efficient, making it suitable for applications that need immediate anomaly detection (e.g., monitoring system health, detecting fraud).

- Customizable Sensitivity: You can adjust the threshold (e.g., 2, 3, or more standard deviations) depending on how sensitive you want the algorithm to be. For example, if you only want to catch major anomalies, you might use a threshold of 3 or 4. If you want to catch smaller deviations, you could lower the threshold to 2.

- Versatile and Lightweight: Z-Score is not tied to any specific domain or data type. Whether you're analyzing financial transactions, sensor data, or website traffic, Z-Score works for most numerical data.
Since it only requires calculating mean and standard deviation, it doesn’t demand heavy computational resources, making it great for large-scale or fast-moving data streams.

### Visualization
The script visualizes the real-time data stream and highlights detected anomalies using matplotlib.
    
## Created Python Scripts

1. anomaly_detection.py
This script will contain the anomaly detection logic using a Z-Score-based algorithm.

2. data_stream.py
This script will generate the data stream with seasonal elements, noise, and occasional anomalies

3. visualize.py
This script will handle real-time visualization using matplotlib.

4. main.py
This is the main script that will tie everything together.

5. Created a packages.txt file to manage the required dependencies:
    => numpy 
    => matplotlib
    Run the following command to install the necessary libraries
    => pip install -r packages.txt

## How to Run
    Run the main.py script to simulate the data stream, detect anomalies, and visualize the results:
    python main.py



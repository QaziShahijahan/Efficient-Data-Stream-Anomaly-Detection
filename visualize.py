import matplotlib.pyplot as plt

def visualize_data_stream(data_stream, anomalies):
    """
    Visualize the data stream and highlight anomalies.
    
    Parameters:
        data_stream (list): List of data points in the stream.
        anomalies (list): List of detected anomalies (index, value).
    """
    plt.ion()
    fig, ax = plt.subplots()
    
    for i, point in enumerate(data_stream):
        ax.clear()
        ax.plot(data_stream[:i], label='Data Stream')
        anomaly_points = [a[1] for a in anomalies if a[0] <= i]
        anomaly_indices = [a[0] for a in anomalies if a[0] <= i]
        ax.scatter(anomaly_indices, anomaly_points, color='r', label='Anomalies')
        ax.legend()
        plt.pause(0.01)  # Simulate real-time plotting
    
    plt.ioff()
    plt.show()

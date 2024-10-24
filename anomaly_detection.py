import numpy as np
from collections import deque

def detect_anomalies(data_stream, window_size, threshold):
    """
    Detect anomalies in the data stream.
    
    Parameters:
        data_stream (list): The data stream to analyze.
        window_size (int): Size of the rolling window for mean and std deviation.
        threshold (float): Z-score threshold for anomaly detection.
        
    Returns:
        list: Indices and values of detected anomalies.
    """
    rolling_window = deque(maxlen=window_size)
    anomalies = []
    
    for i, data_point in enumerate(data_stream):
        rolling_window.append(data_point)
        if len(rolling_window) == window_size:
            mean = np.mean(rolling_window)
            std = np.std(rolling_window)
            z_score = (data_point - mean) / std
            if abs(z_score) > threshold:
                anomalies.append((i, data_point))
    
    return anomalies
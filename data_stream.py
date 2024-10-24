import numpy as np

def generate_data_stream(length=1000, seasonality=True, noise_level=0.1, anomaly_frequency=0.05):
    """
    Generate a synthetic data stream with noise and anomalies.
    
    Parameters:
        length (int): The number of data points to generate.
        seasonality (bool): Whether to include a sinusoidal pattern.
        noise_level (float): The level of random noise in the stream.
        anomaly_frequency (float): Probability of injecting an anomaly.
        
    Returns:
        list: A simulated data stream with anomalies.
    """
    np.random.seed(42)
    data_stream = []
    for i in range(length):
        value = np.sin(i / 50) if seasonality else 0  # Regular pattern
        value += noise_level * np.random.randn()  # Random noise
        if np.random.rand() < anomaly_frequency:  # Inject anomaly
            value += np.random.choice([5, -5])  # Large positive or negative spike
        data_stream.append(value)
    return data_stream

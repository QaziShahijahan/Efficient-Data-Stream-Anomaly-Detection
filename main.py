from data_stream import generate_data_stream
from anomaly_detection import detect_anomalies
from visualize import visualize_data_stream

def main():
    """
    Main function to generate a data stream, detect anomalies, and visualize the result.
    """
    # Step 1: Generate data stream
    print("Generating data stream...")
    data_stream = generate_data_stream(length=1000, seasonality=True, noise_level=0.1, anomaly_frequency=0.05)
    
    # Step 2: Detect anomalies from the beginning
    print("Detecting anomalies...")
    anomalies = detect_anomalies(data_stream, window_size=50, threshold=3)
    print(f"Detected {len(anomalies)} anomalies.")
    
    # Step 3: Visualize results excluding the first 100 data points
    visualize_data_stream(data_stream[100:], [(i-100, val) for i, val in anomalies if i >= 100])

if __name__ == "__main__":
    main()
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def visualize_dataset(dataset_path):
    # Read the dataset into a Pandas DataFrame
    df = pd.read_csv(dataset_path)
    
    # Visualize the dataset using plot()
    print("Visualizing the dataset using plot():")
    df.plot()
    plt.show()
    
    # Draw Scatter plot for a specific column with different colors
    print("\nDrawing a Scatter plot for a specific column with different colors:")
    plt.scatter(df.index, df['sepal.width'], c=np.arange(len(df)), cmap='viridis')
    plt.colorbar(label='Index')
    plt.xlabel('Index')
    plt.ylabel('sepal.width')
    plt.title('Scatter Plot')
    plt.show()
    
    # Draw Histogram for a specific column
    print("\nDrawing a Histogram for a specific column:")
    df['sepal.width'].plot(kind='hist', bins=10)
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title('Histogram of Column2')
    plt.show()

def main():
    # Path to your dataset (replace with your actual dataset path)
    dataset_path = '/Users/jeevans/Python/iris.csv'
    
    # Call the function to visualize the dataset
    visualize_dataset(dataset_path)

if __name__ == "__main__":
    main()

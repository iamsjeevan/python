import pandas as pd

def main():
    # Replace 'path/to/iris.csv' with the actual path to your downloaded Iris dataset
    file_path = '/Users/jeevans/Python/iris.csv'
    
    # Read the Iris dataset from the local CSV file
    df = pd.read_csv(file_path)

    # Display first 5 rows of the dataset
    print("First 5 rows of the dataset:")
    print(df.head())
    print("\n")

    # Display last 5 rows of the dataset
    print("Last 5 rows of the dataset:")
    print(df.tail())
    print("\n")

    # Display information about the dataset
    print("Information about the dataset:")
    print(df.info())
    print("\n")

    # Display overview of the values of each column
    print("Overview of the values of each column:")
    print(df.describe())
    print("\n")

    # Visualize the dataset using plot()
    # Scatter plot of sepal length vs sepal width
    df.plot(kind='line', subplots=True, layout=(2, 2), sharex=False, title='Line Plots of Each Feature')


if __name__ == "__main__":
    main()

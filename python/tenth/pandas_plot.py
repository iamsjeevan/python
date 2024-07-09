import pandas as pd

def main():
    file_path = '/Users/jeevans/Python/iris.csv'
    
    df = pd.read_csv(file_path)

    print("First 5 rows of the dataset:")
    print(df.head())
    print("\n")

    print("Last 5 rows of the dataset:")
    print(df.tail())
    print("\n")

    print("Information about the dataset:")
    print(df.info())
    print("\n")

    print("Overview of the values of each column:")
    print(df.describe())
    print("\n")

    
    #df.plot(kind='line', subplots=True, layout=(2, 2), sharex=False, title='Line Plots of Each Feature')


if __name__ == "__main__":
    main()

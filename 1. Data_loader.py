import pandas as pd

def main():
    # Load the data
    df = pd.read_table('data/Test01_wrist.txt', skiprows=30, header=0, sep=';')
    print(df.head())

if __name__ == "__main__":
    main()
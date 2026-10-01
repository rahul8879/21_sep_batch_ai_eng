import pandas as pd


def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


def basic_stats(df):
    count = df.shape[0]
    mean = df.mean()
    std = df.std()
    return {"count": count, "mean": mean, "std": std}


def main():
    file_path = "data.csv"
    df = load_data(file_path)
    stats = basic_stats(df)
    print(stats)

main()

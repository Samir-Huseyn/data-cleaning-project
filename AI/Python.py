import pandas as pd

df = pd.read_csv("my_file.csv")

print(df.info())
print(df.head())
print(df.shape)

df.columns = df.columns.str.replace(r'\s+', ' ', regex=True).str.strip()
df.drop(columns=["Ref."], inplace=True)

df["Actual gross"] = df["Actual gross"].str.replace(r"[^\d.]", "", regex=True).astype(float)
df["Average gross"] = df["Average gross"].str.replace(r"[^\d.]", "", regex=True).astype(float)


df["Peak"] = df["Peak"].str.extract("(\d+)")
df.dropna(subset=["Peak"], inplace=True)
df["Peak"] = df["Peak"].astype(int)

df["Tour title"] = df["Tour title"].str.replace(r"\[.*?\]", "", regex=True).str.strip()

print("\nCleaned data info:")
print(df.info())
import pandas as pd

data = {
    "Name": ["Manasa", "Anagha", "Harsha"],
    "Marks": [95, 88, 76],
    "City": ["Pileru", "Hyderabad", "Tirupati"]
}

df = pd.DataFrame(data)

print("===== Student Data Analysis =====\n")

print("Student Records:\n")
print(df)

print("\nTotal Students:")
print(len(df))

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nLowest Marks:")
print(df["Marks"].min())
print("\nStudent with Highest Marks:")
print(df.loc[df["Marks"].idxmax()])
print("\nStudent with Lowest Marks:")
print(df.loc[df["Marks"].idxmin()])
import pandas as pd

# Data and labels
details = [
    ["sagar", 20, 10000],
    ["Daniel", 16, 20000],
    ["Veeru", 24, 30000],
    ["Raju", 25, 40000],
    ["kiran", 26, 50000],
    ["kedar", 27, 60000],
    ["reena", 28, 70000],
    ["kartik", 29, 80000],
    ["satis", 30, 90000],
]
inx = ["Row1","Row2","Row3","Row4","Row5","Row6","Row7","Row8","Row9"]
cols = ["Name","Age","Salary"]

# Create DataFrame
df = pd.DataFrame(details, index=inx, columns=cols)

# Display it
print(df)

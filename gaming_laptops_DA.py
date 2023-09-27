import pandas as pd
import numpy as np

df = pd.DataFrame(columns=["Name", "Price"])
print(df)

df.loc[len(df.index)] = ["ASUS", 19870]

print(df)
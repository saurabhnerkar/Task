import pandas as pd

def fill_income(df):
    skew_value =df['Income'].skew()

    if abs(skew_value) <=  0.5:
        fill_value = df['Income'].median()
    else:
        fill_value = df['Income'].mode()[0]

    df["Income"] =df["Income"].fillna(fill_value)
    return df


df = pd.DataFrame({
    'Income': [50000, 60000, None, 55000, None, 70000, 80000, None]
})

df = fill_income(df)
print("after filling the mising value : ",df)
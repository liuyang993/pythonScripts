import pandas as pd

df = pd.DataFrame({
    'date':  ['01-01','01-02','01-03','01-04','01-05','01-06','01-07'],
    'value': [10, 4, 3, 4, 1, 6, 4],
})


# print(df.iloc[1])

# print(df.iloc[:, 0])

# print(df.iloc[-1])


def func(window):
    print(window)
    mask = (window > window.iloc[-1] )
    # print(window.iloc[-1])
    rows = window[mask]  # all previous values grater then current value 
    # print(rows)
    value = rows.min()   # minimal value 
    return value

df['prev_gt_curr'] = df.expanding().apply(func)

# print(df)
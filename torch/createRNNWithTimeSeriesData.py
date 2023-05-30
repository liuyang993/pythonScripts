# https://towardsdatascience.com/building-rnn-lstm-and-gru-for-time-series-using-pytorch-a46e5b094e7b

import plotly.graph_objs as go
from plotly.offline import iplot

def plot_dataset(df, title):
    data = []
    value = go.Scatter(
        x=df.index,
        y=df.value,
        mode="lines",
        name="values",
        marker=dict(),
        text=df.index,
        line=dict(color="rgba(0,0,0, 0.3)"),
    )
    data.append(value)

    layout = dict(
        title=title,
        xaxis=dict(title="Date", ticklen=5, zeroline=False),
        yaxis=dict(title="Value", ticklen=5, zeroline=False),
    )

    fig = dict(data=data, layout=layout)
    iplot(fig)

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('hourlycsvdata/PJME_hourly.csv')


df = df.set_index(['Datetime'])
df.index = pd.to_datetime(df.index)
if not df.index.is_monotonic:
    df = df.sort_index()
    
df = df.rename(columns={'PJME_MW': 'value'})


print(df.head())

# columns = df.columns
# for col in columns:
#     print(col)



# plot_dataset(df, title='PJM East (PJME) Region: estimated energy consumption in Megawatts (MW)')


def generate_time_lags(df, n_lags):
    df_n = df.copy()
    for n in range(1, n_lags + 1):
        df_n[f"lag{n}"] = df_n["value"].shift(n)
    df_n = df_n.iloc[n_lags:]
    return df_n
    
input_dim = 100

df_generated = generate_time_lags(df, input_dim)

# print(df_generated)



df_features = (
                df
                .assign(hour = df.index.hour)
                .assign(day = df.index.day)
                .assign(month = df.index.month)
                .assign(day_of_week = df.index.dayofweek)
                .assign(week_of_year = df.index.week)
              )

print(df_features.head())


def onehot_encode_pd(df, col_name):
    dummies = pd.get_dummies(df[col_name], prefix=col_name)
    # return pd.concat([df, dummies], axis=1).drop(columns=[col_name])
    return pd.concat([df, dummies], axis=1)

df_features = onehot_encode_pd(df_features, ['month','day','day_of_week','week_of_year'])

# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder

# def onehot_encode(df, onehot_columns):
#     ct = ColumnTransformer(
#         [('onehot', OneHotEncoder(drop='first'), onehot_columns)],
#         remainder='passthrough'
#         )
#     return ct.fit_transform(df)

# onehot_columns = ['hour']
# onehot_encoded = onehot_encode(df_features, onehot_columns)


# print(onehot_encoded)
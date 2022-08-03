import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#create DataFrame
df = pd.DataFrame({'x': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180,
                             190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350],
                   'y': [1.4272727409039099, 0.6363636154159434, 0.7545454310449746, 0.3090909127647661, 0.7999999993011164,
                    0.35454540244331567, -0.454545416974063, 0.5181818050024619, 0.10000000703838598, 0.23636362648063777, -0.05454544601565627, 
                    -0.9727272383598817, 0.35454546417520644, 0.23636364593923043, 0.9727272181095323, 0.5181818239566522, 0.11818183165236329,
                     -0.37272726785483146, 0.5727272678908282, 0.25454545444091053, 0.19090907155112546, 0.29090908721582714, -0.16363636695565406,
                      -0.44545453619607034, 0.6272727106526922, 0.01818182071108427, -0.5636363616932474, -0.5999999612289687, 0.9363635943047326,
                       0.936363610358947, 1.1272726829890305, 2.199999920758933, -0.18181816915158405, 0.37272724822375936, 0.6636363355678203]})


#fit polynomial models up to degree 5
model1 = np.poly1d(np.polyfit(df.x, df.y, 1))
model2 = np.poly1d(np.polyfit(df.x, df.y, 2))
model3 = np.poly1d(np.polyfit(df.x, df.y, 3))
model4 = np.poly1d(np.polyfit(df.x, df.y, 4))
model5 = np.poly1d(np.polyfit(df.x, df.y, 5))
# print(model5)

#create scatterplot
polyline = np.linspace(10, 350, 10)
plt.scatter(df.x, df.y)

#add fitted polynomial lines to scatterplot 
plt.plot(polyline, model1(polyline), color='green')
plt.plot(polyline, model2(polyline), color='red')
plt.plot(polyline, model3(polyline), color='purple')
plt.plot(polyline, model4(polyline), color='blue')
plt.plot(polyline, model5(polyline), color='orange')
plt.show()



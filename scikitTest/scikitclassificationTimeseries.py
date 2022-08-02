# 怎么用 sklearn 给 time series 分类 ， 想实时判断是在涨势还是跌势之中 


# 参考资料 ： https://stackoverflow.com/questions/57371065/how-to-use-time-series-data-in-classification-in-sklearn 
#            



from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.ensemble import RandomForestClassifier
import numpy as np

n_samples = 100

# generates 2 n_samples random time series with integer values from 0 to 100.
x1 = np.array([np.random.randint(0, 100, 5) for _ in range(n_samples)])
x2 = np.array([np.random.randint(0, 100, 5) for _ in range(n_samples)])

# print(x1)
# print('--------------------------------')
# print(x2)


X = np.hstack((x1, x2))


# generates n_samples random binary labels.
y = np.random.randint(0, 2, n_samples)

#Random Forest classifier
clf=RandomForestClassifier(random_state = 42, class_weight="balanced", criterion = 'gini', max_depth = 3, max_features = 'auto', n_estimators = 500)

k_fold = StratifiedKFold(n_splits=10, shuffle=True, random_state=0)

output = cross_validate(clf, X, y, cv=k_fold, scoring = 'roc_auc', return_estimator =True)

print(output)

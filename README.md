# pythonscripts


## 数学名字对照 

   二元方程                         <br>
   导数        derivative <br>
   偏导数 partial derivative  <br>
   单增函数  increasing function <br>
   线性规划  Linear Programming <br>
   有监督机器学习  Supervised Learning <br>
   监督机器学习有两种  Classification  分类法-函数的输出结果是某几项，比如红，蓝 或者 涨，跌 <br>
                     Regression    输出是实数值，比如美元或者重量 <br>


### 2022-08-02 
   <pre>学习怎么用 sklearn 对时间序列分类，能实时判断当前是在涨势还是跌势当中 </pre>

   #### 名词 
   classifier  分类器 (分类器有很多 包括决策树等等)<br>
   train_test_split 数据分组 分成训练组和验证组<br>
   X_train, X_test, y_train, y_test 到底是什么意思 <br>
   <p >X_train, X_test, y_train, y_test = train_test_split 
   X_train 是从样本中取样，取多少由 test_size决定，如果 test_size = 0.4，
   那就是取百分之60</p>
   <p> X_test就是剩下的百分之40样本，这部分样本不参与训练， 而一旦训练得出一个函数，用这个函数代入 X_test的值，检查函数的结果与真实值之间的差距，并由此判断训练是否准确</p>
   <p> y_train 就是 X_train的正确值 </p>
   </p>  y_test  是 x_train 的正确值 </p>
   <p>  random_state  随机数种子控制每次划分训练集和测试集的模式，其取值不变时划分得到的结果一模一样，其值改变时，划分得到的结果不同。若不设置此参数，则函数会自动选择一种随机模式，得到的结果也就不同。</p>


   #### 资料文档
   https://stackabuse.com/overview-of-classification-methods-in-python-with-scikit-learn/  <br>
   
   https://towardsdatascience.com/exploring-classifiers-with-python-scikit-learn-iris-dataset-2bcb490d2e1b <br>

   https://www.cnblogs.com/andy0816/p/15925285.html  这个重要 <br>

   


   <p>In a machine learning context, classification is a type of supervised learning. Supervised learning means that the data fed to the network is <strong>already labeled</strong></p>

   
   
   ## 备注 

   ### 删除 pythoncache文件夹， 在github ，来自 https://stackoverflow.com/questions/71922766/removing-pycache-from-git-repository
   

   <p>You cannot remove files from existing commits: those commits are frozen for all time. You can make sure you do not add new files to future commits, though. Simply remove the files now, with git rm -r --cached __pycache__, and list __pycache__ or __pycache__/ in your .gitignore (creating this .gitignore file if needed). Do this for each __pycache__ directory; use your OS's facilities to find these (e.g., find . -name __pycache__ -type d). Then git add .gitignore and git commit to commit the removal. </p>
   
   
   ## stackoverflow 专家
   
   ManojK  python AI <br>
   


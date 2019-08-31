# # %matplotlib inline
# # 内嵌绘图
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# from sklearn.datasets import load_iris
#
# iris = load_iris()
# # 把数据转换成dataframe的格式
# iris_d = pd.DataFrame(iris['data'], columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])
# iris_d['Species'] = iris.target
#
# def plot_iris(iris, col1, col2):
#     sns.lmplot(x = col1, y = col2, data = iris, hue = "Species", fit_reg = False)
#     plt.xlabel(col1)
#     plt.ylabel(col2)
#     loc = 'left'
#     font_dict = {'fontsize': 14,
#                  'fontweight': 8.2,
#                  'verticalalignment': 'baseline',
#                  'horizontalalignment': loc}
#     plt.title('鸢尾花种类分布图', fontdict=font_dict)
#     plt.show()
# plot_iris(iris_d, 'Petal_Width', 'Sepal_Length')





# 导包
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# 1.获取数据集
iris = load_iris()
# print(iris)
# 2.数据基本处理
# x_train,x_test,y_train,y_test为训练集特征值、测试集特征值、训练集目标值、测试集目标值
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)

# 3、特征工程：标准化
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)

# 4、机器学习(模型训练)
estimator = KNeighborsClassifier(n_neighbors=9)
print('-----', estimator)
estimator.fit(x_train, y_train)
# 5、模型评估
# 方法1：比对真实值和预测值
y_predict = estimator.predict(x_test)
print("预测结果为:\n", y_predict)
print("比对真实值和预测值：\n", y_predict == y_test)
# 方法2：直接计算准确率
score = estimator.score(x_test, y_test)
print("准确率为：\n", score)
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

iris = datasets.load_iris()
X = pd.DataFrame(iris.data)
X.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']
y = pd.DataFrame(iris.target)
y.columns = ['Targets']

model = KMeans(n_clusters=2)
model.fit(X)
model = KMeans(n_clusters=2)
model.fit(X)
colormap = np.array(['red', 'blue', 'orange'])

plt.subplot(2,2,1)
plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[y.Targets], s=40)
plt.title('Real Clusters')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')

plt.subplot(2, 2, 2)
plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[model.labels_], s=40)
plt.title('K-Means clustering')
plt.xlabel('Petal length')
plt.ylabel('Petal width')

from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
scaler.fit(X)
xas = scaler.transform(X)
xs = pd.DataFrame(xas, columns=X.columns)
from sklearn.mixture import GaussianMixture
gmm =GaussianMixture(n_components=3)
gmm.fit(xs)
gmm_y = gmm.predict(xs)
plt.subplot(2, 2, 3)
plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[gmm_y], s=40)
plt.title('gmm clustering')
plt.xlabel('petal length')
plt.ylabel('petal width')
print('observation the gmm using em algorithm based clusterig matched')
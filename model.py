
import pandas as pd
from sklearn.cluster import KMeans


data = pd.read_csv('res_dpre.csv')


X = data[['discounted_price', 'actual_price']]


k = 3


kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X)

labels = kmeans.labels_

cluster_counts = pd.Series(labels).value_counts()


with open('k.txt', 'w') as file:
    for cluster, count in cluster_counts.items():
        file.write(f'Cluster {cluster}: {count} records\n')

import csv
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

with open('wine_dataset.csv', newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    data = [list(map(float, row)) for row in reader]

X = [row[:-1] for row in data]
y = [int(row[-1]) for row in data]

model = KMeans(n_clusters=3, random_state=0)
clusters = model.fit_predict(X)

print("", adjusted_rand_score(y, clusters))

import csv
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

with open('wine_dataset.csv', newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    data = [list(map(float, row)) for row in reader]

X = [row[:-1] for row in data]
y = [int(row[-1]) for row in data]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = RandomForestClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("", accuracy_score(y_test, y_pred))

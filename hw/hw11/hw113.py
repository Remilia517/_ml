import csv
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 讀取 CSV 資料
with open('wine_dataset.csv', newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    data = [list(map(float, row)) for row in reader]

# alcohol 是欄位索引 0（可根據實際 header 調整）
alcohol_index = header.index('alcohol')
target_index = header.index('target')

# 準備資料
X = []
y = []
for row in data:
    features = [v for i, v in enumerate(row) if i != alcohol_index and i != target_index]
    label = row[alcohol_index]  # 將 alcohol 當作預測目標
    X.append(features)
    y.append(label)

# 建模與評估
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("", mean_squared_error(y_test, y_pred))

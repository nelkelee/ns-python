from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# 데이터 불러오기
boston = fetch_openml(name='boston')
X = boston.data
y = boston.target

# 데이터 분할하기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 학습하기
model = LinearRegression()
model.fit(X_train, y_train)

# 모델 평가하기
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

train_mse = mean_squared_error(y_train, y_train_pred)
train_r2 = r2_score(y_train, y_train_pred)

test_mse = mean_squared_error(y_test, y_test_pred)
test_r2 = r2_score(y_test, y_test_pred)

print("Train MSE: {:.2f}, Train R2 Score: {:.2f}".format(train_mse, train_r2))
print("Test MSE: {:.2f}, Test R2 Score: {:.2f}".format(test_mse, test_r2))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# 1 load your retail dataset
df = pd.read_csv('Dataset for Data Analytics - Sheet1.csv')

# 2 X = your clues, y = what you want to guess (OrderStatus)
X = df[['Quantity', 'UnitPrice', 'ItemsInCart', 'TotalPrice']]
y = df['OrderStatus']

# 3 shuffle and Split (80% Training, 20% Testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, shuffle=True)

# 4 feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5 train the KNN Model (Using K=5 as per blueprint)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)

# 6 predict
predictions = model.predict(X_test_scaled)

# 7 output Validation
print("*** PERFORMANCE METRICS ***")
print(f"Overall Accuracy: {accuracy_score(y_test, predictions):.2%}\n")

print("*** DIAGNOSTIC TOOL: CONFUSION MATRIX ***")
print(confusion_matrix(y_test, predictions))

print("\n*** STRATEGIC TRADE-OFFS: PRECISION, RECALL & F1-SCORE ***")
print(classification_report(y_test, predictions))
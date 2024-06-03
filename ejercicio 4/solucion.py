import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

data = pd.read_csv('data_customer_classification.csv')

data['trans_date'] = pd.to_datetime(data['trans_date'])
data['year_month'] = data['trans_date'].dt.to_period('M')
data['tran_amount'] = pd.to_numeric(data['tran_amount'])

frequency = data.groupby(['customer_id', 'year_month']).size().reset_index(name='frequency')
frequency = frequency.groupby('customer_id').size().reset_index(name='frequency')
max_spending = data.groupby('customer_id')['tran_amount'].max().reset_index(name='max_spending')

data = pd.merge(data, frequency, on='customer_id')
data = pd.merge(data, max_spending, on='customer_id')

frequency_thresholds = data['frequency'].quantile([0.33, 0.66])
max_spending_thresholds = data['max_spending'].quantile([0.33, 0.66])

def categorize_customer(row):
    if row['frequency'] <= frequency_thresholds[0.66] and row['max_spending'] <= max_spending_thresholds[0.66]:
        return 'low value'
    elif row['frequency'] > frequency_thresholds[0.66] and row['max_spending'] <= max_spending_thresholds[0.66]:
        return 'medium value'
    else:
        return 'high value'

data['category'] = data.apply(categorize_customer, axis=1)

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(data['category'])

X = data.drop(['customer_id', 'trans_date', 'year_month', 'category'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = Sequential()
model.add(Dense(64, activation='relu', input_dim=X_train.shape[1]))
model.add(Dense(32, activation='relu'))
model.add(Dense(3, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

loss, accuracy = model.evaluate(X_test, y_test)
print("Loss:", loss)
print("Accuracy:", accuracy)

model.save('customer_classification_model.h5')

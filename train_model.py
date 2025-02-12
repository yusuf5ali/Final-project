import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
url = "https://raw.githubusercontent.com/selva86/datasets/master/mtcars.csv"
df = pd.read_csv(url)

# Select features & target
features = ['hp', 'wt', 'cyl']
target = 'mpg'

X = df[features]
y = df[target]

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
with open('mtcars_model.pkl', 'wb') as f:
    pickle.dump(model, f)
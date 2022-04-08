from mongo_access import get_persons
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
data = get_persons('Male')
df = pd.DataFrame(data)
new_df = df[['weight', 'height', 'size_value']].copy()
X = new_df.to_numpy()
y = new_df['size_value'].copy().to_numpy()
Z, f = make_classification(n_samples=1000, n_features=10, n_informative=5, n_redundant=5, n_classes=3, random_state=1)

#train_X, test_X, train_y, test_y = train_test_split(X,y, test_size=0.33, random_state=42)

# define the multinomial logistic regression model
model = LogisticRegression(multi_class='multinomial', solver='lbfgs')
# fit the model on the whole dataset
model.fit(Z, f)
# define a single row of input data
row = [180, 75]
# predict the class label
yhat = model.predict([row])
# summarize the predicted class
print('Predicted Class: %d' % yhat[0])






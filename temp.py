# make a prediction with a multinomial logistic regression model
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression



def get_df ():
    from mongo_access import get_persons
    import pandas as pd
    data = get_persons('Male')
    df = pd.DataFrame(data)
    new_df = df[['weight', 'height', 'size_value']].copy()
    X = new_df.to_numpy()
    y = new_df['size_value'].copy().to_numpy()
    y = y.astype('float64')
    return X, y



X, y = get_df()
Z, f = make_classification(n_samples=1000, n_features=10, n_informative=5, n_redundant=5, n_classes=3, random_state=1)
model = LogisticRegression(multi_class='multinomial', solver='lbfgs')
# fit the model on the whole dataset
model.fit(X, y)
# define a single row of input data
row = [1.89149379, -0.39847585, 1.63856893, 0.01647165, 1.51892395, -3.52651223, 1.80998823, 0.58810926, -0.02542177, -0.52835426]
# predict the class label
yhat = model.predict([row])
# summarize the predicted class
print('Predicted Class: %d' % yhat[0])


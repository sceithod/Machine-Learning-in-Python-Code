import numpy as np
import pandas as pd

# Load data

dataset = open("Info.txt", "r")
s=dataset.read()    
       
data=pd.read_csv("Dataset\\"+s)

print(data.head())


X=data
y=data


from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)




from sklearn.neural_network import MLPClassifier


clf = MLPClassifier(hidden_layer_sizes=(6,5),
                    random_state=5,
                    verbose=True,
                    learning_rate_init=0.01)

clf.fit(X_train,y_train)



ypred=clf.predict(X_test)


from sklearn.metrics import accuracy_score

accuracy_score(y_test,ypred)

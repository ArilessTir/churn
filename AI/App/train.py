from statistics import mode
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
import pickle
import pandas as pd

from pipeline import Log_reg


data = pd.read_csv('../Data/Churn_Modelling.csv', index_col="RowNumber")


X = data.drop('Exited', axis=1)
y = data['Exited']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=400)

model = Log_reg.fit(X_train, y_train)
s_training = model.score(X_train, y_train)
s_test = model.score(X_test, y_test)
pred_test = model.predict(X_test)
pred_train = model.predict(X_train)
f1_test = f1_score(y_test, pred_test)
f1_train = f1_score(y_train, pred_train)

print(
    f'Voulez vous sauvegarder ce modele \nS_training : {s_training}\nS_test : {s_test}\n F1_training : {f1_train}\nF1_test : {f1_test}\n')
answer = input('O/N? :')

if answer == 'O' or answer == "o":
    q1 = input("s'agit il d'un nouveau model\nO/N ?: ")
    if q1 == 'O' or q1 == 'o':
        name = input('Nom du modele:')
        model_save = f'model/{name}.sav'
        pickle.dump(model, open(model_save, 'wb'))
        print('model enregistré')
    else:
        model_save = f'model/LinearSVC.sav'
        pickle.dump(model, open(model_save, 'wb'))
        print('model enregistré')

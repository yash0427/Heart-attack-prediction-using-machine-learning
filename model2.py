import pandas as pd
import pickle
df = pd.read_csv("heart.csv")

heart= df.drop(['oldpeak','slp','thall'],axis=1)

x= heart.iloc[:,:-1]
y=heart.iloc[:,-1:]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=101)

from sklearn.preprocessing import LabelEncoder
lbl= LabelEncoder()
encoded_ytrain= lbl.fit_transform(y_train)
encoded_ytest= lbl.fit_transform(y_test)

from sklearn.linear_model import LogisticRegression

logreg= LogisticRegression()
logreg.fit(x_train, encoded_ytrain)

pickle.dump(logreg,open('model2.pkl','wb'))
model = pickle.load(open('model2.pkl','rb'))

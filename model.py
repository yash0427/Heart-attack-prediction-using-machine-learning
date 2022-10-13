import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import pickle
df = pd.read_csv("heart.csv")
heart= df.drop(['oldpeak','slp','thall'],axis=1)

scale=StandardScaler()
scale.fit(heart)
heart= scale.transform(heart)
heart=pd.DataFrame(heart,columns=['age', 'sex', 'cp', 'trtbps', 'chol', 'fbs', 'restecg', 'thalachh','exng', 'caa', 'output'])

x= heart.iloc[:,:-1]
y=heart.iloc[:,-1:]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=101)

lbl= LabelEncoder()
encoded_ytrain= lbl.fit_transform(y_train)
encoded_ytest= lbl.fit_transform(y_test)

logreg= LogisticRegression()
logreg.fit(x_train, encoded_ytrain)


pickle.dump(logreg,open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))


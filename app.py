from copyreg import pickle
from flask import Flask , render_template, request
import numpy as np
import pickle
import pandas as pd
app = Flask(__name__)
model2 = pickle.load(open('model2.pkl','rb'))
@app.route('/')
def hello_world():
      return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
      # features = [int(x) for x in request.form.values()]
      # final = [np.array(features)]
      # prediction = model2.predict(final)
      # output = round(prediction[0],2)
      # # if(output==0):
      # #       output = "No"
      # # if(output==1):
      # #       output="yes"
      
      # return render_template('index.html',predicton_value='Person is having attack chances are {}'.format(output))
      input_features = [int(x) for x in request.form.values()]
      features_value = [np.array(input_features)]
      
      
      features_name = [ "age", "sex","cp","trtbps", "chol", "fbs",
                       "restecg", "thalachh", "exng", "caa"]
          
      df = pd.DataFrame(features_value, columns=features_name)
      output = model2.predict(df)
        
      if(output==0):
               output="Patient Does Not Have Risk of Heart Attack"
      else:
               output="Patient Has Risk of Heart Attack"
        
               
      return render_template('index.html', prediction_text='{}'.format(output))

if __name__ == "__main__":
      app.run(debug=True,port =8000)
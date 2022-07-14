from flask import Flask,request, jsonify
import joblib
import pandas as pd 

app = Flask(__name__)

@app.route('/predict',methods=['POST'])
def predict():

    feat_data = request.json

    df = pd.DataFrame(feat_data)
    df = df.reindex(columns=col_names)
    
    prediction = list(model.predict(df))

    return jsonify({'prediction':str(prediction)})

if __name__ == '__main__':
    model = joblib.load('final_model.pkl')
    col_names = joblib.load('column_names.pkl')

    app.run(debug=True)


from flask import Flask, render_template, request
from functions import prediction_model
import mlflow
from tensorflow.keras.models import load_model
app = Flask(__name__)
# C:\Users\anany\Desktop\Internship\Website classification\MLFLOW MODEL\mlruns\models\Website_Authenticity_Detection\version-1
# model_uri = "file:///C:/Users/anany/Desktop/Internship/Website classification/MLFLOW MODEL/mlruns/models/Website_Authenticity_Detection/version-1"  # Replace <model_name> and <version> with your model's name and version
# model = mlflow.pyfunc.load_model(model_uri)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])


def predict():
    url = request.form['user_data']
    model = load_model('model_3.h5')
    pred = prediction_model(url,model)
    return pred
# prediction = {"result": "This is a prediction"}
if __name__ == "__main__":
    app.run(debug=True)

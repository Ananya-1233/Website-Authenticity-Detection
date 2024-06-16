from django.shortcuts import render
import tensorflow as tf
from tensorflow.keras.models import load_model
from functions import prediction_model
import numpy as np
# def index(request):
#     if request.method == 'POST':
#         text_input = request.POST.get('text_input')
#         # Handle the text input (e.g., process it or save it)
#         return HttpResponse(f"Received input: {text_input}")
#     return render(request, 'index.html')
model = load_model('model_3.h5')
def predict(request):
  if request.method == 'POST':
    text = request.POST['text_input']
        # if isinstance(text, str):
        #   text = text.lower()
        # else:
        #   text = "" 
          # Load your model
        #preprocessed_data = preprocess_data(text)  # Preprocess the input data
      #  text_input = np.array([[float(text)]])
        # input_data = np.array([text])
    predictions = prediction_model(text, model) 
    pred = np.argmax(predictions, axis=1)
    prediction_text = {'predictions': pred}
    if pred == 0:
      result = 'Authentic'
    else:
      result = 'Malicious'
    return render(request, 'index.html', {'prediction_text': result})
  else:
    return render(request, 'index.html')
 
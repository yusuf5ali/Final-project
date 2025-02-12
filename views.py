from django.shortcuts import render
from .forms import PredictionForm
from .models import CarInput
import pickle
import numpy as np

# ট্রেন করা মডেল লোড করুন
with open('mtcars_model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_mpg(request):
    prediction = None
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            hp = form.cleaned_data['hp']
            wt = form.cleaned_data['wt']
            cyl = form.cleaned_data['cyl']
            # পূর্বাভাসের জন্য ইনপুট প্রস্তুত করুন
            input_data = np.array([[hp, wt, cyl]])
            prediction = model.predict(input_data)[0]

            # ইনপুট ডেটা এবং পূর্বাভাস সংরক্ষণ করুন
            car_input = CarInput(hp=hp, wt=wt, cyl=cyl, predicted_mpg=prediction)
            car_input.save()
    else:
        form = PredictionForm()

    return render(request, 'mtcars/predict.html', {'form': form, 'prediction': prediction})
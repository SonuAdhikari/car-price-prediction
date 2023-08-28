from flask import Flask, request, render_template
import pickle

app = Flask(__name__)  # initialising flask app

model = pickle.load(open('car-price.pkl', 'rb')) # load ml model

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        year_of_purchase = float(request.form['year'])
        #km_driven = int(request.form['distance'])
        car_mileage = request.form['mileage']
        engine = request.form['engine']
        max_power = request.form['max_power']
        prediction = model.predict([[year_of_purchase, car_mileage, engine, max_power]])[0]
        #prediction = model.predict([[year_of_purchase, km_driven, car_mileage, engine, max_power]])

        #output = round(prediction[0], 2)
        return render_template("index.html", prediction=prediction)

        #*return render_template('index.html', output="{} Lakh".format(output))
if __name__ == '__main__':
    app.run(debug=True)
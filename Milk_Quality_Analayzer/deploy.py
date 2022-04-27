from flask import Flask,render_template,request
import pickle
 
app = Flask(__name__,template_folder='template')

#load the model

model = pickle.load(open('milkquality.pkl','rb'))

@app.route('/')
def home():
    return render_template('main_form.html',**locals())

@app.route('/predict', methods=['POST','GET'])
def predict():
    PH = float(request.form['PH'])
    Temp = float(request.form['Temp'])
    Taste = float(request.form['Taste'])
    Odor= float(request.form['Odor'])
    Fat = float(request.form['Fat'])
    Turbidity = float(request.form['Turbidity'])
    Color = float(request.form['Color'])

    result = model.predict([[PH,Temp,Taste,Odor,Fat,Turbidity,Color]])[0]
    return render_template('main_form.html',**locals())

if __name__ == '__main__':
    app.run(debug=True)    

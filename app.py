from flask import Flask,request,render_template
import pickle


file = open('hyd_house_rf.pkl','rb')
rf = pickle.load(file)
file.close()



app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/parameters')
def parameters():
    return render_template('parameters.html')

    
@app.route('/predict',methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        my_dict = request.form
        meanrad = float(my_dict['meanrad'])
        concavemean= float(my_dict['concavemean'])
        concavepoints = float(my_dict['concavepoints'])
        radworst= float(my_dict['radworst'])
        perworst= float(my_dict['perworst'])
        input_features = [meanrad,concavemean,concavepoints,radworst,perworst]
        inf = rf.predict([input_features])
        inf*=0.5
        return render_template('show.html',inf = inf)
    return render_template('predict.html')

if __name__ == "__main__":
    app.run(debug = True)
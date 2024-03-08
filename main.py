#flask,scikit-learn,pandas,pickle-mixin all this libraires needed install by pip install
#{{this jinja code which is used in python flask }}
import pandas as pd   #we want to import clean data before that we import pandas

from flask import Flask, render_template,request
import pickle
import numpy as np

app = Flask(__name__)
data = pd.read_csv('Cleaned_data.csv')
# open pickle file in rb mode
pipe = pickle.load(open("RidgeModel.pkl",'rb'))
# just like above create 4 more
data2 = pd.read_csv('Cleaned_data2.csv')
pipe2 = pickle.load(open("RidgeModel2.pkl",'rb'))

data3 = pd.read_csv('Cleaned_data3.csv')
pipe3 = pickle.load(open("RidgeModel3.pkl",'rb'))

data4 = pd.read_csv('Cleaned_data4.csv')
pipe4 = pickle.load(open("RidgeModel4.pkl",'rb'))

data5 = pd.read_csv('Cleaned_data5.csv')
pipe5 = pickle.load(open("RidgeModel5.pkl",'rb'))
#first page
@app.route('/') #/ this froward slash site run the site first
def index():
    locations = sorted(data['location'].unique())   # in locations we store data location and get unique and sorted
    return render_template('index.html',locations=locations) #passing my location to index file so that we can fill the options
#in below code we are passing locations
#linking
#while linking pages don't do spelling mistakes becoz it can stop your render and show error
# @app.route('/about') 
# def about():
#     return render_template('about.html')

@app.route('/gallery') 
def gallery():
     return render_template('gallery.html')

@app.route('/blog') 
def blog():
     return render_template('blog.html')

@app.route('/about') 
def about():
     return render_template('about.html')

@app.route('/contact') 
def contact():  
     return render_template('contact.html')

@app.route('/predictor_page') 
def predictor_page():  
     return render_template('predictor_page.html')

#now linking predictor page with states predictor
#...............................................#
#...............................................#
@app.route('/B_predictor') 
def B_predictor():  
    locations = sorted(data['location'].unique())   # in locations we store data location and get unique and sorted
    return render_template('B_predictor.html',locations=locations) #passing my location to index file so that we can fill the options
     

@app.route('/D_predictor') 
def D_predictor():  
    locations = sorted(data2['location'].unique())   # in locations we store data location and get unique and sorted
    return render_template('D_predictor.html',locations=locations)

@app.route('/G_predictor') 
def G_predictor():  
     locations = sorted(data4['location'].unique())   # in locations we store data location and get unique and sorted
     return render_template('G_predictor.html',locations=locations)

@app.route('/M_predictor') 
def M_predictor():  
    locations = sorted(data3['location'].unique())   # in locations we store data location and get unique and sorted
    return render_template('M_predictor.html',locations=locations)

@app.route('/T_predictor') 
def T_predictor():  
    locations = sorted(data5['location'].unique())   # in locations we store data location and get unique and sorted
    return render_template('T_predictor.html',locations=locations)



@app.route('/predict',methods=['POST'])
def predict():
    #here we get 4 things
    #to acces location we have to write
    #id to location given is location
    #when user selecting the location then we get the data in this location
    #whichever user is selected we get

    location = request.form.get('location') 
    bhk = float(request.form.get('bhk')) 
    bath = float(request.form.get('bath')) 
    sqft = request.form.get('total_sqft') 
    # print(location,bhk ,bath ,sqft) we can see all data is print correctly now we are ready to predict
    input = pd.DataFrame([[location,sqft,bath,bhk]],columns=['location','total_sqft','bath','bhk'])#here fill the data which is send by the user
    #input data is ready now i am going to predict
    prediction = pipe.predict(input)[0] * 1e5#it gives list on 0 position where there is one value
    #prediction give integer number and we write str prediction
    print(prediction)

    return str(np.round(prediction,1))

# now make 4 more predict functions for other states

#prediction function for delhi 
@app.route('/predict_D',methods=['POST'])
def predict_D():
    location = request.form.get('location') 
    bhk = float(request.form.get('bhk')) 
    bath = float(request.form.get('bath')) 
    sqft = request.form.get('total_sqft') 
    # print(location,bhk ,bath ,sqft) we can see all data is print correctly now we are ready to predict
    input = pd.DataFrame([[location,sqft,bath,bhk]],columns=['location','total_sqft','bath','bhk'])#here fill the data which is send by the user
    #input data is ready now i am going to predict
    prediction = pipe2.predict(input)[0] * 1e5#it gives list on 0 position where there is one value
    #prediction give integer number and we write str prediction
    print(prediction)

    return str(np.round(prediction,1))#reduce  1 points after decimal value Beacuse houses are costly ..

#prediction function for Mumbai
@app.route('/predict_M',methods=['POST'])
def predict_M():
    location = request.form.get('location') 
    bhk = float(request.form.get('bhk')) 
    bath = float(request.form.get('bath')) 
    sqft = request.form.get('total_sqft') 
    # print(location,bhk ,bath ,sqft) we can see all data is print correctly now we are ready to predict
    input = pd.DataFrame([[location,sqft,bath,bhk]],columns=['location','total_sqft','bath','bhk'])#here fill the data which is send by the user
    #input data is ready now i am going to predict
    prediction = pipe3.predict(input)[0] * 1e5#it gives list on 0 position where there is one value
    #prediction give integer number and we write str prediction
    print(prediction)

    return str(np.round(prediction,1))#reduce  1 points after decimal value Beacuse houses are costly ..

#prediction function for Gujarat
@app.route('/predict_G',methods=['POST'])
def predict_G():
    location = request.form.get('location') 
    bhk = float(request.form.get('bhk')) 
    bath = float(request.form.get('bath')) 
    sqft = request.form.get('total_sqft') 
    # print(location,bhk ,bath ,sqft) we can see all data is print correctly now we are ready to predict
    input = pd.DataFrame([[location,sqft,bath,bhk]],columns=['location','total_sqft','bath','bhk'])#here fill the data which is send by the user
    #input data is ready now i am going to predict
    prediction = pipe4.predict(input)[0] * 1e5#it gives list on 0 position where there is one value
    #prediction give integer number and we write str prediction
    print(prediction)

    return str(np.round(prediction,1))


#prediction function for Tamil nadu
@app.route('/predict_T',methods=['POST'])
def predict_T():
    location = request.form.get('location') 
    bhk = float(request.form.get('bhk')) 
    bath = float(request.form.get('bath')) 
    sqft = request.form.get('total_sqft') 
    # print(location,bhk ,bath ,sqft) we can see all data is print correctly now we are ready to predict
    input = pd.DataFrame([[location,sqft,bath,bhk]],columns=['location','total_sqft','bath','bhk'])#here fill the data which is send by the user
    #input data is ready now i am going to predict
    prediction = pipe5.predict(input)[0] * 1e5#it gives list on 0 position where there is one value
    #prediction give integer number and we write str prediction
    print(prediction)

    return str(np.round(prediction,1))

if __name__== "__main__":
    app.run(debug=True,port=5001)


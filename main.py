import pickle
import streamlit as st
import pandas as pd
from datetime import date
import sklearn
from sklearn.ensemble import RandomForestRegressor
st.header('Get the right price of your Bike')
bike = pd.read_csv('data.csv')
model = pickle.load(open('bike_prediction_best.pkl','rb'))
bike_model = sorted(bike['bike_name'].unique())
brand = sorted(bike['brand'].unique())
years = sorted(bike['age'].unique())
engine = sorted(bike['power'].unique())
#kms_run = bike['kms_driven'].unique()
#print(bike_model)
todays_year = date.today().year
def predict_price(selected_bike_model,selected_bike_brand,selected_year,selected_engine,selected_kms_run):
    bike_age = todays_year - int(selected_year)
    price = model.predict(pd.DataFrame([[selected_bike_model,selected_kms_run,bike_age,selected_engine,selected_bike_brand]],
                                       columns = ['bike_name','kms_driven','age','power','brand']))
    #print(price)
    
    return round(price[0])




selected_bike_model = st.selectbox(
    "Type or select a bike model from the dropdown",
    bike_model
)
selected_bike_brand = st.selectbox(
    "Type or select a bike brand from the dropdown",
    brand
)
selected_year = st.text_input(
    "Enter year of purchase"
)
selected_engine = st.selectbox(
    "Type or select engine typeof your bike",engine
)
selected_kms_run = st.text_input(
    "Enter the number of K.M travelled without comma separation",
)

if st.button('Show price'):
    price = predict_price(selected_bike_model,selected_bike_brand,selected_year,selected_engine,selected_kms_run)
    st.write("The estimated price of your bike is: Rs",price)


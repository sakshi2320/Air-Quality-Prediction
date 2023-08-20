import streamlit as st
import pickle

model = pickle.load(open('model.pkl','rb'))

st.title('Air Quality Prediction')

pm2 = st.text_input('Enter the value for PM2.5')
pm10 = st.text_input('Enter the value for PM10')
no = st.text_input('Enter the value for NO')
no2 = st.text_input('Enter the value for NO2')
nox = st.text_input('Enter the value for NOx')
co = st.text_input('Enter the value for CO')
nh3 = st.text_input('Enter the value for NH3')
o3 = st.text_input('Enter the value for O3')
so2 = st.text_input('Enter the value for SO2')
benzene = st.text_input('Enter the value for Benzene')
toluene = st.text_input('Enter the value for Toluene')
xylene = st.text_input('Enter the value for Xylene')

if st.button('Predict'):
    val = model.predict([[pm2, pm10, no, no2, nox, co, nh3, o3, so2, benzene, toluene, xylene]])

    if val <= 50:
        st.header(f'The AQI Value of {val[0]} is Good')
    elif val < 100:
        st.header(f'The AQI Value of {val[0]} is Unhealthy')
    elif val < 150:
        st.header(f'The AQI Value of {val[0]} is Satisfactory')
    elif val < 200:
        st.header(f'The AQI Value of {val[0]} is Severe')
    elif val < 300:
        st.header(f'The AQI Value of {val[0]} is Hazardous')
    else:
        st.header(f'The AQI Value of {val[0]} is Dangerous')
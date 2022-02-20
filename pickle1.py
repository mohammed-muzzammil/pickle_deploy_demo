import streamlit as st
import pickle

# "/app/{repository name}/ {file.extension}"
Pkl_Filename = "/Users/macbook/Downloads/Model.pkl"

#with open('model_pkl', 'wb') as files:
 #   pickle.dump(model, files)

with open(Pkl_Filename, 'rb') as file:
    Regressor_model = pickle.load(file)

st.title('Salary Prediction Model')

yoe = st.sidebar.slider('Years of Expirience', 18, 60)

if st.sidebar.button('Predict'):
    output = Regressor_model.predict([[yoe]])
    st.write('The Predicted Salary is {}'.format(output))
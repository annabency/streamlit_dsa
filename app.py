import streamlit as st
import pickle
st.header("Predict weight from height")  #header


st.write("Demo of linear regression")

#with st.form("myform"):
height =st.number_input(label="Enter the height in inches", min_value=35.0,max_value=180.0,value=50.0,step=1.0 )
submitted= st.button('submit')

if submitted:
    pickled_model=pickle.load(open("model.pkl",'rb'))
    weight=pickled_model.predict([[height]])
    print(weight[0])
    st.write(f"Expected weight value is {weight[0]} pounds.")
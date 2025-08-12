import pickle
import string
import streamlit as st
import webbrowser

global Lrdetect_Model
LrdetectFile = open('model.pkl','rb')
Lrdetect_Model = pickle.load(LrdetectFile)
LrdetectFile.close()
st.title("Language Detection Tool")
input_test = st.text_input("provide your text input here" , 'my name is nadeem')

button_clicked = st.button("Get Language")
if button_clicked:
    st.text(Lrdetect_Model.predict([input_test]))
   


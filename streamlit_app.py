import streamlit as st
import numpy as np
import pandas as pd
st.header("st.slider")
age=st.slider(
    "Enter you age",0,100
)
st.write("Your age is ",age)

line_chart=pd.DataFrame(np.random.rand(20,3),columns=['a','b','c'])
st.line_chart(line_chart)

st.write("st.selectbox")
option=st.selectbox("What is your favourite color",('red','blue','green'))
st.write("Your favourite color is",option)
         
st.write("st.multiselect")
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'])

st.write('You selected:')
for option in options:
  st.write(option)


  st.write(" Creating check box ")

  tea=st.checkbox("Tea")
  coffee=st.checkbox("Coffee")
  icecream=st.checkbox("iceCream")

  if tea:
    st.write("Here is your tea")
  if coffee:
   st.write("Here is your coffee")
  if icecream:
    st.write("Here is your icecream")    
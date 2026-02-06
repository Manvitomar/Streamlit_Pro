import streamlit as st

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#FFFFFF"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.slider('Select a number:', 0, 90)
st.sidebar.write('Selected number from slider widget is:', number)
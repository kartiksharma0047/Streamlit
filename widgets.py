import streamlit as st

st.title("Widgets")

if st.button("Click Here"):
    st.write("Button Clicked")
    
name=st.text_input("Name")
st.write(name)

address=st.text_area("Enter address")
st.write(address)


if st.checkbox("You accept the T&C",value=False):
    st.write("Thank you!")
    
st.radio("Colors",["Red","Grenn","Blue"],index=1)

st.selectbox("Colors",["Red","Green","Blue"],index=1)

st.multiselect("Colors",["Red","Green","Blue"])

st.slider("age",min_value=10,max_value=80,step=2,value=36)
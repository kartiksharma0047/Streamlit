import streamlit as st

st.title("Registration Form")

first, last = st.columns(2)
first.text_input("First Name")
last.text_input("Last Name")

email,mob=st.columns([2,1])
email.text_input("Email")
mob.number_input("Mobile Number",min_value=0,max_value=9999999999)

user,pw,pw2=st.columns(3)
user.text_input("Username")
pw.text_input("Password",type="password")
pw2.text_input("Retype Password",type="password")

checkBox,bl,submit=st.columns(3)
checkBox.checkbox("Agree",value=False)
submit.button("Submit")

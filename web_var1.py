import streamlit as st
import json

st.title('Website for KMA')

st.subheader('Please enter user id')

userID = st.text_input('Please enter an eight-digit id', '')
userID = "N"+userID
if st.button('Check'):
    with open("sample.json") as file:
        data = json.load(file)
    for i in data:
        if data[i]["ID number"] != userID:
            st.write("There is no such user with this ID")
            st.write("Please enter the correct ID")
            break
        elif data[i]["ID number"] == userID:
            name = data[i]['Name of participants']
            dfb = data[i]['Date of birth']
            idn = data[i]["ID number"]
            iss_date = data[i]["Issue date"]
            date_of_cour = data[i]["Date of courses"]
            sert_num = data[i]["Number of certificate"]
            #st.write(json.dumps(data[i], indent=4, ensure_ascii=False))
            st.write("Name of participants: " , name)
            st.write("Issue date: ", iss_date)
            st.write("Data of course: ", date_of_cour)
            st.write("Number of certificate: ", sert_num)







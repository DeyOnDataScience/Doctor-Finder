from workflow import extract_location_speciality,summary
import streamlit as st

st.title("Doctor Finder")
side = st.sidebar.selectbox("Select",["About","Doctor Finder"])
if side == "About":
    st.write(f"""
                The Health Assistant Project is a Python-based application designed to assist users with health-related queries.
                It uses natural language processing (NLP) to identify key symptoms, possible causes, and suitable medical specialties. The project also includes a web scraping feature to find nearby doctors based on the user's location and preferred specialty.
""")
elif side == "Doctor Finder":
    user_query = st.text_input("Enter Your Health Problem")
    if st.button("Find Doctor"):
        loc_spec = extract_location_speciality(user_query)
        result = summary(user_query,loc_spec)
        st.write(result)
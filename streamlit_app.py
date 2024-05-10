import streamlit as st
from main import ResearchCrew  # Import the ResearchCrew class from main.py
import os

st.title('WHATS THE STORY MORNING GLORY')
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["SERPER_API_KEY"] = st.secrets["SERPER_API_KEY"]

with st.sidebar:
    st.header('Enter Newsletter Details Here')
    subject = st.text_input("What does the customer sell?")
    customer = st.text_area("Who is the customer or persona?")
    additional_info = st.text_area("What are they interested in buying from you?")

if st.button('Run Research'):
    if not customer or not subject or not additional_info:
        st.error("Please fill all the fields.")
    else:
        inputs = f"Subject: {subject}\nCustomer: {customer}\nAdditional Information: {additional_info}"
        research_crew = ResearchCrew(inputs)
        result = research_crew.run()
        st.subheader("Results of your research project:")
        st.write(result)
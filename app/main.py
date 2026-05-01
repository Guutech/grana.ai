import streamlit as st
from core.controller import handle
from data.data_service import DataService

st.title("Grana AI 💰")

data_service = DataService()

uploaded_file = st.file_uploader("Envie seu CSV", type=["csv"])

if uploaded_file:
    df = data_service.get_data(uploaded_file)

    user_input = st.chat_input("Pergunte sobre suas finanças")

    if user_input:
        response = handle(user_input, df)

        st.write(response["text"])

        if "chart" in response:
            st.plotly_chart(response["chart"])

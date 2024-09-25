import streamlit as st

x = st.number_input("Masukkan suhu")
sx = st.text_input("Satuan c")
st.write("Amda menginput suhu ", x," dengan satuan ", sx )
st.write("Kuadratnya ", x*x)

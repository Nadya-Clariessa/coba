import streamlit as st

x = st.number_input("Masukkan suhu")
sx = st.text_input("Satuan c")
st.write("Anda menginput suhu ", x," dengan satuan ", sx )
st.write("Kuadratnya ", x*x)
if (sx == "c"):
  pass
else:
  pass

st.write("Hasil konversi ", x," dengan satuan ",x,sx," adalah ...", sy )

import streamlit as st

x = st.number_input("Masukkan suhu")
sx = st.text_input("Satuan", "c")
st.write("Anda menginput suhu ", x," dengan satuan ", sx )
sy = st.text_input("Konversi ke", "c")
if (sx == "c"):
  pass
else:
  pass

st.write("Hasil konversi dari ",x,sx," adalah ...", sy )

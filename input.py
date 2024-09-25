import streamlit as st

# Input suhu
x = st.number_input("Masukkan suhu")
sx = st.text_input("Satuan", "c").lower()
st.write("Anda menginput suhu ", x, " dengan satuan ", sx)

# Input satuan konversi
sy = st.text_input("Konversi ke", "c").lower()

# Fungsi untuk konversi suhu
def konversi_suhu(suhu, dari_satuan, ke_satuan):
    if dari_satuan == "c":
        if ke_satuan == "f":
            return suhu * 9/5 + 32
        elif ke_satuan == "k":
            return suhu + 273.15
        elif ke_satuan == "c":
            return suhu
    elif dari_satuan == "f":
        if ke_satuan == "c":
            return (suhu - 32) * 5/9
        elif ke_satuan == "k":
            return (suhu - 32) * 5/9 + 273.15
        elif ke_satuan == "f":
            return suhu
    elif dari_satuan == "k":
        if ke_satuan == "c":
            return suhu - 273.15
        elif ke_satuan == "f":
            return (suhu - 273.15) * 9/5 + 32
        elif ke_satuan == "k":
            return suhu

# Proses konversi
if sx in ["c", "f", "k"] and sy in ["c", "f", "k"]:
    hasil = konversi_suhu(x, sx, sy)
    st.write("Hasil konversi dari ", x, sx, " adalah ", hasil, sy)
else:
    st.write("Satuan tidak valid. Silakan masukkan satuan yang benar (c, f, k).")

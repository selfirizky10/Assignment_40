import streamlit as st

st.set_page_config(page_title="Portofolio",
                   layout='wide', page_icon=":rocket:")

st.title("Portofolio Selfi")
st.header("Assigment 40")

st.sidebar.title("Menu")
page = st.sidebar.radio("Pilih Halaman",
                        ["Tentang Saya", "Proyek", "Machine Learning", "Kontak"])

if page == "Tentang Saya":
    import tentang_saya
    tentang_saya.tampilkan_tentang_saya()
elif page == "Proyek":
    import proyek
    proyek.tampilkan()
elif page == "Machine Learning":
    import machine_learning
    machine_learning.tampilkan()
elif page == "Kontak":
    import kontak
    kontak.tampilkan_kontak()

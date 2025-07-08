import streamlit as st

def tampilkan_kontak():
    st.subheader("Hubungi Saya")

    st.write("📧 Email: selfihandayani20@email.com")
    st.write("💼 LinkedIn: [linkedin.com/in/selfirizky](https://www.linkedin.com/in/selfirizky/)")
    st.write("📱 WhatsApp: +62 838-0856-0303")

    st.write("Atau isi form di bawah:")
    nama = st.text_input("Nama")
    pesan = st.text_area("Pesan")

    if st.button("Kirim"):
        st.success("Pesan terkirim! Terima kasih telah menghubungi saya.")

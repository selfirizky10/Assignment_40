import streamlit as st

def tampilkan_tentang_saya():
    st.subheader("👩‍💻 Tentang Saya")

    # Dua kolom: gambar di kiri, teks di kanan
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("https://i.pinimg.com/736x/25/06/c9/2506c909c706c6fcbaaf686aafc5032e.jpg", width=200, caption="Selfi Rizky Handayani")

    with col2:
        st.markdown("""
        Halo! Saya **Selfi Rizky Handayani**, seorang siswa di program DBIMBING Batch 32A yang sedang belajar menjadi seorang **Data Analyst**.

        Saya memiliki minat di bidang:
        - 📊 Analisis dan visualisasi data
        - 🤖 Machine Learning
        - 🌐 Aplikasi Web dengan Streamlit

        Saat ini saya sedang membangun portofolio proyek untuk mendukung perjalanan karier saya di bidang data.
        """)

    st.markdown("---")
    st.markdown("📫 **Kontak**: selfihandayani20@email.com  |  🌐 [LinkedIn](https://linkedin.com/in/selfirizky)  |  💻 [GitHub](https://github.com/selfirizky10)")

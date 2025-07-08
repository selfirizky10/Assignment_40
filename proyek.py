import streamlit as st
import pandas as pd
import numpy as np

def tampilkan():
    st.subheader("📈 Visualisasi Data Dinamis")
    
    # Buat data dummy
    data = pd.DataFrame(
        np.random.randn(50, 3),
        columns=['A', 'B', 'C']
    )

    # Pilih jenis grafik
    chart_type = st.selectbox(
        "Pilih jenis grafik yang ingin ditampilkan:",
        ["Line Chart", "Bar Chart", "Area Chart"]
    )

    # Filter data dengan slider
    st.markdown("### 🎚️ Filter Data")
    range_slider = st.slider("Pilih rentang baris", 0, len(data) - 1, (10, 30))
    filtered_data = data.iloc[range_slider[0]:range_slider[1]]

    # Tampilkan grafik sesuai pilihan
    st.markdown("### 📊 Hasil Visualisasi")
    if chart_type == "Line Chart":
        st.line_chart(filtered_data)
    elif chart_type == "Bar Chart":
        st.bar_chart(filtered_data)
    elif chart_type == "Area Chart":
        st.area_chart(filtered_data)

    # Tampilkan tabel
    st.markdown("### 📄 Data Ditampilkan")
    st.dataframe(filtered_data)

import streamlit as st
import numpy as np

def tampilkan():
    st.subheader("Machine Learning")
    st.write("Model regresi sederhana untuk prediksi harga rumah menggunakan perhitungan manual")

    luas = st.number_input("Luas Tanah (m2)", 20, 1000, 100)
    kamar = st.slider("Jumlah Kamar", 1, 10, 3)

    if st.button("Prediksi"):
        # Data training
        X = np.array([[100, 3],
                      [150, 4],
                      [200, 5],
                      [120, 3]])
        y = np.array([500, 700, 1000, 600])  # dalam juta

       
        X_b = np.c_[np.ones((X.shape[0], 1)), X]  
        y = y.reshape(-1, 1)


        w = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y

        # Data input
        X_input = np.array([[1, luas, kamar]]) 
        y_pred = X_input @ w

        st.success(f"Prediksi Harga Rumah: Rp {y_pred[0,0]:.2f} juta")

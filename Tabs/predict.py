import streamlit as st

from web_function import predict

def app(x, y):
    st.title("Halaman Prediksi")

    col1, col2 = st.columns(2)

    with col1:
        age = st.text_input('Masukan umur pasien')
    with col1:
        sex = st.text_input('Masukan jenis kelamin(1/0)')
    with col1:
        cp = st.text_input('Jenis nyeri dada (1=angina tipikal, 2=angina atipikal, 3=non angina, 4=tanpa gejala)')
    with col1:
        trtbps = st.text_input('Masukan tekanan darah dalam istirahat (mm Hg)')
    with col1:
        chol = st.text_input('Masukan koresterol (mg/dl)')
    with col1:
        fbs = st.text_input('Gula darah puasa > 120 mg/dl (1=benar, 0=salah)')
    with col2:
        restecg = st.text_input('Hasil elektrokardiografi istirahat (0=normal, 1=ada kelainan gelombang ST-T, 2=kemungkinan/pasti hypertrophy)')
    with col2:
        thalachh = st.text_input('Masukan detak jantung maksimum yang dicapai')
    with col2:
        exng = st.text_input('Angina akibat olahraga (1 = ya, 0 = tidak)')
    with col2:
        oldpeak = st.text_input('Masukan oldpeak value')
    with col2:
        slp = st.text_input('Masukan slope value (0-2)')
    with col2:
        caa = st.text_input('Masukan major vessels (0-3)')
    with col2:
        thall = st.text_input('Masukan Thal rate (0-3)')
    
    features = [age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall]

    #tombol prediksi
    if st.button("Prediksi"):
        prediction, score = predict(x, y, features)
        score = score
        st.info("Prediksi Sukses...")

        if(prediction == 1):
            st.warning("Orang tersebut rentan terkena penyakkit jantung")
        else:
            st.success("Orang tersebut relatif aman dari penyakit jantung")
        
        st.write("Model yang digunakan memiliki tingkat akurasi ", (score*100),"%")
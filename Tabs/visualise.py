import warnings
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
from sklearn import tree
from sklearn.model_selection import train_test_split
import streamlit as st


from web_function import train_model

def app(x, y):
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.title("Visualisasi Prediksi Penyakit Jantung")

    if st.checkbox("Plot Confusion Matrix"):
        X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=0)
        model, score = train_model(X_train, y_train)
        y_pred = model.predict(X_test)
        cm = confusion_matrix(y_test, y_pred)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
        plt.figure(figsize=(10,6))
        disp.plot()
        st.pyplot()
# , 
    if st.checkbox("Plot Decision Tree"):
        model, score = train_model(x, y)
        dot_data = tree.export_graphviz(
            decision_tree=model, max_depth=3, out_file=None, filled=True, rounded=True,
            feature_names=x.columns, class_names=['nockd','ckd']

        )

        st.graphviz_chart(dot_data)
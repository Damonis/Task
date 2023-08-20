import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import streamlit as st
import plotly.express as px
import scipy.stats as stats 

def run():
    st.title("Статистика и визуализация")
    st.header("Выберите файл")
    uploaded_file = st.file_uploader("upload file", type={"csv", "txt"})
    if uploaded_file is not None:
        data_frame = pd.read_csv(uploaded_file)
    else:
        st.text("Ошибка-файл отсутствует или не поддерживается")
    st.write(data_frame)
    dropdown(data_frame)

def dropdown(data_frame):
    sd1 = st.selectbox(
        "Выберите первую переменную", #Drop Down Menu Name
        [
            "Survived", #First option in menu
            "Pclass",   #Seconf option in menu
            "Name", #Third option
            "Sex", #Fourth option
            "Age", #Fifth option
            "Siblings/Spouses Aboard", # Sixth option
            "Parents/Children Aboard", # Seventh option
            "Fare"
        ]
    )
    sd2 = st.selectbox(
        "Выберите вторую переменную", #Drop Down Menu Name
        [
            "Survived", #First option in menu
            "Pclass",   #Seconf option in menu
            "Name", #Third option
            "Sex", #Fourth option
            "Age", #Fifth option
            "Siblings/Spouses Aboard", # Sixth option
            "Parents/Children Aboard", # Seventh option
            "Fare"
        ]
    )

    check=st.checkbox("Категориальная")
    

    fig = plt.figure(figsize=(20, 12))

    if ( check == True ):
        fig = px.pie(data_frame, values=sd1, names=sd2,color_discrete_sequence=px.colors.sequential.RdBu)
        fig.show()
    else:
        sns.violinplot(x = sd1, y = sd2, data = data_frame)
        

    st.pyplot(fig)
    st.header("Проверка гипотез")

    hyp= st.selectbox(
        "Выберите гипотезу", #Drop Down Menu Name
        [
            "Two Sample t-test",
            "Paired Samples t-test",
        ]
    )

    alpha=st.slider("Минимальное значение альфа",min_value=0.1,max_value=1.0)  
    hyp1 = data_frame[sd1].to_numpy()
    hyp2 = data_frame[sd2].to_numpy()

    if(hyp == "Two Sample t-test"):
        st.text("P value")
        st.text(stats.ttest_ind(a=hyp1, b=hyp2) ) 
        t,p=stats.ttest_ind(a=hyp1, b=hyp2) 
        if(alpha > p):
            st.text("По предположениям гипотеза неверна")
        elif(alpha <= p):   
            st.text("По предположениям гипотеза верна")
        else:
            st.text("Ошибка подсчета")

    elif(hyp == "Paired Samples t-test"):
        st.text("P value")
        st.text(stats.ttest_rel(a=hyp1, b=hyp2) )
        s,p1=stats.ttest_rel(a=hyp1, b=hyp2)
        if(alpha > p1):
            st.text("По предположениям гипотеза неверна")
        elif(alpha <= p1):   
            st.text("По предположениям гипотеза верна")
        else:
            st.text("Ошибка подсчета")


if __name__=='__main__':
    run()
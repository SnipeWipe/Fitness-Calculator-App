import streamlit as st
import plotly.express as px
import pandas as pd
import plotly
st.markdown(
    "<h1 style='text-align: center; color: #ff0000; text-shadow: 4px 4px 6px #000000;font-size: 40px'><u>Data Analysis over Obesity</u></h1>",
    unsafe_allow_html=True
)
a=pd.read_csv("death-rate-from-obesity.csv")
b=pd.read_csv("deaths-from-obesity-by-age.csv")
c=pd.read_csv("mean-body-mass-index-bmi-in-adult-males.csv")
d=pd.read_csv("mean-body-mass-index-bmi-in-adult-women.csv")
e=pd.read_csv("obesity-in-men-vs-obesity-in-women.csv")

st.divider()
col1,col2=st.columns(2)
with col1:
    st.header("Death rate from Obesity")
    fig1=px.bar(a,x=a['Year'],y=a['Deaths that are from all causes attributed to high body-mass index per 100,000 people, in both sexes aged age-standardized'],color = a['Entity'],color_discrete_sequence=px.colors.qualitative.Antique,width=350)
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    st.header("Death of 70+Years from Obesity")
    fig2=px.pie(b,values=b['Deaths that are from all causes attributed to high body-mass index, in both sexes aged 70+ years'],names=b['Entity'])
    st.plotly_chart(fig2, use_container_width=True)

col31,col32 =st.columns(2)
with col31:
    col41,col42 =st.columns(2)
    with col41:
        st.header("Death of (15-49) Years from Obesity")
        fig3=px.pie(b,values=b['Deaths that are from all causes attributed to high body-mass index, in both sexes aged 15-49 years'],names=b['Entity'])
    st.plotly_chart(fig3, use_container_width=True)
with col32:
    st.header("Mean BMI in SEX (Male vs Female)")
    fig=px.bar(a,x=c['Entity'],y=c['Mean BMI (male)'],color = c['Year'],color_discrete_sequence=px.colors.qualitative.Antique,width=350)
    st.plotly_chart(fig1, use_container_width=True)
    

   
st.header("Obesity in Men Vs Women")
fig4=px.line(e,y=e['Indicator:Prevalence of obesity among adults, BMI &GreaterEqual; 30 (age-standardized estimate) (%) - Sex:Male'],x=e['Entity'])
fig4.add_scatter(y=e['Indicator:Prevalence of obesity among adults, BMI &GreaterEqual; 30 (age-standardized estimate) (%) - Sex:Female'],x=e['Entity'],mode="lines")
st.plotly_chart(fig4, use_container_width=True)

col51,col52,col53= st.columns(3)
with col52:
    st.markdown(
    "<h1 style='text-align: center; color: #ffdf00; text-shadow: 2px 2px 4px #000000;'><b>Defeat Obesity, Embrace Vitality: Your Health, Your Future</b></h1>",
    unsafe_allow_html=True)


    

   
    

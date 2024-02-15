import streamlit as st
import numpy as np
import math as m

st.set_page_config(layout="wide",page_icon="💪")

st.markdown(
    "<h1 style='text-align: center; color: #ff0000; text-shadow: 2px 2px 4px #000000;'><u>Rebuild Yourself</u></h1>",
    unsafe_allow_html=True
)

st.divider()
col1,col2 = st.columns(2)

with col1:
    st.markdown(
    "<h1 style='text-align: center; color: #ffffff; text-shadow: 2px 2px 4px #000000;font-size : 24px'><b>BMI(Body Mass Index) Calculator</b></h1>",
    unsafe_allow_html=True
)
   
    x = st.number_input("Enter Weight in Kilograms")
    h = st.number_input("Enter Height in Meters")
    a = st.number_input("Enter your Age(in yrs)") 
    bmi = 0

    if st.button("Submit"):
        try:
            bmi = x / (h**2)
            st.success(f'Your BMI is {bmi}')
        except ZeroDivisionError:
            st.error('Height Cannot be 0')
   
    if bmi > 0:
        if bmi < 18.5:
            st.text("Underweight")
        elif 18.5 <= bmi < 25:
            st.text("Normal weight")
        elif 25 <= bmi < 30:
            st.text("Overweight")
        elif 30 <= bmi < 35:
            st.text("Obesity Class 1")
        elif 35 <= bmi < 40:
            st.text("Obesity Class 2")
        elif bmi >= 40:
            st.text("Obesity Class 3: Severe Obesity")


with col2:
    st.markdown(
    "<h1 style='text-align: center; color: #ffffff; text-shadow: 2px 2px 4px #000000;font-size : 24px'><b>Calories Calculator</b></h1>",
    unsafe_allow_html=True
)
   

    BMR1 = 0
    BMR2 = 0

    g = st.selectbox("Gender",("Male","Female"))
    l = st.selectbox("Select your activity level", ("Sedentary (little to no exercise)","Lightly active (light exercise/sports 1-3 days a week)",
                                                    "Moderately active (moderate exercise/sports 3-5 days a week)",
                                                    "Very active (hard exercise/sports 6-7 days a week)",
                                                    "Super active (very hard exercise & physical job or 2x training)"))
    if st.button("Calcuate"):

        BMR1 = 66.47 + (13.397*x) + (5.003*(h*100)) - (6.755*a)
        BMR2 = 665.1 + (9.563*x) + (1.85*(h*100)) - (4.676*a)
        
        if g == "Male" :
            if l== "Sedentary (little to no exercise)":
                calories = BMR1*1.2
                st.markdown(f"Your daily maintainance calories is {calories}")
            elif l== "Lightly active (light exercise/sports 1-3 days a week)" :
                calories = BMR1*1.375
                st.markdown(f"Your daily maintainance calories is {calories}")
            elif l== "Moderately active (moderate exercise/sports 3-5 days a week)" :
                calories = BMR1*1.55
                st.markdown(f"Your daily maintainance calories is {calories}")
            elif l== "Very active (hard exercise/sports 6-7 days a week)" :
                calories = BMR1*1.725
                st.markdown(f"Your daily maintainance calories is {calories}")
            else: 
                calories = BMR1*1.9
                st.markdown(f"Your daily maintainance calories is {calories}")
        else:
            if l== "Sedentary (little to no exercise)":
                calories = BMR2*1.2
                st.markdown(f"Your daily maintainance calories is {calories}")
            elif l== "Lightly active (light exercise/sports 1-3 days a week)" :
                calories = BMR2*1.375
                st.markdown(f"Your daily maintainance calories is {calories}")
            elif l== "Moderately active (moderate exercise/sports 3-5 days a week)" :
                calories = BMR2*1.55
                st.markdown(f"Your daily maintainance calories is {calories}")
            elif l== "Very active (hard exercise/sports 6-7 days a week)" :
                calories = BMR1*1.725
                st.markdown(f"Your daily maintainance calories is {calories}")
            else:
                calories = BMR2*1.9
                st.markdown(f"Your daily maintainance calories is {calories}")
        


st.divider()
st.markdown(
    "<h1 style='text-align: center; color: #ff0000; text-shadow: 2px 2px 4px #000000;font-size : 35px'><u>Recommended Workout Porgrams</u></h1>",
    unsafe_allow_html=True
)
col3,col4 = st.columns(2)
with col3:
    st.markdown(
    "<h1 style='text-align: center; color: #ffffff; text-shadow: 2px 2px 4px #000000;font-size : 24px'><b>Fat loss/Weight loss</b></h1>",
    unsafe_allow_html=True
)
    st.markdown("""
    <h3 style='display: flex; align-items: center;'> 
        <img src="https://www.pngplay.com/wp-content/uploads/9/Girl-Weight-Loss-PNG-Photo-Image.png" style='margin-left:220px;width:250px; height:250px;'> 
    </h3>
    """, unsafe_allow_html=True)
    st.markdown("""
    <h3 style='display: flex; align-items: center;'> 
    <p> For beginners looking to lose fat, I recommend starting with a combination of strength training and cardio exercises. Strength training helps build muscle, which in turn can boost metabolism and aid in fat loss. It's also important to incorporate cardiovascular exercises to burn calories and improve overall fitness.A beginner workout program for fat loss could include activities such as bodyweight exercises (squats, lunges, push-ups), dumbbell or resistance band exercises, and cardio activities like walking,
                 jogging, cycling, or swimming. Aim for at least 150 minutes of moderate-intensity cardio per week, along with two to three strength training sessions targeting major muscle groups.Remember to gradually increase the intensity and duration of your workouts as your fitness improves. Additionally, it's crucial to pair your exercise routine with a balanced diet to maximize fat loss results. Always consult with a fitness professional before starting a new workout program.  </p></h3>
    """, unsafe_allow_html=True)
    
   

with col4:
    st.markdown(
    "<h1 style='text-align: center; color: #ffffff; text-shadow: 2px 2px 4px #000000;font-size : 24px'><b>Weight gain/ Muscle gain</b></h1>",
    unsafe_allow_html=True
)
  
    st.markdown("""
    <h3 style='display: flex; align-items: center;'> 
        <img src="https://alphaprogression.com/data/blog/img/articles/sizes/sets-per-workout-maximum-muscle-gain-2400.png" style='margin-left:220px;width:300px; height:250px;'> 
    </h3>
    """, unsafe_allow_html=True)
    st.markdown("""
    <h3 style='display: flex; align-items: center;'> 
    <p> For beginners looking to gain muscle, I recommend starting with a full-body strength training program three times per week. Focus on compound exercises like squats, deadlifts, bench presses, rows, and overhead presses. Aim for 8-12 repetitions per set to stimulate muscle growth and be sure to gradually increase the weight as you get stronger. Additionally, incorporating core exercises and adequate rest days is crucial for recovery and growth. As a beginner, it's essential to learn proper form to prevent injuries, 
                so consider working with a certified personal trainer or using reputable resources to understand correct execution. Lastly, remember that nutrition plays a vital role in muscle gain, so ensure you're consuming enough protein and overall calories to support your training. Consistency and patience are key, so stick to the program and track your progress over time.   </p></h3>
    """, unsafe_allow_html=True)
st.divider()
col7,col8,col9,col10,col11 = st.columns(5)
with col9:
    st.page_link("pages\Data_Analysis.py",label="Some Analysis",icon="📊")    

  
st.divider()
col3,col4,col5 = st.columns(3)
st.markdown(
    """
    <style>
    glow-text {
  transition: text-shadow 0.3s ease;
}
    .glow-text:hover {
      text-shadow: 0 0 30px #ffff00, 0 0 30px #ffff00, 0 0 30px #ffff00, 0 0 40px #ffff00;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
with col4:
    st.markdown(
    "<h1 style='text-align: center; color: #eed202; text-shadow: 2px 2px 4px #000000;font-size : 24px'><b><u>For Personal Training details</u></b></h1>",
    unsafe_allow_html=True
)
    st.markdown(
    """<h3 style='display: flex;text-align: center; '> 
        <img src="https://logos-world.net/wp-content/uploads/2020/11/Gmail-Logo.png" style='margin-left:50px;width:55px; height:35px;'> 
        <p style ='margin-left:50px', class="glow-text">fitnessworld@gmail.com</p>
    </h3>
    """, unsafe_allow_html=True)
    st.markdown(
    """<h4 style='display: flex;text-align: center; '> 
        <img src="https://png.pngtree.com/png-clipart/20230123/original/pngtree-flat-red-location-sign-png-image_8927579.png" style='margin-left:50px;width:55px; height:55px;'> 
        <p style ='margin-left:50px', class="glow-text">Mumbai,Near Gymhub</p>
    </h4>
    """, unsafe_allow_html=True)
    
with col5:
    st.markdown(
    "<h1 style='text-align: center; color: #eed202; text-shadow: 2px 2px 4px #000000;font-size : 24px'><b><u>Social Media</u></b></h1>",
    unsafe_allow_html=True
)
   
    st.markdown("""
    <h3 style='display: flex;text-align: center; '> 
        <img src="https://logopng.com.br/logos/instagram-40.png" style='margin-left:50px;width:35px; height:35px;'> 
        <p style ='margin-left:50px', class="glow-text">@health_coach </p>
    </h3>
    """, unsafe_allow_html=True)
    st.markdown("""
    <h3 style='display: flex; text-align: center;'> 
        <img src="https://pluspng.com/img-png/twitter-png-logo-logo-twitter-in-png-2500.png" style='margin-left:50px;width:40px; height:40px;'> 
        <p style ='margin-left:50px', class="glow-text">@health/lifestyle_coach </p>
    </h3>
    """, unsafe_allow_html=True)
    st.markdown("""
    <h3 style='display: flex; text-align: center;'> 
        <img src="https://www.freepnglogos.com/uploads/youtube-play-red-logo-png-transparent-background-6.png" style='margin-left:50px;width:35px; height:35px;'> 
        <p style ='margin-left:50px', class="glow-text">@Your_Coach</p>
    </h3>
    """, unsafe_allow_html=True)
with col3:
    st.markdown(
    "<h1 style='text-align: center; color: #eed202; text-shadow: 2px 2px 4px #000000;font-size : 24px'><b><u>FAQ</u></b></h1>",
    unsafe_allow_html=True
)
    st.link_button(":blue[What is the most effective weight loss method or program?]","https://www.quora.com/What-is-the-most-effective-weight-loss-method-or-program")
    st.link_button(":blue[What are the best ways to lose weight?]","https://www.quora.com/What-are-the-best-ways-to-lose-weight-8")
    st.link_button(":blue[What workout routine has given you the most muscle gains?]","https://quora.com/What-workout-routine-has-given-you-the-most-muscle-gains")
    st.link_button(":blue[What is the best muscle gaining program for beginners?]","https://www.quora.com/What-is-the-best-muscle-gaining-program-for-beginners")
    st.link_button(":blue[How often should I take a protein supplement for weight/muscle gaining?]","https://www.quora.com/How-often-should-I-take-a-protein-supplement-for-weight-muscle-gaining")
    
    
       
   
    



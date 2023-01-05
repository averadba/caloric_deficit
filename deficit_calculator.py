import streamlit as st

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

st.set_option('deprecation.showPyplotGlobalUse', False)

def calculate_bmr(weight, feet, inches, age, sex):
    height = (feet * 12) + inches
    if sex == "male":
        bmr = 66 + (6.2 * weight) + (12.7 * height) - (6.76 * age)
    else:
        bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
    return bmr

def calculate_tdee(bmr, activity_level):
    if activity_level == "sedentary (little or no exercise)":
        tdee = bmr * 1.2
    elif activity_level == "lightly active (light exercise 1-3 days/week)":
        tdee = bmr * 1.375
    elif activity_level == "moderately active (moderate exercise 3-5 days/week)":
        tdee = bmr * 1.55
    elif activity_level == "very active (hard exercise 6-7 days/week)":
        tdee = bmr * 1.725
    elif activity_level == "extra active (very hard exercise)":
        tdee = bmr * 1.9
    return tdee

def calculate_deficit(tdee):
    deficit = tdee - 500
    return deficit

st.title("Caloric Deficit Calculator")

weight = st.number_input("Weight (lbs):")
feet = st.number_input("Height (feet):")
inches = st.number_input("Height (inches):")
age = st.number_input("Age:")
sex = st.radio("Sex:", ["male", "female"])
activity_level = st.selectbox("Activity level:", ["sedentary (little or no exercise)", "lightly active (light exercise 1-3 days/week)",
                              "moderately active (moderate exercise 3-5 days/week)", "very active (hard exercise 6-7 days/week)", "extra active (very hard exercise)"])

bmr = calculate_bmr(weight, feet, inches, age, sex)
tdee = calculate_tdee(bmr, activity_level)
deficit = calculate_deficit(tdee)

st.write(f"Your BMR is {bmr:.2f} calories per day.")
st.write(f"Your TDEE is {tdee:.2f} calories per day.")
st.write(f"To lose 1-2 pounds per week, aim for a daily caloric deficit of 500-750 calories.")
st.write(f"Your ideal caloric deficit is {deficit:.2f} calories per day.")

st.write("GENERAL GUIDANCE")
st.write("BMR (Basal Metabolic Rate) is the number of calories your body needs to maintain basic functions like breathing and circulation. The calculation here is based on the Harris-Benedict Equation.")
st.write("TDEE (Total Daily Energy Expenditure) is the product of your BMR and a factor of your activity level.")
import streamlit as st

st.title("🎉 Interactive Greeting App 🎉")

Name= st.text_input("Enter Your Name:")
if st.button("Press Here"):
    st.success(f"Welcome ***{Name}***")

st.title("➗ Simple Calculator")

num1 = st.number_input("Enter first Number")
num2 = st.number_input("Enter Second Number")

operation =st.radio("Choose:",["Addition","Subtraction","Multiplication","Division"])

if st.button ("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        result = "Cannot divide by zero" if num2 == 0 else num1 / num2
    st.info(f"Result: {result}")


st.title("🌦️ Weather App Skeleton")

city = st.text_input("Enter City Name:")
import google.generativeai as genai
genai.configure(api_key = st.secrets["GOOGLE_API_KEY"])

if st.button("Get Weather"):
    if city:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"give a simple weather report on {city}.")
        st.success(response.text)
    else:
        st.warning("Please Enter A City")

# st.title("🌦️ Weather App Skeleton")

# city = st.text_input("Enter City Name:")

# # Load API key safely
# genai.configure(api_key =st.secrets["AIzaSyA8Y0cZ3ZSyPL7HAduolDbA99WtP85yA6g"])

# # Configure Gemini API
# genai.configure(api_key=api_key)

# if st.button("Get Weather"):
#     if city:
#         model = genai.GenerativeModel("gemini-1.5-flash")
#         response = model.generate_content(f"Give a simple weather report for {city}.")
#         st.success(response.text)
#     else:
#         st.warning("Please enter a city name.")

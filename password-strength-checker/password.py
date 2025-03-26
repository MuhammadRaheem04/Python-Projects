
import streamlit as st
import re

st.set_page_config("Password Strength Checker", page_icon="🔒")

st.title("🔐 Password Strength Checker")
st.markdown("""
## Welcome to Ultimate Password Strength Checker! 👏
Use this tool to check the strength of your Password.
We will help you to create an **Strong Password!** """)

password = st.text_input("Enter Your Password:", type="password")

feedback = []

score = 0

if (password):
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be atleast 8 charectors long")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain both upper and lower case charectors")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Passward should contain atleast one digit.")

    if re.search(r'[!@#$%&*]', password):
        score += 1
    else:
        feedback.append("Passward should contain atleast one special charector (!@#$%&*).")

    if score == 4:
        feedback.append("Your Password is strong✅")

    elif score == 3:
         feedback.append("🟡Your Password is of medium srength, It could be strong!")

    else:
         feedback.append("🔴Your Password is weak, make it strong!")

    if (feedback):
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
            st.write(tip)

else:
    st.info("Plz Enter your Password to get started!")


    



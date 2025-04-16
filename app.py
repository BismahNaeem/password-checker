import streamlit as st
from zxcvbn import zxcvbn
import random
import string

# Function to analyze password strength
def password_strength(password):
    if not password:
        return 'No input', 'gray', None

    result = zxcvbn(password)
    score = result['score']

    if score == 0:
        return 'Very Weak', 'red', result
    elif score == 1:
        return 'Weak', 'orange', result
    elif score == 2:
        return 'Moderate', 'yellow', result
    elif score == 3:
        return 'Strong', 'blue', result
    elif score == 4:
        return 'Very Strong', 'green', result
    return 'Unknown', 'gray', result

# Function to suggest a strong password
def suggest_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit App UI
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")
st.title("🔐 Password Strength Checker")
st.markdown("Check how strong your password is, get suggestions, and helpful tips!")

password = st.text_input("Enter your password", type='password')

if password:
    strength, color, result = password_strength(password)
    st.markdown(f"**Password Strength:** <span style='color:{color}; font-size: 20px'>{strength}</span>", unsafe_allow_html=True)

    if result:
        st.write("🔎 **Details:**")
        st.write(f"- Crack time (offline): `{result['crack_times_display']['offline_slow_hashing_1e4_per_second']}`")
        if result['feedback']['warning']:
            st.warning(f"⚠️ {result['feedback']['warning']}")
        if result['feedback']['suggestions']:
            for suggestion in result['feedback']['suggestions']:
                st.info(f"💡 {suggestion}")

# Suggest strong password
if st.button("🔁 Suggest a Strong Password"):
    strong_pass = suggest_password()
    st.text_input("Here's a strong password you can use:", value=strong_pass, disabled=True)

# Tips for creating strong passwords
st.markdown("---")
st.markdown("### 🛡️ Tips for Creating a Strong Password:")
st.markdown("""
- Use **uppercase**, **lowercase**, **numbers**, and **symbols**.
- Avoid common words, names, and patterns.
- Make it at least **12 characters** long.
- Don’t reuse old passwords.
""")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit and zxcvbn-python.")

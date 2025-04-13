import streamlit as st
import re

def check_password_strength(password):
    score = 0
    suggestions = []

    # 1. Check password length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("❌ Password should be at least 8 characters long.")

    # 2. Check for both uppercase and lowercase letters
    if any(char.isupper() for char in password) and any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("❌ Use both uppercase (A-Z) and lowercase (a-z) letters.")

    # 3. Check for at least one digit
    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("❌ Add at least one number (0-9).")

    # 4. Check for special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("❌ Add at least one special character (!@#$%^&*).")

    return score, suggestions

# 🌟 Streamlit UI
st.set_page_config(page_title="🔐 Password Strength Meter", layout="centered")
st.title("🔐 Password Strength Meter")
st.write("Check how strong your password is!")

password = st.text_input("Enter your password", type="password")

if password:
    score, suggestions = check_password_strength(password)
    
    st.subheader("🔍 Analysis:")
    
    if score == 4:
        st.success("✅ Great! Your password is strong. 🔒")
    elif score == 3:
        st.warning("⚠️ Your password is okay, but it can be stronger:")
        for tip in suggestions:
            st.markdown(f"- {tip}")
    else:
        st.error("❌ Weak password! Please improve it:")
        for tip in suggestions:
            st.markdown(f"- {tip}")

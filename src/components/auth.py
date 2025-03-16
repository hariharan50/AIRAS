import streamlit as st
from config.settings import USERS_DB

def auth_page():
    if st.session_state.user_authenticated:
        _show_logged_in_state()
        return

    auth_tabs = st.tabs(["Login", "Sign Up"])
    with auth_tabs[0]:
        _show_login_form()
    with auth_tabs[1]:
        _show_signup_form()

def _show_login_form():
    with st.form("Login Form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.form_submit_button("Login"):
            if email in USERS_DB and USERS_DB[email]['password'] == password:
                st.session_state.user_authenticated = True
                st.session_state.username = USERS_DB[email]['name']
                st.rerun()
            else:
                st.error("Invalid credentials")

def _show_signup_form():
    with st.form("signup_form", clear_on_submit=True):
        new_email = st.text_input("Email")
        new_name = st.text_input("Full Name")
        new_password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        submitted = st.form_submit_button("Create Account", use_container_width=True)
        
        if submitted:
            if new_email in USERS_DB:
                st.error("Email already exists")
            elif new_password != confirm_password:
                st.error("Passwords don't match")
            else:
                USERS_DB[new_email] = {
                    'password': new_password,
                    'name': new_name
                }
                st.success("Account created successfully! Please login.")
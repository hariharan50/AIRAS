import streamlit as st

def init_session_state():
    """Initialize the application's session state"""
    session_defaults = {
        'current_page': 'Summarizer',
        'user_authenticated': False,
        'username': '',
        'selected_article': None,
        'selected_model': "Gemini",
        'user_api_keys': {'gemini': '', 'openai': ''},  #apikey
        'feedback_history': [],
        'search_history': [],
        'generated_summaries': {}
    }

    for key, value in session_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def get_users_db():
    """Get the users database"""
    if 'users_db' not in st.session_state:
        st.session_state.users_db = {
            'admin@researchanalyzer.ai': {
                'password': 'admin123',
                'name': 'Admin'
            },
            'demo@example.com': {
                'password': 'demo123',
                'name': 'Demo User'
            }
        }
    return st.session_state.users_db
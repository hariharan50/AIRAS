import streamlit as st

def init_session_state():
    """Initialize session state variables"""
    default_states = {
        'current_page': 'Summarizer',
        'user_authenticated': False,
        'username': '',
        'selected_article': None,
        'search_history': [],
        'generated_summaries': {},
        'feedback_history': [],
        'user_api_keys': {
            'gemini': '',
            'openai': ''
        }
    }
    
    for key, value in default_states.items():
        if key not in st.session_state:
            st.session_state[key] = value
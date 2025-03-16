import streamlit as st
from streamlit_option_menu import option_menu
from config.settings import DEFAULT_SETTINGS
from config.styles import CUSTOM_CSS
from components.auth import auth_page
from components.summarizer import show_summarizer
from components.quickview import show_quickview
from components.help import help_page
from components.feedback import feedback_page
from utils.session import init_session_state

def run_app():
    # Initialize session state
    init_session_state()

    # Page configuration
    st.set_page_config(
        page_title="Research Paper Analyzer",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Apply custom CSS
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

    # Sidebar navigation
    with st.sidebar:
        st.markdown('<div class="sidebar-title">🔬 Research Paper Analyzer</div>', unsafe_allow_html=True)

        if st.session_state.user_authenticated:
            st.markdown(f"👤 Welcome, {st.session_state.username}!")

            # API Keys management
            with st.expander("🔑 API Settings"):
                st.session_state.user_api_keys['gemini'] = st.text_input(
                    "Gemini API Key",
                    value=st.session_state.user_api_keys['gemini'],
                    type="password"
                )
                st.session_state.user_api_keys['openai'] = st.text_input(
                    "OpenAI API Key",
                    value=st.session_state.user_api_keys['openai'],
                    type="password"
                )

        # Navigation menu
        menu_choice = option_menu(
            None,
            ["📝 Summarizer", "🚀 QuickView", "🔐 Login/Signup", "❓ Help", "📬 Feedback"],
            icons=['journal-text', 'rocket', 'person', 'question-circle', 'chat'],
            default_index=0
        )

        st.session_state.current_page = menu_choice.split()[1]

    # Main content router
    if st.session_state.current_page == 'Summarizer':
        if not st.session_state.user_authenticated:
            st.warning("Please login to use the summarizer")
            auth_page()
        else:
            show_summarizer()
    elif st.session_state.current_page == 'QuickView':
        if not st.session_state.user_authenticated:
            st.warning("Please login to use QuickView")
            auth_page()
        else:
            show_quickview()
    elif st.session_state.current_page == 'Login/Signup':
        auth_page()
    elif st.session_state.current_page == 'Help':
        help_page()
    elif st.session_state.current_page == 'Feedback':
        feedback_page()

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        <p>🔬 Research Paper Analyzer v2.1 | 📚 Making Research Accessible</p>
        <p>⚡ Powered by Streamlit | 🤖 AI by Gemini & GPT-3.5</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    run_app()
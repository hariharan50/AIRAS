import streamlit as st
from datetime import datetime

def feedback_page():
    st.title("📬 Feedback & History")
    
    # Feedback form
    st.subheader("Share Your Feedback")
    with st.form("feedback_form", clear_on_submit=True):
        feedback_type = st.selectbox(
            "Feedback Type",
            ["General Feedback", "Bug Report", "Feature Request", "Summary Quality"]
        )
        
        feedback_text = st.text_area(
            "Your Feedback",
            height=150,
            placeholder="Please share your thoughts..."
        )
        
        rating = st.slider(
            "Rate your experience",
            min_value=1,
            max_value=5,
            value=5,
            help="1 = Poor, 5 = Excellent"
        )
        
        col1, col2 = st.columns(2)
        with col1:
            email = st.text_input("Email (optional)", help="For follow-up if needed")
        with col2:
            category = st.selectbox(
                "Category",
                ["UI/UX", "Performance", "Features", "Accuracy", "Other"]
            )
        
        submitted = st.form_submit_button("Submit Feedback", use_container_width=True)
        
        if submitted:
            feedback_entry = {
                "type": feedback_type,
                "text": feedback_text,
                "rating": rating,
                "email": email,
                "category": category,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            if "feedback_history" not in st.session_state:
                st.session_state.feedback_history = []
            
            st.session_state.feedback_history.append(feedback_entry)
            st.success("Thank you for your feedback!")
    
    # Display feedback history
    if st.session_state.feedback_history:
        st.markdown("---")
        st.subheader("📜 Previous Feedback")
        
        for idx, feedback in enumerate(reversed(st.session_state.feedback_history)):
            with st.expander(f"Feedback #{len(st.session_state.feedback_history) - idx}", expanded=False):
                st.markdown(f"**Type:** {feedback['type']}")
                st.markdown(f"**Category:** {feedback['category']}")
                st.markdown(f"**Rating:** {'⭐' * feedback['rating']}")
                st.markdown(f"**Feedback:** {feedback['text']}")
                st.markdown(f"**Submitted:** {feedback['timestamp']}")
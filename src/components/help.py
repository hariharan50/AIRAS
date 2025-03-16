import streamlit as st

def help_page():
    st.title("❓ Help & Support")

    with st.expander("🚀 Getting Started", expanded=True):
        st.markdown("""
        1. **Search Papers**
           - Use keywords or paper titles
           - Filter by date and relevance
           - Access full PDF links
        
        2. **Generate Summaries**
           - Choose between AI models
           - Get structured analysis
           - Save and export summaries
        
        3. **QuickView Feature**
           - Upload PDFs directly
           - Get instant insights
           - Compare multiple papers
        """)
    
    with st.expander("🔍 Search Tips", expanded=False):
        st.markdown("""
        - Use quotes for exact phrases: "machine learning"
        - Combine terms with AND/OR: deep learning AND neural networks
        - Use parentheses for complex queries: (AI OR "artificial intelligence") AND healthcare
        - Filter by date range for recent papers
        """)
    
    with st.expander("💡 Best Practices", expanded=False):
        st.markdown("""
        - Keep search terms specific and relevant
        - Compare summaries from different AI models
        - Save important summaries for later reference
        - Use QuickView for rapid paper screening
        - Provide feedback to help improve the system
        """)
    
    with st.expander("⚠️ Troubleshooting", expanded=False):
        st.markdown("""
        **Common Issues:**
        1. **Search not working**
           - Check internet connection
           - Try different search terms
           - Reduce number of results
        
        2. **Summary generation failed**
           - Verify API keys are correct
           - Try regenerating the summary
           - Check if the paper is accessible
        
        3. **PDF upload issues**
           - Ensure file is in PDF format
           - Check file size (max 10MB)
           - Try copying text directly
        """)
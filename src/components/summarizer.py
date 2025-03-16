import streamlit as st
from services.arxiv_service import AdvancedArxivClient  # Updated import
from services.ai_service import AIService

def show_summarizer():
    # Initialize the ArXiv client
    arxiv_client = AdvancedArxivClient()
    
    st.title("📝 AI Research Summarizer")

    if st.session_state.selected_article is None:
        # Search Interface
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                search_query = st.text_input("🔍 Search arXiv papers",
                                             placeholder="Enter keywords or paper titles")
            with col2:
                st.write("")
                st.write("")
                if st.button("🚀 Search", use_container_width=True):
                    if search_query:
                        with st.spinner("Searching arXiv..."):
                            results = arxiv_client.search(search_query)
                            st.session_state.search_history = results
                    else:
                        st.warning("Please enter a search query")

        # Display Results
        if st.session_state.search_history:
            st.subheader("📄 Search Results")
            for idx, article in enumerate(st.session_state.search_history):
                with st.expander(article['title'], expanded=False):
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        st.markdown(f"**Authors**: {', '.join(article['authors'][:3])}...")
                        st.markdown(f"**Published**: {article['published']}")
                    with col2:
                        st.markdown(f"**Abstract**: {article['abstract'][:400]}...")

                    # Enhanced preview with a progress bar for visual appeal
                    st.markdown("""
                    <div style="background-color: #00000; padding: 9px; border-radius: 5px; 
                    border-left: 4px solid #4CAF50; margin-top: 5px;">
                        <p style="font-style: italic; color: #555;">Click to view AI-enhanced summary, key findings, and visual analysis</p>
                    </div>
                    """, unsafe_allow_html=True)

                    if st.button("📊 View Full Summary", key=f"view_{idx}"):
                        st.session_state.selected_article = idx
                        st.rerun()
    else:
        # Detailed View
        article = st.session_state.search_history[st.session_state.selected_article]

        # Back button with improved styling
        col_back, col_title = st.columns([1, 5])
        with col_back:
            if st.button("← Back", use_container_width=True):
                st.session_state.selected_article = None
                st.rerun()

        with col_title:
            st.markdown(f"## {article['title']}")

        st.markdown("---")

        col1, col2 = st.columns([1, 2])

        with col1:
            st.markdown("### 📚 Article Details")
            st.markdown(f"""
            - **Authors**: {', '.join(article['authors'])}
            - **Publication Date**: {article['published']}
            - **Categories**: {', '.join(article['categories'])}
            """)
            if article['doi']:
                st.markdown(f"- **DOI**: [{article['doi']}](https://doi.org/{article['doi']})")

            st.markdown("</div>", unsafe_allow_html=True)

            # Download button with improved styling
            st.markdown(f"""
            <a href="{article['pdf_url']}" target="_blank">
                <button style="background-color: #4CAF50; color: white; padding: 10px 20px; 
                border: none; border-radius: 4px; cursor: pointer; margin-top: 10px; width: 100%;">
                    📥 Download Full PDF
                </button>
            </a>
            """, unsafe_allow_html=True)

            # Citation information
            st.markdown("### 📝 Citation")
            authors_citation = ", ".join(article['authors'])
            st.code(f"{authors_citation}. ({article['published'][:4]}). {article['title']}. arXiv.", language="text")

        with col2:
            # AI model selection with tabs
            model_tabs = st.tabs(["Gemini Summary", "GPT-3.5 Summary"])

            # Generate and display summary
            entry_id = article['entry_id']

            # AI summary prompts enhanced for better formatting
            summary_prompt = """
            Analyze this research paper abstract and provide:

            1. KEY FINDINGS:
            - Provide 3-5 bullet points of the main findings

            2. METHODOLOGY:
            - Brief paragraph on methods used

            3. IMPLICATIONS:
            - 2-3 bullet points on the significance of this research

            Abstract: {text}
            """

            with model_tabs[0]:  # Gemini tab
                if entry_id not in st.session_state.generated_summaries:
                    with st.spinner("Generating AI summary..."):
                        summary = AIService.generate_content(
                            summary_prompt,
                            article['abstract'],
                            "Gemini"
                        )
                        st.session_state.generated_summaries[entry_id] = summary

            # GPT-3.5 tab
            with model_tabs[1]:  # GPT-3.5 tab
                gpt_key = f"{entry_id}_gpt"
                if gpt_key not in st.session_state.generated_summaries:
                    if st.session_state.user_api_keys['openai']:
                        with st.spinner("Generating GPT-3.5 summary..."):
                            summary = AIService.generate_content(
                                summary_prompt,
                                article['abstract'],
                                "GPT-3.5"
                            )
                            st.session_state.generated_summaries[gpt_key] = summary
                    else:
                        st.session_state.generated_summaries[
                            gpt_key] = "⚠️ Please add your OpenAI API key in settings to use GPT-3.5."



            st.markdown("---")
            st.markdown("### 📖 Original Abstract")

            # Format abstract with paragraph breaks for better readability
            formatted_abstract = article['abstract'].replace(". ", ".\n\n")
            st.markdown(
                f'<div style="background: #00000; padding: 15px; border-radius: 5px;">{formatted_abstract}</div>',
                unsafe_allow_html=True)

            # User feedback section
            st.markdown("### Was this summary helpful?")
            col_yes, col_no = st.columns(2)
            with col_yes:
                if st.button("👍 Yes", use_container_width=True):
                    st.success("Thanks for your feedback!")
            with col_no:
                if st.button("👎 No", use_container_width=True):
                    st.info("We'll improve our summaries. Please consider leaving detailed feedback.")
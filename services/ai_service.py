import google.generativeai as genai
import openai
import streamlit as st

class AIService:
    @staticmethod
    def get_active_api_key(model_type):
        model_key = model_type.lower()
        return st.session_state.user_api_keys.get(model_key, '')

    @staticmethod
    def generate_content(prompt, text, model_type):
        try:
            api_key = AIService.get_active_api_key(model_type)
            if not api_key:
                return f"⚠️ Please add your {model_type} API key in settings."

            if model_type == "Gemini":
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-pro')
                response = model.generate_content(prompt.format(text=text))
                return response.text

            elif model_type == "GPT-3.5":
                openai.api_key = api_key
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful research paper analysis assistant."},
                        {"role": "user", "content": prompt.format(text=text)}
                    ],
                    temperature=0.7,
                    max_tokens=1000
                )
                return response.choices[0].message.content

            else:
                return "⚠️ Unsupported model type"

        except Exception as e:
            return f"⚠️ Error generating content: {str(e)}"

    @staticmethod
    def analyze_sentiment(text, model_type="Gemini"):
        sentiment_prompt = """
        Analyze the sentiment and key emotions in the following text. 
        Provide a brief summary of the overall tone and emotional content.
        
        Text: {text}
        """
        return AIService.generate_content(sentiment_prompt, text, model_type)

    @staticmethod
    def generate_keywords(text, model_type="Gemini"):
        keyword_prompt = """
        Extract the most important keywords and phrases from the following text.
        Focus on technical terms, methodologies, and key concepts.
        
        Text: {text}
        """
        return AIService.generate_content(keyword_prompt, text, model_type)
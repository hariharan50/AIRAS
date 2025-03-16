import google.generativeai as genai
import openai
import streamlit as st

class AIService:
    @staticmethod
    def generate_content(prompt, text, model_type):
        try:
            api_key = AIService._get_api_key(model_type)

            if model_type == "Gemini":
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-pro')
                response = model.generate_content(prompt.format(text=text))
                return response.text

            elif model_type == "GPT-3.5":
                openai.api_key = api_key
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt.format(text=text)}],
                    temperature=0.7
                )
                return response.choices[0].message.content

        except Exception as e:
            return f"⚠️ AI Service Error: {str(e)}"

    @staticmethod
    def _get_api_key(model_type):
        model_key = model_type.lower()
        user_key = st.session_state.user_api_keys[model_key]
        return user_key if user_key else 'your-default-api-key'
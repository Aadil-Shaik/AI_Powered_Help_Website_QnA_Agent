import os
import google.generativeai as genai

class GeminiAPI:
    def __init__(self, api_key=None):
        api_key = api_key or os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("Gemini API key is required.")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('models/gemini-2.0-flash')

    def generate_answer(self, query, context):
        """Generate an answer using Gemini API based on retrieved documentation."""
        prompt = f"""
        You are an AI assistant helping users with documentation. Use ONLY the provided context.

        Question: {query}

        Context:
        {context}

        Instructions:
        - Provide a **clear and detailed answer**.
        - If step-by-step instructions exist, **list them numerically**.
        - If troubleshooting is required, **explain possible causes and solutions**.
        - **If no answer is found**, suggest **related information** from the context.
        - **DO NOT** say "Based on the context provided"—just give the answer.

        Answer:
        """

        response = self.model.generate_content(prompt, stream=False)
        return response.text.strip()

gemini_api_instance = GeminiAPI()

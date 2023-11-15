from openai import OpenAI
import streamlit as st
import os

API_KEY = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=API_KEY)
print(API_KEY)


def send_to_chatgpt(cv, application, about, job, language, customInstruction):
    try:
        # Determine if the applicant has provided existing application text
        application_content = f"This is the applicant's current application: {application}\n" if application else "The applicant has not written any application text yet.\n"

        # Constructing the chat message
        messages = [
            {"role": "system", "content": "You are a professional job application writer."},
            {"role": "user", "content":
              f"This is the applicant's CV: {cv}\n"
               + application_content
               + f"This is the job application/description: {job}\n" 
               + f"This is the 'About Us' page of the company the applicant is applying to: {about}"
            },
            {"role": "system", "content": f"Write a job application for the applicant in {language}. "
             + f"Use these custom instructions to write the application: {customInstruction}"
             }
        ]
        
        response = client.chat.completions.create(model="gpt-4",
        messages=messages,
        max_tokens=1500)
        
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return {"error": str(e)}

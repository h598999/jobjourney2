import streamlit as st

with open("custom_instruction.txt", "r") as f:
    customInstruction = f.read()

st.title('Job application generator')

st.write("Upload your CV, input your current Cover Letter, as well as the URL for the company's 'About Us' page and the job application page. Then click 'Generate job application' to generate a new job application.")

st.subheader("CV")
cv_upload = st.file_uploader("CV", type=['pdf'])

st.subheader("Current Cover Letter")
application_upload = st.file_uploader("Upload Cover letter (PDF)", type=['pdf'])
application_text = st.text_area("Or input Cover letter text here")

aboutUs = st.text_input("About us URL")
jobApplication = st.text_input("Job application URL")

language = st.selectbox("Language", ["English", "Norwegian"])

st.write(cv_upload.name, application_upload.name)

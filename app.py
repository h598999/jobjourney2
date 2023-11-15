import streamlit as st
from pdf_extractor import extract_text_from_pdf
from gpt import send_to_chatgpt
from web_scrape import fetch_website_content

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

response = ""
if st.button("Generate job application"):
    # Check if the CV has been uploaded
    if not cv_upload:
        st.error('Please upload your CV.')
    # Check if the URLs have been entered
    elif not aboutUs or not jobApplication:
        st.error('Please enter both the About us URL and the Job application URL.')
    else:
        with st.spinner('Generating...'):
            # Process the files and URLs
            cv = extract_text_from_pdf(cv_upload)

            # Use uploaded application text if available, otherwise use the text input
            application = ""
            if application_upload:
                application = extract_text_from_pdf(application_upload)
            elif application_text:
                application = application_text

            about = fetch_website_content(aboutUs)
            job = fetch_website_content(jobApplication)

            # Call the function to send data to the model
            response = send_to_chatgpt(cv, application, about, job, language, customInstruction)

    # Output the response outside the spinner context
    st.write(response)

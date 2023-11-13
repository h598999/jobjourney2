from PyPDF2 import PdfReader

def extract_text_from_pdf(uploaded_pdf):
    try:
        pdf = PdfReader(uploaded_pdf)
        
        # Check if the PDF is encrypted
        if pdf.is_encrypted:
            raise ValueError("The provided PDF is password protected and cannot be processed.")
        
        # Use a list to accumulate the extracted text for memory efficiency
        extracted_texts = [pdf.pages[page].extract_text() for page in range(len(pdf.pages))]
        
        # Join the list to get the complete text
        text = "".join(extracted_texts)
        
        return text
    except Exception as e:
        # Handle general exceptions and return an appropriate message
        return f"An error occurred while processing the PDF: {str(e)}"
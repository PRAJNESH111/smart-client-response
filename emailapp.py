import streamlit as st
from urllib.parse import quote
from ml_backend import ml_backend

# Page Title
st.title("Email Generator")
st.markdown("# Generate Email")

# Backend Initialization
backend = ml_backend()

# Form for input
with st.form(key="form"):
    from_name = st.text_input("Your Name:")
    client_first_name = st.text_input("Client's First Name:")
    client_last_name = st.text_input("Client's Last Name:")
    client_email = st.text_input("Client's Email:")
    client_country = st.text_input("Client's Country:")
    client_location = st.text_input("Client's Location:")
    client_language = st.text_input("Client's Language:")
    project_type = st.text_input("Project Type:")
    service_category = st.text_input("Service Category:")
    client_website = st.text_input("Client's Website:")
    additional_info = st.text_area("Additional Information:")

    submit_button = st.form_submit_button(label="Generate Email")

if submit_button:
    with st.spinner("Generating Email..."):
        output = backend.generate_email(
            from_name, client_first_name, client_last_name, client_email,
            client_country, client_location, client_language, project_type,
            service_category, client_website, additional_info
        )

    # Display the generated email
    st.markdown("# Email Output:")
    st.markdown(f"Subject: {project_type} - {service_category}\n\nDear {client_first_name},\n\n{output}")

    # Construct the email URL
    subject = f"{project_type} - {service_category}"
    body = f"\n\n{output}"
    encoded_url = f"https://mail.google.com/mail/?view=cm&fs=1&to={client_email}&su={quote(subject)}&body={quote(body)}"

    # Add a button for sending the email
    st.markdown(
        f'<a href="{encoded_url}" target="_blank" style="display: inline-block; padding: 10px 15px; '
        f'background-color: #4CAF50; color: white; text-decoration: none; border-radius: 5px;">Send Email</a>',
        unsafe_allow_html=True,
    )

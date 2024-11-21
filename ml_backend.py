import openai
import time
from openai.error import RateLimitError

class ml_backend:
    def __init__(self):
        # Replace with your actual OpenAI API key in production (use environment variables for safety)
        openai.api_key = "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"

    def generate_email(
        self, from_name, client_first_name, client_last_name, client_email,
        client_country, client_location, client_language, project_type,
        service_category, client_website, additional_info
    ):
        """Generates a personalized email using GPT-3.5 Turbo."""
        
        # Define a detailed and structured prompt
        userPrompt = f"""
You are a professional email assistant. Generate a business email for the following scenario:
- **From Name**: {from_name}
- **Client First Name**: {client_first_name}
- **Client Last Name**: {client_last_name}
- **Client Email**: {client_email}
- **Client Country**: {client_country}
- **Client Location**: {client_location}
- **Client Language**: {client_language}
- **Project Type**: {project_type}
- **Service Category**: {service_category}
- **Client Website**: {client_website}
- **Additional Information**: {additional_info}

Format the email as follows:
1. Subject: A short and professional subject line based on the project type and service category.
2. Greeting: Address the client using their full name.
3. Body: Start with a thank-you message, followed by a brief explanation of how the project requirements will be met. Ensure a polite, formal tone.
4. Closing: Include a request for further discussion if required and sign off with "Best regards, {from_name}".

Ensure the tone is polite, professional, and focused on meeting the client's needs.
        """
        
        retries = 5
        delay = 5  # Initial delay in seconds

        for attempt in range(retries):
            try:
                # Make the API call to generate a response
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are an email assistant."},
                        {"role": "user", "content": userPrompt}
                    ],
                    temperature=0.7,  # Adjust for creativity
                    max_tokens=300,  # Limit to avoid overflows
                    top_p=1,
                    frequency_penalty=0.36,
                    presence_penalty=0.75
                )
                return response['choices'][0]['message']['content'].strip()

            except RateLimitError:
                if attempt < retries - 1:
                    print(f"Rate limit exceeded. Retrying in {delay} seconds... (Attempt {attempt + 1}/{retries})")
                    time.sleep(delay)
                    delay *= 2  # Exponential backoff
                else:
                    return "Failed to generate email due to rate limit. Please try again later."

    def replace_spaces_with_pluses(self, sample):
        """Formats a string for a hyperlink by replacing spaces with '+'."""
        return '+'.join(sample.split())

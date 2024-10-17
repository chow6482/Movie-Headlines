import json  # Add the json module
from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)

# Define the conversation with system, user, and assistant messages
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an expert movie critic in the style of Siskel & Ebert."},
        {"role": "user", "content": "I need 10 creative headlines for a review of my favorite movie, 'The Dark Knight', with a mix of positive and critical tones."},
        {"role": "assistant", "content": "Sure! I'll create a mix of headlines in the style of Siskel & Ebert."}
    ]
)

# Extract the API response correctly
headlines_text = response.choices[0].message.content  # Correct way to access the content

# Clean up quotes and prepare the final JSON output
headlines = [headline.strip().replace('\"', '') for headline in headlines_text.strip().split("\n")]

review_headlines = {
    "movie": "The Dark Knight",
    "headlines": headlines
}

# Pretty print the JSON response
print(json.dumps(review_headlines, indent=4))  # Use json.dumps to format the output with indentation

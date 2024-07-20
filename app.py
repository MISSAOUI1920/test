import streamlit as st
from huggingface_hub import InferenceClient

# Initialize the InferenceClient
client = InferenceClient(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    token="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"
)

# Function to handle chat completion
def get_chat_completion(prompt):
        response = ""
        for message in client.chat_completion(
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            stream=True,
        ):
            response += message.choices[0].delta.content
        return response
user_input = st.text_input("Enter your question:")

if st.button("Get Solution"):
        if user_input:
            with st.spinner("Generating response..."):
                response = get_chat_completion(user_input)
            st.write(response)
        else:
            st.write("Please enter a message.")

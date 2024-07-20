import streamlit as st
from huggingface_hub import InferenceClient

# Initialize the InferenceClient
client = InferenceClient(
    model_id="meta-llama/Meta-Llama-3-8B-Instruct",
    token="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",
)

# Function to handle chat completion
def chat_with_model():
    messages = [{"role": "user", "content": "What is the capital of France?"}]
    for message in client.chat_completion(
        messages=messages,
        max_tokens=500,
        stream=True,
    ):
        # Streamlit component to display the streamed response
        st.write(message['choices'][0]['delta']['content'])

# Streamlit app layout
st.title("Chat with Meta-Llama Model")
if st.button("Ask"):
    chat_with_model()

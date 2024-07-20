import streamlit as st
from huggingface_hub import InferenceClient
client = InferenceClient(
        "meta-llama/Meta-Llama-3-8B-Instruct",
        token="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",
    )
for message in client.chat_completion(
	messages=[{"role": "user", "content": "What is the capital of France?"}],
	max_tokens=500,
	stream=True,
):
    st.write(message.choices[0].delta.content, end="")

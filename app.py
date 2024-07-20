from huggingface_hub import InferenceClient
import streamlit as st
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

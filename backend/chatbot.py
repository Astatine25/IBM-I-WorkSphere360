from vertexai.preview.generative_models import GenerativeModel

model = GenerativeModel("gemini-1.5-pro")

def leave_chat(user_role, message, context):
    prompt = f"""
    User Role: {user_role}
    Context: {context}
    Question: {message}
    """
    response = model.generate_content(prompt)
    return response.text

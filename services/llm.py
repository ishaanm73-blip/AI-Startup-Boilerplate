from openai import OpenAI
client = OpenAI()
def answer_questions(question, context):
    prompt = f"""Answer the question based on the given context.
Context: {context}
Question: {question}
Answer:"""
    response = client.chat.completions.create(
        model="gpt-5.1",
        messages=[{'role': 'user', 'content': prompt}]
    )
    return response.choices[0].message['content']

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()  # loads OPENROUTER_API_KEY from .env

# Use OpenRouter's automatic free model router
# This automatically picks from available free models based on your needs
llm = ChatOpenAI(
    api_key=os.environ.get("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    model="openrouter/free",  # Automatically selects from available free models
    temperature=0.7,
)

chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]

print("LangChain Chatbot (OpenRouter automatic free tier)")
print("Using openrouter/free - auto-selects from available free models")
print("Type 'exit' to quit\n")

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == 'exit':
        break
    
    try:
        result = llm.invoke(chat_history)
        chat_history.append(AIMessage(content=result.content))
        print("AI: ", result.content)
    except Exception as e:
        print(f"Error: {e}")
        print("\nIf you keep getting errors:")
        break

print("\nChat ended.")

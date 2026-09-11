from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langcahin_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model="gpt-4o", temperature=0.7, max_tokens=128)

chat_history = [
    SystemMessage(content="You are a helpful assistant.")
]
while True:
    user_input = input("User: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == "exits":
        break
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print(f"Bot: {response.content}")

print("chat session ended this is the chat history:")
print(chat_history)
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()



model=ChatOpenAI(model="gpt-4o", temperature=0.7, max_tokens=128)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="tell me a joke about cats.")
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))


print(messages)
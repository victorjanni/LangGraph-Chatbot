from langgraph.graph import StateGraph, START, END
from typing import TypedDict,Annotated
from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-20b"
)

class Chatstate(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: Chatstate):
    messages = state['messages']
    response = llm.invoke(messages)
    return {'messages': [response]}

# checkpointer
checkpointer = InMemorySaver()


graph = StateGraph(Chatstate)

graph.add_node("chat_node", chat_node)

graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)

# config = {
#     "configurable": {
#         "thread_id": "user-1"
#     }
# }

# response = chatbot.invoke({
#     'messages': [HumanMessage(content="Hello, how are you?")]
# }, config)


# print(response['messages'][-1].content)
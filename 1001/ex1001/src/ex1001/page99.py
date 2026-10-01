from typing import TypedDict, Annotated
from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph.message import add_messages

def add(left,right):
    return left + right

# 상태값 리듀서 예시
class State(TypedDict):
    # 리듀서가 지정된 필드 (add 리듀서를 사용)
    messages: Annotated[list[str], add]

# 기존state : HumanMessage
msgs1 = [HumanMessage(content="Hello", id="1")]

# 노드반환값 : AIMessage
msgs2 = [AIMessage(content="Hi there!", id="2")]

# 에이전트에 들어온 메세지 저장용: add_messages
result = add_messages(msgs1, msgs2)
print(result)
# [HumanMessage(content='Hello', additional_kwargs={}, response_metadata={}, id='1'), 
# AIMessage(content='Hi there!', additional_kwargs={}, response_metadata={}, id='2', tool_calls=[], invalid_tool_calls=[])]
from dotenv import load_dotenv

from langchain_groq.chat_models import ChatGroq
from pydantic import BaseModel
from langgraph.constants import END
from langgraph.graph import StateGraph
from langchain.tools import tool
from agent.prompts import *
from agent.states import *
from agent.tools import write_file, read_file, get_current_directory, list_files
from langgraph.prebuilt import create_react_agent



_ = load_dotenv()
import os

os.environ["LANGCHAIN_VERBOSE"] = "true"
os.environ["LANGCHAIN_DEBUG"] = "true"



from langchain_core.messages import HumanMessage, SystemMessage

def execute_tool_call(tool_call):
    tool_name = tool_call["name"]
    args = tool_call["args"]

    if tool_name not in TOOL_REGISTRY:
        raise ValueError(f"Unknown tool: {tool_name}")

    tool = TOOL_REGISTRY[tool_name]
    result = tool.invoke(args)

    return ToolMessage(
        content=str(result),
        tool_call_id=tool_call["id"]
    )





llm = ChatGroq(model="openai/gpt-oss-120b")
def Planner_agent(state:dict) ->dict:
    """Convert user propmt into a Structured Plan."""
    user_prompt = state['user_prompt']
    resp = llm.with_structured_output(Plan).invoke(
        planner_prompt(user_prompt)
    )
    if resp is None:
        raise  ValueError("planner Did not return a valid response.")
    return {"plan":resp}


def architect_agent(state: dict) -> dict:
    """Creates TaskPlan from Plan."""
    plan: Plan = state["plan"]
    resp = llm.with_structured_output(TaskPlan).invoke(
        architect_prompt(plan=plan.model_dump_json())
    )
    if resp is None:
        raise ValueError("Planner did not return a valid response.")

    resp.plan = plan
    print(resp.model_dump_json())
    return {"task_plan": resp}




CODER_TOOLS = [
    write_file,
    read_file,
    list_files,
    get_current_directory
]

TOOL_REGISTRY = {tool.name: tool for tool in CODER_TOOLS}

react_agent = create_react_agent(llm, CODER_TOOLS)

def coder_agent(state: dict) -> dict:
    coder_state = state.get("coder_state")

    if coder_state is None:
        coder_state = CoderState(
            task_plan=state["task_plan"],
            current_step_idx=0
        )

    steps = coder_state.task_plan.implementation_steps
    if coder_state.current_step_idx >= len(steps):
        return {"coder_state": coder_state, "status": "DONE"}

    current_task = steps[coder_state.current_step_idx]

    existing_content = read_file.invoke({
        "path": current_task.filepath
    })

    messages = [
        SystemMessage(content=coder_system_prompt()),
        HumanMessage(
            content=(
                f"Task: {current_task.task_description}\n"
                f"File: {current_task.filepath}\n"
                f"Existing content:\n{existing_content}\n"
                "Use write_file(path, content) to save your changes."
            )
        )
    ]

    response = react_agent.invoke({"messages": messages})

    # 🔥 EXECUTE TOOL CALLS
    tool_messages = []
    for tc in response["messages"][-1].tool_calls:
        tool_msg = execute_tool_call(tc)
        tool_messages.append(tool_msg)

    # (optional but recommended)
    messages.extend(tool_messages)

    coder_state.current_step_idx += 1

    return {
        "coder_state": coder_state,
        "messages": messages
    }



graph = StateGraph(dict)
graph.add_node("planner",Planner_agent)
graph.add_node("architect",architect_agent)
graph.add_node("coder", coder_agent)
graph.add_edge("planner", "architect")
graph.add_edge("architect", "coder")

graph.add_conditional_edges(
    "coder",
    lambda s: "END" if s.get("status") == "DONE" else "coder",
    {"END": END, "coder": "coder"}
)
graph.set_entry_point("planner")

agent = graph.compile()
if __name__ == "__main__":
    result = agent.invoke({"user_prompt": "Build a colourful modern todo app in html css and js"},
                          {"recursion_limit": 100})
    print("Final State:", result)

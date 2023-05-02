from __future__ import annotations

import sys
from io import StringIO

from dotenv import load_dotenv
from fastapi import FastAPI
from langchain.agents import AgentType
from langchain.agents import initialize_agent
from langchain.agents import load_tools
from langchain.llms import OpenAI
from pydantic import BaseModel

load_dotenv()


class Question(BaseModel):
    question: str


app = FastAPI()


@app.post("/ask")
def ask(question: Question) -> dict[str, str]:
    llm = OpenAI(temperature=0)
    tools = load_tools(["llm-math"], llm=llm)
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    backup = sys.stdout
    try:
        sys.stdout = StringIO()
        agent.run(question)
        answer = sys.stdout.getvalue()
    finally:
        sys.stdout.close()
        sys.stdout = backup
    return {"result": answer}

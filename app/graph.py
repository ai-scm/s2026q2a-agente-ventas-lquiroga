import json
import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from app.tools.sql_tool import execute_sql
from app.tools.chart_tool import create_chart
from app.tools.export_tool import export_csv

load_dotenv()

llm = ChatOpenAI(
    model="nvidia/nemotron-3-super-120b-a12b:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

ROUTER_PROMPT = open(
    "app/prompts/router_prompt.txt"
).read()

def run_agent(user_input, history=[]):

    conversation_context = ""

    for msg in history[-5:]:

        if msg["role"] == "user":

            conversation_context += f"""
            Usuario:
            {msg["content"]}
            """

    messages = [
        HumanMessage(
            content=f"""
            {ROUTER_PROMPT}

            Historial:
            {conversation_context}

            Nueva pregunta:
            {user_input}
            """
        )
    ]

    response = llm.invoke(messages)

    print("\n========== RESPUESTA RAW ==========")
    print(response.content)

    clean_response = (
        response.content
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    print("\n========== RESPUESTA LIMPIA ==========")
    print(clean_response)

    agent_output = json.loads(clean_response)

    sql_query = agent_output["sql"]

    print("\n========== SQL ==========")
    print(sql_query)

    df = execute_sql(sql_query)

    print("\n========== DATAFRAME ==========")
    print(df)

    chart = None
    csv_file = None

    # gráfico
    if agent_output["needs_chart"]:

        chart = create_chart(df)

    # csv
    if agent_output["needs_csv"]:

        csv_file = export_csv(df)

    return {
        "dataframe": df,
        "chart": chart,
        "csv": csv_file
    }

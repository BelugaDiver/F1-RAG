"""RAG Module talks to a database and an agent

Returns:
    string: the response from the llm
"""
    
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langgraph.prebuilt import create_react_agent
# from ViewAndTableDBSchemaTool import (ViewAndTableDBSchemaTool)

"""Queries an F1 sqlite database and returns a response augmented by AI.
"""
def rag(query: str) -> str:
    db = SQLDatabase.from_uri("sqlite:///f1db.db")
    api_key = "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"
    llm = ChatNVIDIA(model="meta/llama-3.1-405b-instruct",
                     temperature=0.2,
                     top_p=0.7,
                     max_tokens=1024,
                     api_key=api_key)

    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    tools = toolkit.get_tools()
    # del tools[1]

    # db_schema_tool = ViewAndTableDBSchemaTool(db=db)
    # tools.append(db_schema_tool)

    system = """You are an agent designed to interact with a SQL database.
    Given an input question, create a syntactically correct SQLite query to run, then look at the results of the query and return the answer.
    Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most 5 results.
    You can order the results by a relevant column to return the most interesting examples in the database.
    Never query for all the columns from a specific table, only ask for the relevant columns given the question.
    You have access to tools for interacting with the database.
    Only use the given tools. Only use the information returned by the tools to construct your final answer.
    You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.

    DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.

    You have access to the following tables and views: {table_names}
    
    Before deciding to query a table, make sure you understand the table schema by running the `sql_db_schema` command. You CANNOT run the sql_db_schema tool with a view as a parameter.
    
    Some useful table and view context includes:
    - `race_result` - view that lists all the driver_ids in the position they completed a specific race. You can look up what race is referenced through the race_id foreign key. You can look up which driver is referenced through the driver_id foreign key.
    - `race` - table that lists all of the formula 1 races, the year they were held, and other relevant information.
    - `season_driver_standing` - table that lists all of the drivers in the position_number they completed a season. The winner of a season always has the number 1 position for that year.
    - `season` - table that lists all the formula 1 years tracked in this database.
    - `grand_prix` - table that lists all of the offical grand prix and totals the number of races under each grand prix.
    - `sprint_race_result` - view that lists all driver_ids in the position_number they completed a sprint race. You can look up what race is referenced through the race_id foreign key. You can look up which driver is referenced through the driver_id foreign key.""".format(
        table_names=db.get_usable_table_names()
    )

    system_message = SystemMessage(content=system)
    agent = create_react_agent(llm, tools, messages_modifier=system_message)

    print("Performing Agent Requests:")
    messages = []
    for s in agent.stream({"messages": [HumanMessage(content=query)]}):
        messages.append(s)
        print(s)
        print("----")


    final_message: AIMessage = messages[-1]["agent"]["messages"][0]
    return final_message.content
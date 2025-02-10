from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import re


def sql_ddl_generator(details):
    template = """You are an SQL developer you have been provided with task to generate DDL for a table containing following details: \n{details}

    SQL command for this is \n```sql"""

    prompt = ChatPromptTemplate.from_template(template)

    model = OllamaLLM(model="deepseek-r1:1.5b")

    chain = prompt | model

    result = chain.invoke({"details": details})
    pattern = r"```(.*?)```"  
    matches = re.findall(pattern, result, re.DOTALL) 
    return matches

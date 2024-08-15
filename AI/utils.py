from langchain_openai import OpenAI
from langchain_core.prompts.few_shot import FewShotPromptTemplate
from langchain_core.prompts.prompt import PromptTemplate
from langchain.chains import LLMChain
from langchain_anthropic import ChatAnthropic
from .workers_comp_few_shots import work_comp_examples



# chatgptgit
# llm = OpenAI(openai_api_key=api_key)
# claude
# llm = ChatAnthropic(anthropic_api_key=claude_api_key,model="claude-3-sonnet-20240229",temperature=0)

def few_shot(orm_object,input_data):

    pass

    # my_data = input_data
    # template = """Exmaple: <input>{input}</input>\n\n
    #     <output>{output}</output>"""

    # examples = work_comp_examples

    # example_prompt = PromptTemplate(
    #     input_variables=["input", "output"], template= template
    # )

    # prompt = FewShotPromptTemplate(
    #     examples=examples,
    #     example_prompt=example_prompt,
    #     suffix="""</input>{my_data}<input>\n\n
    #     <output></output>
    #     Please also supply a copy in Spanish as well as English! :)
    #     """,
    #     input_variables=["my_data"],
    # )

    # print(prompt.format(my_data=my_data))
    # chain = LLMChain(
    #     llm=llm,
    #     prompt = prompt,
    # )

    # result = chain({
    #     "my_data":my_data
    # })

    # print(result["text"])

    # return(result["text"])
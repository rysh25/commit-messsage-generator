import sys

from dotenv import load_dotenv
from fire import Fire
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()


def generate_commit_message():
    diff = "\n".join(sys.stdin.readlines())

    template = """
    Please read the git diff output below and write your commit message concisely and clearly.
    
    '''
    {diff}
    '''
    """

    prompt = PromptTemplate(
        input_variables=["diff"],
        template=template,
    )

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.invoke({"diff": diff})

    print(result["text"])


if __name__ == "__main__":
    Fire(generate_commit_message)

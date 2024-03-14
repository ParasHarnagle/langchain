from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.tools import DuckDuckGoSearchRun

#generate video script
def generate_script(prompt, video_length, creativity, api_key):
    #title template
    title_template = PromptTemplate(
        input_variables = ['subject'],
        template ='Title for youtube video {subject}.'    
    )

    #script_template 
    script_template = PromptTemplate(
        input_variables = ['title','DuckDuckGo_Search', 'duration'],
        template = 'create script for yt video based TITLE:{title} of duration:{duration} using search data{DuckDuckGo_Search}'
    )

    #setting up OpenAI LLM
    llm = ChatOpenAI(temperature = creativity,
                    openai_api_key = api_key,
                    model_name = 'gpt-3.5-turbo' )
    
    #creating chain for 'Title' and 'Video script'
    title_chain = LLMChain(llm = llm,
                        prompt = title_template,
                        verbose = True)
    
    script_chain = LLMChain(llm=llm,
                        prompt = script_template,
                        verbose = True)

    # https://python.langchain.com/docs/modules/agents/tools/integrations/ddg
    search = DuckDuckGoSearchRun()

    # executing chain for title
    title = title_chain.invoke(prompt)

    #executing for video script
    search_result = search.run(prompt)
    script = script_chain.run(title = title,
                    DuckDuckGo_Search = search_result,
                    duration = video_length )
                    
    return search_result, title,script

    
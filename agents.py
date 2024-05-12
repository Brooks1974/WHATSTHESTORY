from crewai import Agent
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool, WebsiteSearchTool,YoutubeChannelSearchTool, TXTSearchTool




class ResearchCrewAgents:

    def __init__(self):
        # Initialize tools if needed
        self.serper = SerperDevTool()
        self.web = WebsiteSearchTool()
        self.txt_tool = TXTSearchTool()
        self.gpt3 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.gpt4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

#added in Editor
    def editor(self):
        # Detailed agent setup for the Editor
        return Agent(
            role='Newsletter Editor',
            goal='Oversee the creation of the newsltter. Ensure it is relevant to recent stories in {input}',
            backstory='You have a keen eye for detail and passion for storytelling. You ensure the newsletter is relevant to {inputs} and informs, engages and inspirses the readers.',            
            verbose=True,
            allow_delegation=True,
            max_iter=15,
            tools=[self.web],
            llm=self.gpt4,
        )

    def researcher(self):
        # Detailed agent setup for the Researcher
        return Agent(
            role='Research Expert',
            goal='Find current news stories about {input}',
            backstory='You search the internet for recent stories on {inputs}. You make sure our readers are always in the know',            
            verbose=True,
            allow_delegation=True,
            tools=[self.web],
            llm=self.gpt3,
        )

    def analyst(self):
        # Detailed agent setup for the Analyst
        return Agent(
            role='Data Analysis Specialist',
            goal='Analyze each news story and generate a detailed markdown summary',
            backstory='With a journalism degree from a prestigious university and years of experience as a news editor and content strategist your summaries are known for their clarity, objectivity, and ability to capture the essence of a story in just a few paragraphs. Your work has been instrumental in helping busy executives, policymakers, and the general public stay informed and up-to-date on the most important developments across various fields.',            
            tools=[self.serper],
            verbose=True,
            allow_delegation=True,
            llm=self.gpt4,
        )

    def writer(self):
        # Detailed agent setup for the Writer
        return Agent(
            role='Newsletter Compiler',
            goal='Compile the analyzed newsletter stories into a final newsletter format',
            backstory='You are the final architect of the newsletter. Its your job to create a coherent and visually appealing newsletter that capivates our readers and remains consitant throughout'
            verbose=True,
            llm=self.gpt4,
        )
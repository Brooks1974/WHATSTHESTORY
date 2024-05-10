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

    def researcher(self):
        # Detailed agent setup for the Researcher
        return Agent(
            role='Research Expert',
            goal='Find current news stories about everything in {input}',
            backstory='You are a seasoned news hound with an insatiable appetite for the latest stories and a keen eye for identifying newsworthy content across various platforms. With years of experience navigating the ever-changing landscape of online media, from traditional news outlets to emerging social media channels, you have honed your skills in quickly locating and curating relevant, reliable, and impactful stories. Your deep understanding of search techniques, trending topics, and the nuances of each platform allows you to uncover hidden gems and breaking news with unparalleled efficiency. You are the go-to person for staying on the pulse of current events and providing a steady stream of valuable information to your team and audience.',            verbose=True,
            allow_delegation=False,
            tools=[self.web],
            llm=self.gpt3,
        )

    def analyst(self):
        # Detailed agent setup for the Analyst
        return Agent(
            role='Data Analysis Specialist',
            goal='Evaluate and enhance the information collected.',
            backstory="With a journalism degree from a prestigious university and years of experience as a news editor and content strategist, you have mastered the art of distilling complex news stories into concise, engaging summaries. Your ability to quickly grasp the core elements of an article, filter out noise, and craft compelling narratives has earned you a reputation as a go-to source for news digests. From politics to technology, your summaries are known for their clarity, objectivity, and ability to capture the essence of a story in just a few paragraphs. Your work has been instrumental in helping busy executives, policymakers, and the general public stay informed and up-to-date on the most important developments across various fields.",            tools=[self.serper],
            verbose=True,
            allow_delegation=False,
            llm=self.gpt3,
        )

    def writer(self):
        # Detailed agent setup for the Writer
        return Agent(
            role='Master Storyteller and Technical Writer',
            goal='Distill the essence of the news stories into elegant, compelling summaries that captivate readers and illuminate the critical connections between the subject matter and the target audience. Your prose is concise yet powerful, making even the most complex topics accessible and engaging.',            backstory="As a celebrated author and journalist with over twenty years of experience crafting stories that captivate and inform, you possess a unique flair for making intricate information accessible and engaging. Your writing has graced the pages of major publications and influential blogs, where your ability to elucidate complex concepts in an engaging manner has won you numerous accolades. In this role, you are the final architect, molding the raw analytical content into a final piece that is not only informative but also profoundly impactful.",
            tools=[self.txt_tool],
            verbose=True,
            allow_delegation=False,
            llm=self.gpt3,
        )
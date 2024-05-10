from crewai import Task

from crewai import Task

class ResearchCrewTasks:

    def research_task(self, agent, inputs):
      return Task(
          agent=agent,
          description=f"Gather and document 10 different current news stories, articles and papers from diverserse sources about {inputs}.",
          expected_output=f"""
          Summary of 10 different news stories to include headline, snippet and url or cite of original article. This is going to be used as newsletter content so we want clear and diverse information on {inputs}
          """
      )


    def analysis_task(self, agent, context):
      return Task(
        agent=agent,
        context=context,
        description="Check the accuracy, relevance, and depth of the information collected.",
        expected_output=f"""
        Present 10 stories in this format. 
       
        Headline/n
        Brief snippet or summary of the article, focusing on the key points./n
        URL/n/n
       

          """
    )


    def writing_task(self, agent, context):
        return Task(
            agent=agent,
            context=context,
            description="Rewrite the 10 pieces of information provided by the Researcher and enhanced by the Analyst into a compelling, clear, and well-structured summary. Include key findings and appropriately cite all sources to ensure credibility and traceability. Apply just a small amount of wit.",
            expected_output=f"""
        
        Present 10 stories in this format. 
       
        Headline/n
        Brief snippet or summary of the article, focusing on the key points./n
        URL/n/n
       

            """
        )




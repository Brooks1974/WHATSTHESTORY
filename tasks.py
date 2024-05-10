from crewai import Task

from crewai import Task

class ResearchCrewTasks:

    def research_task(self, agent, inputs):
      return Task(
          agent=agent,
          description=f"Gather and document 10 different current news stories from diverserse sources about everything in {inputs}.",
          expected_output=f"""
          Summary of 10 different news stories to include headline, snippet and url or cite of original article. The stories must be relevant to everything in {inputs}
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
            description="In needed Rewrite the 10 pieces of information into a compelling, clear, and well-structured summary. Apply just a small amount of wit.",
            expected_output=f"""
        
        Present 10 stories in this format. 
       
        Headline/n
        Brief snippet or summary of the article, focusing on the key points./n
        URL/n/n
       

            """
        )




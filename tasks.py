from crewai import Task

from crewai import Task

class ResearchCrewTasks:

    def research_task(self, agent, inputs):
      return Task(
          agent=agent,
          description=f"Systematically gather and document current and relevant news and articles from diverse sources about {inputs}. Use all available digital tools to ensure comprehensive coverage.",
          expected_output=f"""
  Detailed Research Report on {inputs}
          """
      )


    def analysis_task(self, agent, context):
      return Task(
        agent=agent,
        context=context,
        description="Critically assess the accuracy, relevance, and depth of the information collected. Employ advanced data analysis methodologies to enhance the information's value, ensuring it meets the high standards required for expert assessment.",
        expected_output=f"""
        Break each story up like this. 
        ###
        Title/Headline 1
        Brief snippet or summary of the article, focusing on the key points.
        URL: Insert the URL of the original article or cite here
        ###
          """
    )


    def writing_task(self, agent, context):
        return Task(
            agent=agent,
            context=context,
            description="Synthesize the information provided by the Researcher and enhanced by the Analyst into a compelling, clear, and well-structured summary. Include key findings and appropriately cite all sources to ensure credibility and traceability.",
            expected_output=f"""
        Output as this
        ###
        Title/Headline 1
        Brief snippet or summary of the article, focusing on the key points.
        URL: Insert the URL of the original article or cite here
        ###
            """
        )




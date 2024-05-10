from crewai import Task

from crewai import Task

class ResearchCrewTasks:

    def research_task(self, agent, inputs):
      input_lines = inputs.split("\n")
      subject = input_lines[0].split(":")[1].strip()
      customer = input_lines[1].split(":")[1].strip()
      additional_info = input_lines[2].split(":")[1].strip()
      return Task(
          agent=agent,
          description=f"Systematically gather and document current and relevant news and articles from diverse sources about {inputs}. Use all available digital tools to ensure comprehensive coverage.",
          expected_output=f"""
  Detailed Research Report on {inputs}
        ###
        Title/Headline 1
        Brief snippet or summary of the article, focusing on the key points related to {subject} and {customer}.
        URL: [Insert the URL of the original article here]
        ###
        
        [Repeat the above format for approximately 25 stories]
          """
      )


    def analysis_task(self, agent, context):
      return Task(
        agent=agent,
        context=context,
        description="Critically assess the accuracy, relevance, and depth of the information collected. Make sure each story is relevant to all {inputs}. Employ advanced data analysis methodologies to enhance the information's value, ensuring it meets the high standards required for expert assessment. Return the top 10 stories. ",
        expected_output=f"""
        ###
        Title/Headline 1
        Brief snippet or summary of the article, focusing on the key points related to {subject} and {customer}.
        URL: [Insert the URL of the original article here]
        ###
        
        [Repeat the above format for approximately 10 stories]
          """
    )


    def writing_task(self, agent, context):
        return Task(
            agent=agent,
            context=context,
            description="Synthesize the information provided by the Researcher and enhanced by the Analyst into a compelling, clear, and well-structured summary. Include key findings and appropriately cite all sources to ensure credibility and traceability.",
            expected_output=f"""
        ###
        Title/Headline 1
        Brief snippet or summary of the article, focusing on the key points related to {subject} and {customer}.
        URL: [Insert the URL of the original article here]
        ###
        
            """
        )





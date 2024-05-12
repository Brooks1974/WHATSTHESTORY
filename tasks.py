from crewai import Task
from datetime import datetime

class ResearchCrewTasks:

    def research_task(self, agent, inputs):
      return Task(
          description=f"Fetch the top news stories about from the past 48 hours about {inputs}. Current time is {datetime.now()}",
          agent=agent,
          async_execution=True,
          expected_output=f"""A list with story titles, URLS and a brief summary for each
          Example output:
          [
            { 'title': 'Headline',
             'url': 'https://example.com/story1',
             'summary': 'SUMMARY GOES HERE'
            },
            {{...}}
            ]
          """
      )


    def analysis_task(self, agent, context):
      return Task(
        agent=agent,
        context=context,
        async_execution=True,
        description="Analyze the news story and enure there are at least 5 well-fomatted articles",
        expected_output=f""" A formatted analysis of each newsstory; includes a headline, rundown, details and why it matters section. Include the full url to the original story.
        Present 5 stories in this format. 
       
        Example output:
        ** HEADLINE
        ** The Rundown:
        ** The Details:
        ** Why it matters: 
        ** Original URL: 

          """
    )


    def writing_task(self, agent, context, callback_function):
        return Task(
            agent=agent,
            context=context,
            description="A complete newsletter in markdown format with a consistent style and layout.",
            expected_output=f"""
        
        Present each of the 5 stories in this format. 
       
        Example output:
        ** HEADLINE
        ** The Rundown:
        ** The Details:
        ** Why it matters: 
        ** Original URL: 
       

            """,
        callback=callback_function    
        )




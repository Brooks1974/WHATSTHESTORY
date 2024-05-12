import os
from decouple import config
from crewai import Crew, Process
from textwrap import dedent
from agents import ResearchCrewAgents
from tasks import ResearchCrewTasks



class ResearchCrew:
    def __init__(self, inputs):
        self.inputs = inputs
        self.agents = ResearchCrewAgents()
        self.tasks = ResearchCrewTasks()

    def run(self):
        # Initialize agents
        researcher = self.agents.researcher()
        analyst = self.agents.analyst()
        writer = self.agents.writer()

        # Initialize tasks with respective agents
        research_task = self.tasks.research_task(researcher, self.inputs)
        analysis_task = self.tasks.analysis_task(analyst, [research_task])
        writing_task = self.tasks.writing_task(writer, [analysis_task])

        # Form the crew with defined agents and tasks
        crew = Crew(
            agents=[researcher, analyst, writer],
            tasks=[research_task, analysis_task, writing_task],
            process=Process.sequential
        )

        # Execute the crew to carry out the research project
        return crew.kickoff()

if __name__ == "__main__":
    print("Welcome to the Research Crew Setup")
    print("---------------------------------------")
    subject = input("What is the subject?")
    customer = input("Who's the customer or segment?")
    additional_info = input("Additional information")

    inputs = f"Main subject: {subject}\nThe Customer: {customer}\nMore Information: {additional_info}"
    subject = f"Subject {subject}"
    customer = f"Subject {customer}"
    additional_info = f"Subject {additional_info}"
    research_crew = ResearchCrew(inputs)
    result = research_crew.run()

    print("\n\n##############################")
    print("## Here are the results:")
    print("##############################\n")
    print(result)

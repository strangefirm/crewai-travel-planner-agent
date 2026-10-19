
from importlib import import_module
from dotenv import load_dotenv
load_dotenv()  # load environment variables from .env file

crewai = import_module("crewai")
Agent, Task, Crew = crewai.Agent, crewai.Task, crewai.Crew
city = input("Which city? ")
planner = Agent(role="Travel Planner", goal="Plan a trip to a given city", backstory="You are a seasoned travel planner with extensive knowledge of various cities around the world.", verbose=True)
task = Task(description=f"Plan a trip to {city}",
 expected_output="A detailed travel plan for the specified city.", agent=planner)
crew = Crew(agents=[planner], tasks=[task])
print(crew.kickoff(inputs={"city": city}))
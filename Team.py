from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.team import Team

load_dotenv()

english_agent = Agent(
    name="English Agent",
    role="Give answer and traslate in english language"
)

hindi_agent = Agent(
    name="hindi Agent",
    role="Give answer and traslate in hindi language"
)

gujarati_agent = Agent(
    name="gujrati Agent",
    role="Give answer and traslate in hindi language"
)

team_leader = Team(
    name="Translate Agent",
    members=[english_agent,hindi_agent,gujarati_agent],
    model=Groq(id="qwen/qwen3-32b"),
    markdown=True,
    show_members_responses=True,
    instructions=""" all member agents must answer to the query to thier specific language.
                    do not route to just one agent.
                    output the response of all agents.
    """,
)


team_leader.print_response("what is the capital of india")
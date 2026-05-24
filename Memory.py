from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint

load_dotenv()

db=SqliteDb(db_file="tmp/memory.db")
db.clear_memories()

def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"),
        markdown=True,
        db = db,
        add_history_to_context=True,
        enable_user_memories=True
    )

groq_agent = build_agent()

user_id = "ronaksinhrajput160805@gmail.com"

groq_agent.print_response("my name is Ronaksinh Rajput, i am data analyts",user_id=user_id)
groq_agent.print_response("who amm i?",user_id=user_id)

memories = groq_agent.get_user_memories(
    user_id=user_id
)
print("Memories")
pprint(memories)

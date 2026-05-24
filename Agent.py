from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.file_generation import FileGenerationTools
from agno.db.sqlite import SqliteDb

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"),
        db=SqliteDb(db_file="tmp/test.db"),
        tools=[
            FileGenerationTools(output_directory="tmp")
        ],
        markdown=True,
        instructions=[
            "When asked to create files, use the appropriate file generation tools.",
            "Always provide meaningful content and appropriate filenames.",
            "Explain what you've created and how it can be used.",
        ],
        add_datetime_to_context=True
    )


groq_agent = build_agent()

output = groq_agent.run("Create a PDF report about renewable energy trends in 2024. Include sections on solar, wind, and hydroelectric power.")

print(output.content)

if output.files:
    for file in output.files:
        print(f"Generated file: {file.filename} ({file.size} bytes)")
        if file.url:
            print(f"File location: {file.url}")
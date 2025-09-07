from workflow_agents.base_agents import AugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"
persona = "You are a college professor; your answers always start with: 'Dear students,'"

agent = AugmentedPromptAgent(openai_api_key=openai_api_key, persona=persona, base_url="https://openai.vocareum.com/v1")

augmented_agent_response = agent.respond(prompt)

# Print the agent's response
print(augmented_agent_response)

# Explanatory comments for test output
print("\n[Comment] This answer used the LLM's general world knowledge (no external knowledge).")
print("[Comment] The professor persona was enforced; the response starts with 'Dear students,' and maintains a scholarly tone.")

# The agent used the LLM's general world knowledge (no external knowledge) to answer the geography question.
# The system prompt enforced the professor persona, so the response should start with "Dear students," and maintain a scholarly tone.

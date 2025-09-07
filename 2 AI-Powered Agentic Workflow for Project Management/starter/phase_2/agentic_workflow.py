# agentic_workflow.py

import os
import sys
from dotenv import load_dotenv

# Ensure Phase 1 package is importable when running this script directly
CURRENT_DIR = os.path.dirname(__file__)
PHASE_1_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "phase_1"))
if PHASE_1_DIR not in sys.path:
    sys.path.insert(0, PHASE_1_DIR)

from workflow_agents.base_agents import (
    ActionPlanningAgent,
    KnowledgeAugmentedPromptAgent,
    EvaluationAgent,
    RoutingAgent,
)

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# load the product spec
with open(os.path.join(os.path.dirname(__file__), "Product-Spec-Email-Router.txt"), "r", encoding="utf-8") as f:
    product_spec = f.read()

# Instantiate all the agents

# Action Planning Agent
knowledge_action_planning = (
    "You will always extract exactly these three steps in order, as short imperative sentences: \n"
    "1) Generate user stories for the product spec. \n"
    "2) Generate product features by grouping related stories. \n"
    "3) Generate engineering tasks for the product based on the stories. \n\n"
    "Guidance: \n"
    "- Stories are defined from a product spec by identifying a persona, an action, and a desired outcome. \n"
    "- Features are defined by grouping related user stories. \n"
    "- Tasks are defined for each story and represent the engineering work required to develop the product. \n"
    "Return only the three step sentences above, nothing else."
)
action_planning_agent = ActionPlanningAgent(openai_api_key=openai_api_key, knowledge=knowledge_action_planning, base_url="https://openai.vocareum.com/v1")

# Product Manager - Knowledge Augmented Prompt Agent
persona_product_manager = "You are a Product Manager, you are responsible for defining the user stories for a product."
knowledge_product_manager = (
    "Stories are defined by writing sentences with a persona, an action, and a desired outcome. "
    "The sentences always start with: As a "
    "Write several stories for the product spec below, where the personas are the different users of the product. "
    "\n\nProduct specification follows:\n" + product_spec
)
product_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key=openai_api_key,
    persona=persona_product_manager,
    knowledge=knowledge_product_manager,
    base_url="https://openai.vocareum.com/v1"
)

# Product Manager - Evaluation Agent
persona_product_manager_eval = "You are an evaluation agent that checks the answers of other worker agents."
criteria_stories = (
    "User stories must follow: As a [type of user], I want [an action or feature] so that [benefit/value]."
)
product_manager_evaluation_agent = EvaluationAgent(
    openai_api_key=openai_api_key,
    persona=persona_product_manager_eval,
    evaluation_criteria=criteria_stories,
    worker_agent=product_manager_knowledge_agent,
    max_interactions=5,
    base_url="https://openai.vocareum.com/v1"
)

# Program Manager - Knowledge Augmented Prompt Agent
persona_program_manager = "You are a Program Manager, you are responsible for defining the features for a product."
knowledge_program_manager = "Features of a product are defined by organizing similar user stories into cohesive groups."
program_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key=openai_api_key,
    persona=persona_program_manager,
    knowledge=knowledge_program_manager,
    base_url="https://openai.vocareum.com/v1"
)

# Program Manager - Evaluation Agent
persona_program_manager_eval = "You are an evaluation agent that checks the answers of other worker agents."

program_manager_evaluation_agent = EvaluationAgent(
    openai_api_key=openai_api_key,
    persona=persona_program_manager_eval,
    evaluation_criteria=(
        "The answer should be product features that follow the following structure: "
        "Feature Name: A clear, concise title that identifies the capability\n"
        "Description: A brief explanation of what the feature does and its purpose\n"
        "Key Functionality: The specific capabilities or actions the feature provides\n"
        "User Benefit: How this feature creates value for the user"
    ),
    worker_agent=program_manager_knowledge_agent,
    max_interactions=5,
    base_url="https://openai.vocareum.com/v1"
)
#                      "The answer should be product features that follow the following structure: " \
#                      "Feature Name: A clear, concise title that identifies the capability\n" \
#                      "Description: A brief explanation of what the feature does and its purpose\n" \
#                      "Key Functionality: The specific capabilities or actions the feature provides\n" \
#                      "User Benefit: How this feature creates value for the user"
# For the 'agent_to_evaluate' parameter, refer to the provided solution code's pattern.

# Development Engineer - Knowledge Augmented Prompt Agent
persona_dev_engineer = "You are a Development Engineer, you are responsible for defining the development tasks for a product."
knowledge_dev_engineer = "Development tasks are defined by identifying what needs to be built to implement each user story."
development_engineer_knowledge_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key=openai_api_key,
    persona=persona_dev_engineer,
    knowledge=knowledge_dev_engineer,
    base_url="https://openai.vocareum.com/v1"
)

# Development Engineer - Evaluation Agent
persona_dev_engineer_eval = "You are an evaluation agent that checks the answers of other worker agents."
development_engineer_evaluation_agent = EvaluationAgent(
    openai_api_key=openai_api_key,
    persona=persona_dev_engineer_eval,
    evaluation_criteria=(
        "The answer should be tasks following this exact structure: "
        "Task ID: A unique identifier for tracking purposes\n"
        "Task Title: Brief description of the specific development work\n"
        "Related User Story: Reference to the parent user story\n"
        "Description: Detailed explanation of the technical work required\n"
        "Acceptance Criteria: Specific requirements that must be met for completion\n"
        "Estimated Effort: Time or complexity estimation\n"
        "Dependencies: Any tasks that must be completed first"
    ),
    worker_agent=development_engineer_knowledge_agent,
    max_interactions=5,
    base_url="https://openai.vocareum.com/v1"
)
#                      "The answer should be tasks following this exact structure: " \
#                      "Task ID: A unique identifier for tracking purposes\n" \
#                      "Task Title: Brief description of the specific development work\n" \
#                      "Related User Story: Reference to the parent user story\n" \
#                      "Description: Detailed explanation of the technical work required\n" \
#                      "Acceptance Criteria: Specific requirements that must be met for completion\n" \
#                      "Estimated Effort: Time or complexity estimation\n" \
#                      "Dependencies: Any tasks that must be completed first"
# For the 'agent_to_evaluate' parameter, refer to the provided solution code's pattern.


# Routing Agent
routing_agent = RoutingAgent(openai_api_key=openai_api_key, agents=[], base_url="https://openai.vocareum.com/v1")

# Job function persona support functions
def product_manager_support_function(step: str):
    result = product_manager_evaluation_agent.evaluate(step)
    return result


def program_manager_support_function(step: str):
    result = program_manager_evaluation_agent.evaluate(step)
    return result


def development_engineer_support_function(step: str):
    result = development_engineer_evaluation_agent.evaluate(step)
    return result


routing_agent.agents = [
    {
        "name": "Product Manager",
        "description": "Define user stories for a product specification and requests about stories",
        "func": product_manager_support_function,
    },
    {
        "name": "Program Manager",
        "description": "Define product features by grouping related stories and requests about features",
        "func": program_manager_support_function,
    },
    {
        "name": "Development Engineer",
        "description": "Generate engineering tasks for product development with Task ID, Title, Related User Story, Description, Acceptance Criteria, Estimated Effort, and Dependencies",
        "func": development_engineer_support_function,
    },
]

# Run the workflow

print("\n*** Workflow execution started ***\n")
# Workflow Prompt
# ****
workflow_prompt = (
    "Create a complete development plan for this product."
)
# ****
print(f"Task to complete in this workflow, workflow prompt = {workflow_prompt}")

print("\nDefining workflow steps from the workflow prompt")
steps = action_planning_agent.extract_steps_from_prompt(workflow_prompt)
print(f"Extracted steps: {steps}")

completed_steps = []
for idx, step in enumerate(steps, start=1):
    print(f"\nExecuting step {idx}/{len(steps)}: {step}")
    result = routing_agent.route(step)
    completed_steps.append({"step": step, "result": result})
    print(f"Result for step {idx}: {result}\n")

if completed_steps:
    print("\nFinal workflow output:")
    print(completed_steps[-1])
else:
    print("No steps were extracted.")
# AgenticAI: Advanced AI Agent Projects Portfolio

This repository showcases a comprehensive collection of AI agent projects demonstrating advanced techniques in **Prompting for Effective LLM Reasoning and Planning**, **Agentic Workflows**, and **Building Agents and Multi-Agent Systems**. Each project explores different aspects of AI agent development, from basic prompt engineering to complex multi-agent orchestration.

## 🎯 Project Overview

This portfolio contains four distinct projects that progressively build expertise in AI agent development:

1. **AgentsVille Trip Planner** - Multi-agent travel planning with advanced reasoning
2. **AI-Powered Agentic Workflow for Project Management** - Reusable agent library and workflow orchestration
3. **UdaPlay - AI Research Agent for Video Game Industry** - RAG-based knowledge agent with web search
4. **Munder Difflin Multi-Agent System** - Business process automation with specialized agents

---

## 🚀 Project 1: AgentsVille Trip Planner - Multi-Agent Travel Assistant

### **Project Description:**
The AgentsVille Trip Planner is a sophisticated AI-powered travel planning system that demonstrates advanced multi-agent coordination and reasoning techniques. This project simulates a real-world travel planning scenario where multiple specialized AI agents work together to create personalized, detailed travel itineraries for the fictional city of AgentsVille.

The system showcases how AI agents can handle complex, multi-step planning tasks that require external data integration, constraint satisfaction, and iterative improvement. It processes traveler preferences, weather conditions, budget constraints, and available activities to generate comprehensive travel plans that can be refined through feedback loops.

**Real-World Application**: This system could be adapted for actual travel planning platforms, event scheduling, or any scenario requiring complex multi-constraint optimization with human feedback integration.

### **Focus Areas:**
- **Prompting for Effective LLM Reasoning and Planning**
- **Chain-of-Thought Reasoning**
- **ReAct Prompting (Thought → Action → Observation)**
- **Feedback Loops and Self-Evaluation**

### **Key Features:**

#### 🧠 Advanced AI Techniques
- **Role-Based Prompting**: Specialized agents with specific travel planning roles
- **Chain-of-Thought Reasoning**: Step-by-step itinerary planning process
- **ReAct Prompting**: Iterative improvement through Thought → Action → Observation cycles
- **Feedback Loops**: Self-evaluation using tools to identify and fix planning mistakes

#### 🤖 Multi-Agent Architecture
- **ItineraryAgent**: Creates initial day-by-day travel plans
- **ItineraryRevisionAgent**: Refines plans based on feedback and evaluation results
- **Evaluation System**: Comprehensive validation of itinerary quality

#### 📊 Smart Data Integration
- **Weather API Integration**: Real-time weather data for activity compatibility
- **Activity Database**: Comprehensive activity listings with pricing and details
- **Dynamic Tool System**: Calculator, activity retrieval, and evaluation tools

### **Technical Implementation:**
- **Pydantic Models**: Structured data validation for vacation info and travel plans
- **Tool System**: Four specialized tools for calculations, data retrieval, evaluation, and output
- **Evaluation Functions**: Multi-criteria validation including date matching, budget accuracy, and weather compatibility
- **Feedback Integration**: User feedback incorporation with constraint validation

### **Learning Outcomes:**
- Advanced prompt engineering techniques
- Multi-agent system design patterns
- LLM reasoning and evaluation methodologies
- Structured data validation and API integration
- Feedback loop implementation for iterative improvement

---

## 🏗️ Project 2: AI-Powered Agentic Workflow for Project Management

### **Project Description:**
The AI-Powered Agentic Workflow for Project Management is a comprehensive two-phase project that demonstrates how to build reusable AI agent libraries and orchestrate them into sophisticated workflow systems. This project addresses real-world challenges faced by technical project managers at scaling companies who need consistent, high-quality project planning and execution.

The first phase focuses on creating a library of seven specialized, reusable AI agents that can be deployed across various workflow scenarios. The second phase demonstrates how to orchestrate these agents into a complete project management workflow that transforms high-level product specifications into detailed user stories, product features, and engineering tasks.

**Real-World Application**: This system could be deployed in software companies, consulting firms, or any organization that needs to systematically break down complex projects into actionable development plans with consistent quality and structure.

### **Focus Areas:**
- **Building Reusable Agent Libraries**
- **Agentic Workflow Orchestration**
- **Multi-Agent System Design**
- **Knowledge-Augmented Prompting**

### **Phase 1: Agent Library Development**

#### **Seven Specialized Agent Classes:**

1. **DirectPromptAgent**: Basic LLM interaction without additional context
2. **AugmentedPromptAgent**: Persona-based prompting for specialized responses
3. **KnowledgeAugmentedPromptAgent**: Context-aware responses using provided knowledge
4. **RAGKnowledgePromptAgent**: Retrieval-augmented generation for dynamic knowledge sourcing
5. **EvaluationAgent**: Iterative response evaluation and refinement
6. **RoutingAgent**: Semantic routing to appropriate specialized agents
7. **ActionPlanningAgent**: Dynamic task decomposition and step extraction

#### **Technical Features:**
- **Embedding-Based Routing**: Cosine similarity for intelligent agent selection
- **Iterative Evaluation**: Multi-round feedback loops for response refinement
- **Knowledge Integration**: Context-aware responses using domain-specific knowledge
- **Modular Design**: Reusable components for various workflow applications

### **Phase 2: Project Management Workflow**

#### **Workflow Architecture:**
- **Action Planning**: Dynamic task breakdown using specialized knowledge
- **Intelligent Routing**: Semantic assignment of tasks to appropriate agent teams
- **Multi-Team Simulation**: Product Manager, Program Manager, and Development Engineer teams
- **Structured Output**: Comprehensive project plans with user stories, features, and engineering tasks

#### **Agent Teams:**
- **Product Manager Team**: User story generation with evaluation criteria validation
- **Program Manager Team**: Feature definition with detailed specifications
- **Development Engineer Team**: Technical task creation with acceptance criteria

### **Learning Outcomes:**
- Reusable agent library design patterns
- Workflow orchestration and coordination
- Knowledge-augmented prompting techniques
- Multi-agent system architecture
- Domain-specific agent specialization

---

## 🎮 Project 3: UdaPlay - AI Research Agent for Video Game Industry

### **Project Description:**
UdaPlay is an intelligent AI research agent specifically designed for the video game industry, demonstrating advanced techniques in Retrieval-Augmented Generation (RAG) and hybrid knowledge systems. This project showcases how to build AI agents that can seamlessly combine local knowledge bases with real-time web search capabilities to provide comprehensive, accurate information about video games.

The project is structured in two parts: first, building a robust offline RAG system using vector databases to store and retrieve game information efficiently, and second, creating an intelligent agent that can dynamically decide when to use local knowledge versus web search to answer complex questions about video games.

**Real-World Application**: This system could be adapted for any domain requiring research assistance, such as academic research, market analysis, technical documentation, or customer support systems that need both historical knowledge and real-time information.

### **Focus Areas:**
- **Retrieval-Augmented Generation (RAG)**
- **Vector Database Integration**
- **Web Search Integration**
- **Conversation State Management**

### **Part 1: Offline RAG System**

#### **Vector Database Implementation:**
- **ChromaDB Integration**: Persistent vector storage for game information
- **Embedding Functions**: Text-to-vector conversion for semantic search
- **Document Processing**: JSON game data indexing and retrieval
- **Collection Management**: Organized storage of 15+ game documents

#### **Data Structure:**
- Game metadata (name, platform, genre, publisher, year)
- Rich descriptions for semantic search
- Structured JSON format for easy processing

### **Part 2: AI Agent Development**

#### **Agent Capabilities:**
1. **Local Knowledge Retrieval**: RAG-based game information access
2. **Web Search Integration**: Tavily API for real-time information
3. **Conversation State**: Context-aware multi-turn interactions
4. **Structured Outputs**: Consistent response formatting
5. **Knowledge Storage**: Learning from interactions for future use

#### **Tool Implementation:**
- **`retrieve_game`**: Vector database search for game information
- **`evaluate_retrieval`**: Quality assessment of retrieved results
- **`game_web_search`**: Web search for additional information

### **Technical Features:**
- **Hybrid Knowledge System**: Combines local RAG with web search
- **Intelligent Retrieval**: Semantic search with quality evaluation
- **State Management**: Conversation context preservation
- **Error Handling**: Robust failure management and recovery

### **Learning Outcomes:**
- RAG system implementation and optimization
- Vector database design and management
- Web search integration in AI agents
- Conversation state management
- Hybrid knowledge system architecture

---

## 🏢 Project 4: Munder Difflin Multi-Agent System

### **Project Description:**
The Munder Difflin Multi-Agent System is a comprehensive business process automation solution designed for a fictional paper manufacturing company. This project demonstrates how to build enterprise-level multi-agent systems that can handle complex business workflows including inventory management, quote generation, order processing, and supply chain coordination.

The system showcases real-world business automation scenarios where multiple specialized agents work together to process customer requests, manage inventory, generate quotes with bulk discounts, process orders, and coordinate with suppliers for restocking. It demonstrates how AI agents can be integrated into existing business systems to automate complex, multi-step processes that traditionally require human intervention.

**Real-World Application**: This system could be adapted for any manufacturing, retail, or service company that needs to automate customer request processing, inventory management, pricing, and order fulfillment workflows.

### **Focus Areas:**
- **Business Process Automation**
- **Multi-Agent Orchestration**
- **Tool-Based Agent Architecture**
- **Real-Time Data Integration**

### **System Architecture:**

#### **Four Specialized Agents:**
1. **Inventory Manager**: Real-time stock level tracking and management
2. **Quote Specialist**: Automated pricing with bulk discount calculations
3. **Order Processor**: Transaction management and inventory updates
4. **Restocking Coordinator**: Supplier delivery planning and coordination

#### **Business Functions:**
- **Inventory Management**: Real-time stock level tracking and restocking decisions
- **Quote Generation**: Automated pricing with tiered bulk discounts (5%, 10%, 15%)
- **Order Processing**: Complete transaction management and inventory updates
- **Financial Tracking**: Cash flow monitoring and transaction logging

### **Technical Implementation:**

#### **Tool-Based Architecture:**
- **8 Specialized Tools**: Business operation-specific functions
- **Database Integration**: SQLite with SQLAlchemy ORM
- **Real-Time Processing**: Live data access for decision making
- **Error Handling**: Comprehensive validation and failure management

#### **Smart Features:**
- **Item Name Mapping**: Handles 50+ paper product variations
- **Historical Learning**: Uses past quote data for pricing guidance
- **Bulk Discount System**: Tiered pricing based on order value
- **Financial Reporting**: Comprehensive business insights and analytics

### **Agent Tools:**
- **Inventory Tools**: `check_inventory_tool`, `get_all_inventory_tool`, `check_cash_balance_tool`
- **Quote Tools**: `search_quote_history_tool`, `calculate_quote_tool`
- **Order Tools**: `process_order_tool`, `get_supplier_delivery_info_tool`

### **Learning Outcomes:**
- Business process automation with AI agents
- Multi-agent orchestration and coordination
- Tool-based agent architecture design
- Real-time data integration and processing
- Enterprise-level system design patterns

---

## 🎓 Key Learning Outcomes Across All Projects

### **Prompting for Effective LLM Reasoning and Planning:**
- **Chain-of-Thought Reasoning**: Step-by-step problem decomposition
- **Role-Based Prompting**: Specialized agent personas and contexts
- **ReAct Prompting**: Iterative improvement through action-observation cycles
- **Knowledge-Augmented Prompting**: Context-aware responses using domain knowledge
- **Evaluation and Feedback Loops**: Self-improvement through iterative refinement

### **Agentic Workflows:**
- **Workflow Orchestration**: Coordinating multiple agents for complex tasks
- **Dynamic Task Routing**: Intelligent assignment based on semantic similarity
- **Multi-Step Processing**: Breaking down complex problems into manageable steps
- **State Management**: Maintaining context across workflow stages
- **Error Handling and Recovery**: Robust failure management in agent systems

### **Building Agents and Multi-Agent Systems:**
- **Agent Specialization**: Creating focused agents for specific domains
- **Tool Integration**: Equipping agents with specialized capabilities
- **Communication Patterns**: Agent-to-agent interaction and coordination
- **System Architecture**: Designing scalable multi-agent systems
- **Testing and Validation**: Comprehensive testing frameworks for agent systems

---

## 🛠️ Technical Stack

### **Core Technologies:**
- **Python 3.8+**: Primary development language
- **OpenAI GPT Models**: LLM integration for agent reasoning
- **Pydantic**: Data validation and structured outputs
- **SQLAlchemy**: Database ORM for data persistence
- **ChromaDB**: Vector database for RAG implementations
- **Pandas**: Data processing and analysis

### **Agent Frameworks:**
- **smolagents**: Multi-agent orchestration framework
- **Custom Agent Classes**: Specialized agent implementations
- **Tool Systems**: Function-based agent capabilities

### **External Integrations:**
- **Weather APIs**: Real-time weather data integration
- **Web Search APIs**: Tavily integration for real-time information
- **Vector Databases**: ChromaDB for semantic search
- **Database Systems**: SQLite for persistent storage

---

## 📁 Repository Structure

```
AgenticAI/
├── 1 AgentsVille Trip Planner - Project Assignment/
│   ├── project_starter.ipynb          # Main implementation notebook
│   ├── project_lib.py                 # Supporting library functions
│   └── README.md                      # Detailed project documentation
├── 2 AI-Powered Agentic Workflow for Project Management/
│   ├── starter/
│   │   ├── phase_1/                   # Agent library development
│   │   │   ├── workflow_agents/       # Reusable agent classes
│   │   │   └── *_agent.py            # Individual agent test scripts
│   │   └── phase_2/                   # Workflow orchestration
│   │       └── agentic_workflow.py   # Main workflow implementation
│   └── project_overview.md            # Project requirements and goals
├── 3 UdaPlay - An AI Research Agent for the Video Game Industry/
│   ├── starter/
│   │   ├── lib/                       # Custom library implementations
│   │   ├── games/                     # Game data JSON files
│   │   ├── Udaplay_01_starter_project.ipynb  # RAG implementation
│   │   └── Udaplay_02_starter_project.ipynb  # Agent development
│   └── README.md                      # Project documentation
└── 4 The Beaver's Choice Paper Company needs your help!/
    ├── project_starter.py             # Multi-agent system implementation
    ├── workflow_diagram.md            # System architecture documentation
    ├── design_notes.txt               # Technical implementation details
    └── IMPLEMENTATION_SUMMARY.md      # Project completion summary
```

---

## 🚀 Getting Started

### **Prerequisites:**
- Python 3.8 or higher
- OpenAI API access
- Jupyter Notebook or JupyterLab (for notebook-based projects)

### **Setup Instructions:**
1. Clone the repository
2. Install required dependencies from individual project requirements files
3. Set up API keys in `.env` files for each project
4. Follow individual project README files for specific setup instructions

### **Running the Projects:**
- **AgentsVille Trip Planner**: Run the Jupyter notebook cells sequentially
- **Agentic Workflow**: Execute Phase 1 agent tests, then Phase 2 workflow
- **UdaPlay**: Complete Part 1 (RAG setup), then Part 2 (agent development)
- **Munder Difflin**: Run the main Python script with proper API configuration

---

## 🎯 Project Impact and Applications

These projects demonstrate practical applications of AI agent technology across various domains:

- **Travel Planning**: Personalized itinerary generation with real-time data integration
- **Project Management**: Automated workflow orchestration for technical teams
- **Research Assistance**: Intelligent information retrieval and synthesis
- **Business Automation**: Multi-agent systems for enterprise process automation

Each project showcases different aspects of AI agent development, from basic prompt engineering to complex multi-agent orchestration, providing a comprehensive foundation for building sophisticated AI systems.

---

## 📚 Additional Resources

- **OpenAI Documentation**: [https://platform.openai.com/docs](https://platform.openai.com/docs)
- **ChromaDB Documentation**: [https://docs.trychroma.com/](https://docs.trychroma.com/)
- **Pydantic Documentation**: [https://docs.pydantic.dev/](https://docs.pydantic.dev/)
- **SQLAlchemy Documentation**: [https://docs.sqlalchemy.org/](https://docs.sqlalchemy.org/)

---

**Built with ❤️ using advanced AI agent techniques and modern Python frameworks.**

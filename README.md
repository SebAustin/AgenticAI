# Multi-Agent Travel Assistant System

A sophisticated AI-powered travel planning system that uses multiple specialized agents to create personalized travel itineraries. The system demonstrates advanced LLM reasoning techniques including role-based prompting, chain-of-thought reasoning, ReAct prompting, and feedback loops.

## 🎯 Project Overview

This system helps plan trips to the wonderful city of AgentsVille! It uses multiple AI agents working together to create detailed, personalized travel itineraries based on traveler preferences, weather conditions, and available activities.

## ✨ Key Features

### 🤖 Multi-Agent Architecture
- **ItineraryAgent**: Creates initial day-by-day travel plans
- **ItineraryRevisionAgent**: Refines plans based on feedback and evaluation results
- **Evaluation System**: Comprehensive validation of itinerary quality

### 🧠 Advanced AI Techniques
- **Role-Based Prompting**: Specialized agents with specific roles
- **Chain-of-Thought Reasoning**: Step-by-step planning process
- **ReAct Prompting**: Thought → Action → Observation cycles
- **Feedback Loops**: Self-evaluation using tools to find and fix mistakes

### 📊 Smart Data Integration
- **Weather API Integration**: Real-time weather data for activity compatibility
- **Activity Database**: Comprehensive activity listings with pricing and details
- **Dynamic Tool System**: Calculator, activity retrieval, and evaluation tools

### 🎨 Personalized Planning
- **Interest Matching**: Activities tailored to traveler interests
- **Budget Management**: Cost calculation and budget compliance
- **Weather Compatibility**: Activities matched to weather conditions
- **Multi-Traveler Support**: Plans for groups with diverse interests

## 🏗️ System Architecture

### Core Components

1. **VacationInfo** (Pydantic Model)
   - Trip duration, destination, budget
   - Traveler details with interests and ages

2. **TravelPlan** (Pydantic Model)
   - Complete itinerary structure
   - Daily activities with recommendations
   - Cost calculations and weather considerations

3. **Evaluation Functions**
   - Date matching validation
   - Budget accuracy checks
   - Interest satisfaction verification
   - Weather compatibility assessment

4. **Tool System**
   - `calculator_tool`: Mathematical calculations
   - `get_activities_by_date_tool`: Activity retrieval
   - `run_evals_tool`: Evaluation execution
   - `final_answer_tool`: Structured output

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- OpenAI API access (or Vocareum API endpoint)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "A Multi-Agent Travel Assistant System"
   ```

2. **Install required packages**
   ```bash
   pip install -q json-repair==0.47.1 numexpr==2.11.0 openai==1.74.0 pandas==2.3.0 pydantic==2.11.7 python-dotenv==1.1.0
   ```

3. **Configure API access**
   - For Vocareum API: Update the `api_key` in the notebook
   - For OpenAI API: Set your `OPENAI_API_KEY` environment variable

4. **Launch Jupyter**
   ```bash
   jupyter notebook project_starter.ipynb
   ```

## 📖 Usage Guide

### 1. Define Vacation Details
```python
vacation_info = VacationInfo(
    destination="AgentsVille",
    date_of_arrival=datetime.date(2025, 6, 10),
    date_of_departure=datetime.date(2025, 6, 12),
    budget=130,
    travelers=[
        Traveler(name="Yuri", age=30, interests=[tennis, cooking, comedy, technology]),
        Traveler(name="Hiro", age=25, interests=[reading, music, theatre, art])
    ]
)
```

### 2. Review Weather and Activities
The system automatically fetches:
- Weather data for all trip dates
- Available activities with pricing and details
- Activity-interest matching

### 3. Generate Initial Itinerary
The ItineraryAgent creates a comprehensive travel plan considering:
- Traveler interests and preferences
- Weather conditions
- Budget constraints
- Available activities

### 4. Evaluate and Refine
The system evaluates the itinerary using multiple criteria:
- Date and location accuracy
- Budget compliance
- Interest satisfaction
- Weather compatibility

### 5. Incorporate Feedback
The ItineraryRevisionAgent refines the plan based on:
- Traveler feedback (e.g., "at least 2 activities per day")
- Evaluation results
- Additional constraints

## 🔧 Configuration

### API Configuration
```python
# For Vocareum API
client = OpenAI(
    base_url="https://openai.vocareum.com/v1",
    api_key="your-vocareum-api-key"
)

# For OpenAI API
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
```

### Model Configuration
```python
model = "gpt-4"  # or your preferred model
```

## 📊 Data Models

### VacationInfo
```python
class VacationInfo(BaseModel):
    destination: str
    date_of_arrival: datetime.date
    date_of_departure: datetime.date
    budget: int
    travelers: list[Traveler]
```

### TravelPlan
```python
class TravelPlan(BaseModel):
    city: str
    start_date: str
    end_date: str
    total_cost: float
    itinerary_days: list[ItineraryDay]
```

### Interest Enum
```python
class Interest(str, Enum):
    ART = "art"
    COOKING = "cooking"
    COMEDY = "comedy"
    # ... and more interests
```

## 🧪 Evaluation Criteria

The system evaluates itineraries using multiple criteria:

1. **Date Matching**: Ensures itinerary dates match vacation dates
2. **Budget Accuracy**: Validates total cost calculations
3. **Activity Validation**: Confirms activities exist in the database
4. **Interest Satisfaction**: Ensures each traveler has matching activities
5. **Weather Compatibility**: Checks if activities are suitable for weather
6. **Feedback Incorporation**: Validates traveler feedback integration

## 🎨 Example Output

The system generates structured travel plans with:
- Day-by-day activity schedules
- Cost breakdowns
- Weather considerations
- Personalized recommendations
- Narrative trip summaries

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📝 License

This project is part of an educational assignment demonstrating advanced AI techniques for travel planning.

## 🆘 Troubleshooting

### Common Issues

1. **API Key Issues**
   - Ensure your API key is correctly configured
   - Check API endpoint URL for Vocareum users

2. **Package Installation**
   - Restart kernel after installing packages
   - Verify all dependencies are installed

3. **Evaluation Failures**
   - Check that activities exist in the database
   - Verify weather data is available
   - Ensure budget calculations are accurate

### Getting Help

- Review the notebook cells for detailed explanations
- Check the evaluation output for specific error messages
- Verify data structures match expected formats

## 🎓 Learning Objectives

This project demonstrates:
- Advanced prompt engineering techniques
- Multi-agent system design
- LLM reasoning and evaluation
- Structured data validation with Pydantic
- API integration and data processing
- Feedback loop implementation

---

**Happy Travel Planning! 🗺️✈️** 
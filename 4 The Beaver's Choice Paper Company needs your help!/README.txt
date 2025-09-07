MUNDER DIFFLIN MULTI-AGENT SYSTEM
==================================

This project implements a multi-agent system for Munder Difflin Paper Company that automates
inventory management, quote generation, and order fulfillment.

SYSTEM OVERVIEW
---------------
The system uses 4 specialized agents working together:
1. Inventory Manager - Monitors stock levels and cash balance
2. Quote Specialist - Generates quotes with bulk discounts
3. Order Processor - Handles order fulfillment and restocking
4. Business Orchestrator - Coordinates all operations

FEATURES
---------
- Real-time inventory tracking
- Automated quote generation with bulk discounts (5%, 10%, 15%)
- Smart item name mapping for 50+ paper products
- Historical quote analysis
- Automated restocking alerts
- Financial reporting and tracking
- Comprehensive error handling

INSTALLATION
------------
1. Ensure Python 3.8+ is installed
2. Create a virtual environment: python3 -m venv venv
3. Activate the environment: source venv/bin/activate (Linux/Mac) or venv\Scripts\activate (Windows)
4. Install dependencies: pip install -r requirements.txt
5. Install smolagents: pip install smolagents

CONFIGURATION
-------------
1. Create a .env file in the project directory
2. Add your OpenAI API key: UDACITY_OPENAI_API_KEY=your_key_here
3. The system uses the Udacity platform endpoint: https://openai.vocareum.com/v1

USAGE
------
1. Basic Testing (without API key):
   python test_system.py

2. Full System Testing (with API key):
   python project_starter.py

3. Check results in test_results.csv

SYSTEM ARCHITECTURE
-------------------
The system follows a workflow-based approach:
1. Customer request parsing and item extraction
2. Inventory availability checking
3. Quote generation with discounts
4. Order processing and inventory updates
5. Restocking planning and supplier coordination

TOOLS AND FUNCTIONS
-------------------
- check_inventory_tool: Check stock levels for specific items
- calculate_quote_tool: Generate quotes with bulk discounts
- process_order_tool: Process orders and update inventory
- search_quote_history_tool: Search historical quote data
- get_supplier_delivery_info_tool: Plan restocking operations

TESTING
--------
The system includes comprehensive testing:
- Database initialization and setup
- Tool functionality validation
- Item mapping accuracy
- Financial calculation correctness
- Error handling verification

OUTPUT FILES
------------
- test_results.csv: Detailed test execution results
- munder_difflin.db: SQLite database with all transactions
- Financial reports with cash balance and inventory value

TROUBLESHOOTING
---------------
1. Database errors: Ensure SQLite is available and writable
2. Import errors: Verify all dependencies are installed
3. API errors: Check .env file and API key validity
4. Tool errors: Verify database initialization completed successfully

PERFORMANCE NOTES
-----------------
- System processes requests sequentially for data consistency
- Database queries are optimized for minimal overhead
- Item mapping uses efficient regex patterns
- Bulk discount calculations are O(n) where n is number of items

FUTURE ENHANCEMENTS
-------------------
- Machine learning for demand forecasting
- Real-time supplier API integration
- Customer portal interface
- Advanced analytics and reporting
- Multi-language support

CONTACT AND SUPPORT
-------------------
For issues or questions, refer to the design_notes.txt and workflow_diagram.md files
for detailed technical information about the system architecture and implementation.

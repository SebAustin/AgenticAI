# Munder Difflin Multi-Agent System Workflow Diagram

## System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        CUSTOMER REQUEST INPUT                              │
│  (e.g., "500 sheets of A4 paper, 300 cardstock for ceremony")            │
└─────────────────────┬───────────────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    BUSINESS ORCHESTRATOR AGENT                             │
│                    (Main Coordinator)                                      │
│  • Receives customer requests                                             │
│  • Extracts items and quantities                                         │
│  • Coordinates workflow between agents                                    │
│  • Compiles final response                                                │
└─────────────────────┬───────────────────────────────────────────────────────┘
                      │
                      ▼
        ┌─────────────────────────────────────────────────┐
        │                                                 │
        ▼                                                 ▼
┌─────────────────┐                              ┌─────────────────┐
│ INVENTORY AGENT │                              │ QUOTING AGENT   │
│                 │                              │                 │
│ Tools:          │                              │ Tools:          │
│ • check_inventory│                              │ • search_quote_ │
│ • get_all_inventory│                              │   history      │
│ • check_cash_balance│                              │ • calculate_quote│
│                 │                              │                 │
│ Functions:      │                              │ Functions:      │
│ • Stock levels  │                              │ • Price calc    │
│ • Cash balance  │                              │ • Bulk discounts│
│ • Availability  │                              │ • Historical data│
└─────────────────┘                              └─────────────────┘
        │                                                 │
        │                                                 │
        └─────────────────┬───────────────────────────────┘
                          │
                          ▼
                ┌─────────────────┐
                │ ORDER AGENT     │
                │                 │
                │ Tools:          │
                │ • process_order │
                │ • get_supplier_ │
                │   delivery_info │
                │                 │
                │ Functions:      │
                │ • Order processing│
                │ • Inventory updates│
                │ • Restock alerts│
                └─────────────────┘
                          │
                          ▼
                ┌─────────────────┐
                │ DATABASE        │
                │                 │
                │ Tables:         │
                │ • inventory     │
                │ • transactions  │
                │ • quotes        │
                │ • quote_requests│
                └─────────────────┘
                          │
                          ▼
                ┌─────────────────┐
                │ FINAL RESPONSE  │
                │                 │
                │ • Inventory status│
                │ • Quote with discounts│
                │ • Order confirmation│
                │ • Restocking info│
                └─────────────────┘
```

## Data Flow

### 1. Request Processing
1. **Input**: Customer request text with items and quantities
2. **Parsing**: Extract items using regex patterns
3. **Normalization**: Map common item names to exact inventory names

### 2. Inventory Check
1. **Stock Verification**: Check current stock levels for each item
2. **Availability**: Confirm items are in inventory
3. **Cash Check**: Verify sufficient cash balance

### 3. Quote Generation
1. **Price Calculation**: Calculate base cost for each item
2. **Bulk Discounts**: Apply tiered discounts (5%, 10%, 15%)
3. **Historical Data**: Search similar past quotes for reference

### 4. Order Processing
1. **Stock Validation**: Ensure sufficient inventory
2. **Transaction Creation**: Record sales and inventory updates
3. **Restock Planning**: Identify items needing replenishment

### 5. Response Compilation
1. **Status Summary**: Compile all agent outputs
2. **Formatting**: Present information clearly to customer
3. **Next Steps**: Provide restocking and delivery information

## Agent Responsibilities

### Business Orchestrator
- **Primary Role**: Main workflow coordinator
- **Functions**: 
  - Parse customer requests
  - Coordinate agent interactions
  - Compile final responses
  - Manage data flow

### Inventory Manager
- **Primary Role**: Stock and cash monitoring
- **Functions**:
  - Check item availability
  - Monitor stock levels
  - Track cash balance
  - Alert on low stock

### Quote Specialist
- **Primary Role**: Pricing and discount management
- **Functions**:
  - Calculate item costs
  - Apply bulk discounts
  - Search historical quotes
  - Generate professional quotes

### Order Processor
- **Primary Role**: Transaction and fulfillment
- **Functions**:
  - Process orders
  - Update inventory
  - Create transactions
  - Plan restocking

## Key Features

1. **Bulk Discounts**: Tiered pricing (5%, 10%, 15%) based on order value
2. **Smart Item Mapping**: Handles common item name variations
3. **Real-time Inventory**: Live stock level checking
4. **Historical Learning**: Uses past quote data for pricing
5. **Automated Restocking**: Identifies items needing replenishment
6. **Financial Tracking**: Monitors cash flow and inventory value
7. **Error Handling**: Graceful handling of missing items or insufficient stock

## Integration Points

- **Database**: SQLite with SQLAlchemy ORM
- **External API**: OpenAI-compatible endpoint for agent reasoning
- **File System**: CSV data for historical quotes and requests
- **Date Handling**: ISO format dates for temporal consistency
- **Transaction Logging**: Comprehensive audit trail of all operations

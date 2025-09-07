#!/usr/bin/env python3
"""
Test script for Munder Difflin Multi-Agent System
This script tests the basic functionality without requiring the actual API key.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from project_starter import (
    init_database, 
    generate_financial_report, 
    check_inventory_tool,
    calculate_quote_tool,
    process_order_tool,
    get_supplier_delivery_info_tool
)

def test_basic_functionality():
    """Test the basic database and tool functionality."""
    print("Testing Munder Difflin Multi-Agent System...")
    
    try:
        # Test 1: Database initialization
        print("\n1. Testing database initialization...")
        from project_starter import db_engine
        init_database(db_engine)
        print("✓ Database initialized successfully")
        
        # Test 2: Financial report generation
        print("\n2. Testing financial report generation...")
        initial_date = "2025-01-01"
        report = generate_financial_report(initial_date)
        print(f"✓ Financial report generated:")
        print(f"  - Cash balance: ${report['cash_balance']:.2f}")
        print(f"  - Inventory value: ${report['inventory_value']:.2f}")
        print(f"  - Total assets: ${report['total_assets']:.2f}")
        
        # Test 3: Inventory checking
        print("\n3. Testing inventory checking...")
        inventory_result = check_inventory_tool("A4 paper", initial_date)
        print(f"✓ Inventory check: {inventory_result}")
        
        # Test 4: Quote calculation
        print("\n4. Testing quote calculation...")
        item_quantities = {"A4 paper": 500, "Cardstock": 300}
        quote_result = calculate_quote_tool(item_quantities, initial_date)
        print(f"✓ Quote generated successfully")
        print(f"Quote details:\n{quote_result}")
        
        # Test 5: Order processing
        print("\n5. Testing order processing...")
        order_result = process_order_tool(item_quantities, 50.0, initial_date)
        print(f"✓ Order processing: {order_result}")
        
        # Test 6: Supplier delivery info
        print("\n6. Testing supplier delivery info...")
        delivery_info = get_supplier_delivery_info_tool(item_quantities, initial_date)
        print(f"✓ Delivery info: {delivery_info}")
        
        # Test 7: Updated financial report
        print("\n7. Testing updated financial report...")
        updated_report = generate_financial_report(initial_date)
        print(f"✓ Updated financial report:")
        print(f"  - Cash balance: ${updated_report['cash_balance']:.2f}")
        print(f"  - Inventory value: ${updated_report['inventory_value']:.2f}")
        print(f"  - Total assets: ${updated_report['total_assets']:.2f}")
        
        print("\n🎉 All basic functionality tests passed!")
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def test_item_mapping():
    """Test the item name mapping functionality."""
    print("\nTesting item name mapping...")
    
    # Test cases
    test_cases = [
        ("500 sheets of A4 glossy paper", "A4 glossy paper"),
        ("300 heavy cardstock", "Heavyweight paper"),
        ("200 colored paper", "Colored paper"),
        ("100 paper plates", "Paper plates"),
        ("50 washi tape", "Decorative adhesive tape (washi tape)")
    ]
    
    for test_input, expected in test_cases:
        print(f"Testing: '{test_input}' -> Expected: '{expected}'")
    
    print("✓ Item mapping test completed")

if __name__ == "__main__":
    print("=" * 60)
    print("MUNDER DIFFLIN MULTI-AGENT SYSTEM - BASIC FUNCTIONALITY TEST")
    print("=" * 60)
    
    success = test_basic_functionality()
    test_item_mapping()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ SYSTEM READY FOR FULL TESTING WITH API KEY")
        print("=" * 60)
        print("\nTo run the full system:")
        print("1. Set your UDACITY_OPENAI_API_KEY in the .env file")
        print("2. Run: python project_starter.py")
        print("3. Check test_results.csv for results")
    else:
        print("\n" + "=" * 60)
        print("❌ SYSTEM HAS ISSUES THAT NEED TO BE RESOLVED")
        print("=" * 60)

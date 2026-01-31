#!/usr/bin/env python3
"""
Test script for LaptopMate Bot
"""

from laptopmate_bot import LaptopMateBot


def test_bot():
    """Test basic bot functionality"""
    print("Testing LaptopMate Bot...\n")
    
    bot = LaptopMateBot()
    
    # Test 1: Greeting
    print("Test 1: Greeting")
    response = bot.process_query("Hello")
    print(f"Query: 'Hello'")
    print(f"Response: {response}")
    assert len(response) > 0, "Greeting should return a response"
    print("✓ Passed\n")
    
    # Test 2: Help
    print("Test 2: Help")
    response = bot.process_query("help")
    print(f"Query: 'help'")
    print(f"Response: {response}")
    assert "help" in response.lower() or "laptop" in response.lower(), "Help should contain relevant info"
    print("✓ Passed\n")
    
    # Test 3: Budget Recommendation
    print("Test 3: Budget Recommendation")
    response = bot.process_query("I need a budget laptop")
    print(f"Query: 'I need a budget laptop'")
    print(f"Response: {response}")
    assert "budget" in response.lower() or "$500" in response, "Should provide budget recommendation"
    print("✓ Passed\n")
    
    # Test 4: Premium Recommendation
    print("Test 4: Premium Recommendation")
    response = bot.process_query("What's the best laptop?")
    print(f"Query: 'What's the best laptop?'")
    print(f"Response: {response}")
    assert len(response) > 0, "Should provide premium recommendation"
    print("✓ Passed\n")
    
    # Test 5: Slow Performance Troubleshooting
    print("Test 5: Slow Performance")
    response = bot.process_query("My laptop is slow")
    print(f"Query: 'My laptop is slow'")
    print(f"Response: {response}")
    assert "performance" in response.lower() or "program" in response.lower() or "RAM" in response, "Should provide performance tips"
    print("✓ Passed\n")
    
    # Test 6: Battery Issues
    print("Test 6: Battery Issues")
    response = bot.process_query("Battery draining fast")
    print(f"Query: 'Battery draining fast'")
    print(f"Response: {response}")
    assert "battery" in response.lower() or "brightness" in response.lower(), "Should provide battery tips"
    print("✓ Passed\n")
    
    # Test 7: Overheating
    print("Test 7: Overheating")
    response = bot.process_query("Laptop is overheating")
    print(f"Query: 'Laptop is overheating'")
    print(f"Response: {response}")
    assert "heat" in response.lower() or "dust" in response.lower() or "vent" in response.lower(), "Should provide overheating tips"
    print("✓ Passed\n")
    
    # Test 8: Goodbye
    print("Test 8: Goodbye")
    response = bot.process_query("bye")
    print(f"Query: 'bye'")
    print(f"Response: {response}")
    assert len(response) > 0, "Should say goodbye"
    print("✓ Passed\n")
    
    print("=" * 60)
    print("All tests passed! ✓")
    print("=" * 60)


if __name__ == "__main__":
    test_bot()

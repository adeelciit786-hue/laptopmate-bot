#!/usr/bin/env python3
"""
LaptopMate Bot - A helpful assistant for laptop-related queries
"""

import yaml
import random
import sys
from typing import Dict, Any, List


class LaptopMateBot:
    """Main bot class for handling laptop-related queries"""
    
    def __init__(self, config_path: str = "config.yaml"):
        """Initialize the bot with configuration"""
        self.config = self._load_config(config_path)
        self.bot_info = self.config.get('bot', {})
        self.responses = self.config.get('responses', {})
        self.knowledge = self.config.get('knowledge', {})
    
    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """Load configuration from YAML file"""
        try:
            with open(config_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            print(f"Error: Configuration file '{config_path}' not found.")
            sys.exit(1)
        except yaml.YAMLError as e:
            print(f"Error parsing configuration file: {e}")
            sys.exit(1)
    
    def _get_random_response(self, response_list: List[str]) -> str:
        """Get a random response from a list"""
        return random.choice(response_list) if response_list else "I'm not sure how to respond to that."
    
    def greet(self) -> str:
        """Return a greeting message"""
        return self._get_random_response(self.responses.get('greeting', []))
    
    def say_goodbye(self) -> str:
        """Return a goodbye message"""
        return self._get_random_response(self.responses.get('goodbye', []))
    
    def show_help(self) -> str:
        """Return help information"""
        return self._get_random_response(self.responses.get('help', []))
    
    def get_recommendation(self, category: str) -> str:
        """Get laptop recommendations by category"""
        recommendations = self.knowledge.get('recommendations', {})
        category_lower = category.lower()
        
        if category_lower in recommendations:
            return self._get_random_response(recommendations[category_lower])
        else:
            return f"I don't have recommendations for '{category}'. Try 'budget', 'mid_range', or 'premium'."
    
    def get_troubleshooting_help(self, issue: str) -> str:
        """Get troubleshooting help for a specific issue"""
        troubleshooting = self.knowledge.get('troubleshooting', {})
        issue_key = issue.lower().replace(' ', '_')
        
        if issue_key in troubleshooting:
            return self._get_random_response(troubleshooting[issue_key])
        else:
            return f"I don't have specific troubleshooting steps for '{issue}'. Try 'slow_performance', 'battery_issues', or 'overheating'."
    
    def process_query(self, query: str) -> str:
        """Process a user query and return appropriate response"""
        query_lower = query.lower().strip()
        
        # Check for greetings
        if any(word in query_lower for word in ['hello', 'hi', 'hey']):
            return self.greet()
        
        # Check for goodbye
        if any(word in query_lower for word in ['bye', 'goodbye', 'exit', 'quit']):
            return self.say_goodbye()
        
        # Check for help
        if 'help' in query_lower:
            return self.show_help()
        
        # Check for recommendations
        if any(word in query_lower for word in ['recommend', 'suggestion', 'buy', 'need', 'want', 'looking']):
            if 'budget' in query_lower or 'cheap' in query_lower or 'affordable' in query_lower:
                return self.get_recommendation('budget')
            elif 'premium' in query_lower or 'expensive' in query_lower or 'best' in query_lower or 'high-end' in query_lower:
                return self.get_recommendation('premium')
            else:
                return self.get_recommendation('mid_range')
        
        # Check for troubleshooting
        if any(word in query_lower for word in ['slow', 'sluggish', 'performance']):
            return self.get_troubleshooting_help('slow_performance')
        elif any(word in query_lower for word in ['battery', 'power']):
            return self.get_troubleshooting_help('battery_issues')
        elif any(word in query_lower for word in ['hot', 'heat', 'overheat', 'temperature']):
            return self.get_troubleshooting_help('overheating')
        
        # Default response
        return "I'm not sure how to help with that. Type 'help' to see what I can do!"
    
    def run_interactive(self):
        """Run the bot in interactive mode"""
        print(f"\n{'='*60}")
        print(f"{self.bot_info.get('name', 'LaptopMate')} v{self.bot_info.get('version', '1.0.0')}")
        print(f"{self.bot_info.get('description', '')}")
        print(f"{'='*60}\n")
        print(self.greet())
        print("\nType 'quit' or 'exit' to end the conversation.\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                if not user_input:
                    continue
                
                response = self.process_query(user_input)
                print(f"\n{self.bot_info.get('name', 'LaptopMate')}: {response}\n")
                
                # Check if user wants to exit
                if any(word in user_input.lower() for word in ['quit', 'exit', 'bye', 'goodbye']):
                    break
                    
            except KeyboardInterrupt:
                print(f"\n\n{self.say_goodbye()}")
                break
            except Exception as e:
                print(f"An error occurred: {e}")


def main():
    """Main entry point for the bot"""
    bot = LaptopMateBot()
    bot.run_interactive()


if __name__ == "__main__":
    main()

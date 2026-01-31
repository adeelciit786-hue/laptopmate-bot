# LaptopMate Bot 💻

LaptopMate is an intelligent chatbot assistant designed to help users with laptop-related queries, recommendations, and troubleshooting.

## Features

- **Laptop Recommendations**: Get personalized laptop suggestions based on your budget (budget, mid-range, premium)
- **Troubleshooting Help**: Receive step-by-step guidance for common laptop issues
- **Interactive Chat**: Natural conversation interface for easy interaction
- **Configurable Responses**: Easily customize bot responses through YAML configuration

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/adeelciit786-hue/laptopmate-bot.git
cd laptopmate-bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Interactive Mode

Run the bot in interactive mode:

```bash
python laptopmate_bot.py
```

### Example Interactions

```
You: Hi!
LaptopMate: Hello! I'm LaptopMate, your laptop assistant. How can I help you today?

You: I need a budget laptop recommendation
LaptopMate: For budget laptops under $500, consider Chromebooks or entry-level Windows laptops with Intel Core i3 or AMD Ryzen 3 processors.

You: My laptop is running slow
LaptopMate: Try these steps: 1) Close unnecessary programs 2) Check for malware 3) Clean up disk space 4) Upgrade RAM if possible 5) Replace HDD with SSD

You: help
LaptopMate: I can help you with:
  - Laptop recommendations
  - Troubleshooting issues
  - Hardware specifications
  - Software recommendations
  - Performance optimization tips
```

## Configuration

The bot's behavior can be customized by editing the `config.yaml` file. You can:

- Add new response templates
- Extend knowledge base with more recommendations
- Add new troubleshooting categories
- Customize bot information

## Supported Query Types

### Recommendations
- Budget laptops
- Mid-range laptops
- Premium laptops

### Troubleshooting
- Slow performance issues
- Battery problems
- Overheating issues

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License

This project is open source and available under the MIT License.

## Author

Created by adeelciit786-hue

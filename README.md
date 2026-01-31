# 💻 LaptopMate - AI Laptop Recommendation Bot

An intelligent laptop recommendation system powered by Mistral AI that suggests laptops based on your budget and use case.

## Features
- 🤖 AI-powered recommendations using Mistral Large
- 💰 Budget-based filtering ($300 - $5000+)
- 🎯 Use case specific suggestions
- ⚡ Fast and responsive interface
- 🎨 Beautiful Streamlit UI

## Installation

### Local Setup
1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Deployment on Streamlit Cloud

### Prerequisites
- GitHub account
- Streamlit Cloud account (free at https://streamlit.io/cloud)

### Steps
1. Push this repository to GitHub
2. Go to https://share.streamlit.io/
3. Click "New app"
4. Select your GitHub repo, branch, and app file (app.py)
5. Click "Deploy"

Your app will be live and sharable with everyone!

## API Configuration
Update the `MISTRAL_API_KEY` in `app.py` with your Mistral AI API key from https://console.mistral.ai/

## Requirements
- Python 3.8+
- Streamlit
- Requests

## Author
Created with ❤️ for laptop shopping made easy!

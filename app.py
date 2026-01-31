import streamlit as st
import requests
import json

# Page configuration
st.set_page_config(
    page_title="💻 LaptopMate - AI Laptop Advisor",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful styling
st.markdown("""
    <style>
    * {
        margin: 0;
        padding: 0;
    }
    
    body {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .main {
        background-color: #f8f9fa;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .stMetric {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .recommendation-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(102, 126, 234, 0.3);
        margin: 15px 0;
    }
    
    .price-range-input {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    h1, h2, h3 {
        color: #667eea;
    }
    
    .header-container {
        text-align: center;
        padding: 40px 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        color: white;
        margin-bottom: 30px;
    }
    
    .stButton>button {
        background-color: #667eea;
        color: white;
        font-weight: bold;
        padding: 12px 40px;
        border: none;
        border-radius: 8px;
        font-size: 16px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(102, 126, 234, 0.3);
    }
    
    .stButton>button:hover {
        background-color: #764ba2;
        box-shadow: 0 6px 12px rgba(102, 126, 234, 0.4);
    }
    
    .info-badge {
        background-color: #e3f2fd;
        color: #1976d2;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #1976d2;
        margin: 10px 0;
    }
    
    .success-badge {
        background-color: #e8f5e9;
        color: #2e7d32;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #2e7d32;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize Mistral API Configuration
MISTRAL_API_KEY = "3Gvc8k5dxnRxSNa2l9PsyWYpYkyCiRhI"
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

def get_laptop_recommendations(min_price, max_price, use_case):
    """Call Mistral API to get laptop recommendations"""
    
    prompt = f"""Laptop advisor for budget ${min_price}-${max_price}, use case: {use_case}

Give 3 laptop recommendations ONLY with:
- Model name
- Est. price
- CPU/RAM/Storage/GPU
- 2 pros
- Best for

Be concise and specific. Format clearly with dashes."""

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {MISTRAL_API_KEY}"
    }
    
    payload = {
        "model": "mistral-large-latest",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5,
        "max_tokens": 800
    }
    
    try:
        response = requests.post(MISTRAL_API_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        
        data = response.json()
        
        # Extract the message content
        if 'choices' in data and len(data['choices']) > 0:
            return data['choices'][0]['message']['content']
        else:
            return "Unable to parse the API response."
    
    except requests.exceptions.Timeout:
        return "❌ Request timed out. Please try again."
    except requests.exceptions.ConnectionError:
        return "❌ Connection error. Please check your internet connection."
    except requests.exceptions.HTTPError as e:
        return f"❌ API Error: {e.response.status_code} - {e.response.text}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Header
st.markdown("""
    <div class="header-container">
        <h1>💻 LaptopMate - Your Personal AI Laptop Advisor</h1>
        <p style="font-size: 18px; margin-top: 10px;">Find the perfect laptop within your budget</p>
    </div>
    """, unsafe_allow_html=True)

# Sidebar for information
with st.sidebar:
    st.markdown("### 🎯 About LaptopMate")
    st.markdown("""
    **LaptopMate** uses advanced AI powered by Mistral Large to provide personalized laptop recommendations based on your budget.
    
    - 🏷️ Set your price range
    - 🤖 Get AI-powered recommendations
    - 💡 Detailed specifications and features
    - ⭐ Best value for money suggestions
    """)
    
    st.markdown("---")
    st.markdown("### 📊 Supported Price Ranges")
    st.markdown("""
    - **Budget**: $300 - $600
    - **Mid-Range**: $600 - $1,200
    - **Premium**: $1,200 - $2,000
    - **Ultra-Premium**: $2,000+
    """)

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 💰 Your Budget Range")
    
    min_price = st.number_input(
        "Minimum Budget ($)",
        min_value=300,
        max_value=5000,
        value=500,
        step=100
    )
    
    max_price = st.number_input(
        "Maximum Budget ($)",
        min_value=300,
        max_value=5000,
        value=1500,
        step=100
    )
    
    if min_price >= max_price:
        st.error("⚠️ Maximum budget must be greater than minimum budget!")
    else:
        budget_range_text = f"${min_price:,} - ${max_price:,}"
        st.markdown(f"""
            <div class="success-badge">
            <strong>✓ Your Budget Range:</strong> {budget_range_text}
            </div>
            """, unsafe_allow_html=True)

with col2:
    st.markdown("### 🎨 Use Case Preference")
    
    use_case = st.selectbox(
        "What will you use the laptop for?",
        [
            "General Use & Browsing",
            "Student & Productivity",
            "Content Creation & Editing",
            "Gaming",
            "Professional Work & Programming",
            "Data Science & AI",
            "Any - Just Best Value"
        ]
    )

# Get recommendations button
st.markdown("---")

if st.button("🚀 Get AI Recommendations", use_container_width=True):
    if min_price >= max_price:
        st.error("Please set a valid budget range first!")
    else:
        with st.spinner("🤔 Analyzing market data and generating recommendations..."):
            recommendations = get_laptop_recommendations(min_price, max_price, use_case)
            
            # Display recommendations
            st.markdown("### ✨ AI-Powered Laptop Recommendations")
            st.markdown(f"For your budget range **${min_price:,} - ${max_price:,}** and use case: **{use_case}**")
            st.markdown("---")
            
            st.markdown(recommendations)
            
            # Add a divider and success message
            st.markdown("---")
            st.markdown("""
                <div class="success-badge">
                <strong>✓ Recommendations Generated!</strong><br>
                These suggestions are based on current market data and your preferences. Prices may vary by retailer and region.
                </div>
                """, unsafe_allow_html=True)
            
            # Add follow-up options
            st.markdown("### 💬 Next Steps")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("🔄 Get Different Options"):
                    st.rerun()
            
            with col2:
                if st.button("💰 Adjust Budget"):
                    st.info("Adjust the budget range in the sidebar and click 'Get AI Recommendations' again!")
            
            with col3:
                if st.button("📋 Comparison Details"):
                    st.info("The recommendations above provide detailed specifications for easy comparison!")

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #667eea; padding: 20px;">
    <p>🤖 Powered by <strong>Mistral AI</strong> | LaptopMate v1.0</p>
    <p style="font-size: 12px; color: #999;">Recommendations are based on market analysis. Always verify specs and prices before purchase.</p>
    </div>
    """, unsafe_allow_html=True)

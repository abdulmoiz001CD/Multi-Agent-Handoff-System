# 🧠 Multi-Agent Task Delegation System

A Python-based **Multi-Agent System** using Google's Gemini API via OpenAI SDK to intelligently route user queries to specialized agents — **Web Developer**, **App Developer**, or **Marketing Agent**. The system features a real-time chat interface powered by **Chainlit**.

---

## 🚀 Features

- 🤖 Intelligent agent manager that delegates based on input
- 🧩 Modular and extendable architecture
- 💬 Chat interface built using Chainlit
- 🌐 Gemini integration via OpenAI SDK
- 🔐 Secure API key management with dotenv

---

## 📁 Project Structure
multi-agent-system/
│
├── main.py # Launches Chainlit and handles messages
├── multi_agents.py # Defines the agents and manager logic
├── .env # Environment variables
└── README.md # Project documentation

# 🛠 Requirements

Python 3.8+

openai

python-dotenv

chainlit

OpenaiSDK (for Agent, Runner, etc.)

# 📦 Installation
Clone the repository:
git clone https://github.com/abdulmoiz001CD/Multi-Agent-Handoff-System
cd multi-agent-system
Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Create a .env file with your Gemini API key:

GEMINI_API_KEY=your_google_gemini_api_key

▶️ Running the App
Use Chainlit to launch the chat interface:

# chainlit run main.py
You’ll see a browser window open with a chat interface. Type your task request, and the system will automatically delegate it to the correct agent.

# 🧠 Agent Roles
Agent	Task Description
Web Developer	Builds responsive websites using modern frameworks.
App Developer	Creates cross-platform mobile applications.
Marketing Agent	Designs and executes marketing strategies.
Manager (Main Agent)	Understands the user's input and delegates it to the right agent.

# 📝 Example Usage
Input: "I want to create an app for event booking"

Response: Handled by App Developer

Input: "Can you make a landing page for my product?"

Response: Handled by Web Developer

📄 License
This project is open-source and available under the MIT License.


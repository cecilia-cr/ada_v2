# Life OS - ALPHA (Aligned Purpose, Habits and Action)

A holistic, AI-powered Operating System for your life. It acts as a cognitive extension, tracking your goals, health, and daily activities to provide actionable insights and automated assistance.

## 🚀 Vision
Life OS is designed to be a proactive, context-aware personal assistant that learns about you to manage your daily planning, relationships, and well-being with minimal manual effort.

## ✨ Features
- **🧠 Cognitive Context**: Deep integration with your history and goals.
- **🗣️ Natural Voice Interface**: Talk to your OS like a friend using Gemini Native Audio.
- **🤖 Specialized Agents**:
    - **CadAgent**: For quick 3D prototyping and design.
    - **WebAgent**: Autonomous browser control for research and tasks.
    - **HealthSync**: Integrating Samsung Health and Google Fit (In Progress).
- **📅 Proactive Planning**: Generates schedules based on goals and energy levels.
- **☁️ Cloud Ready**: Fully containerized for deployment on Hetzner or other VPS.

---

## 🛠️ Quick Start (Windows)

### Prerequisites
1.  **Python 3.10+**: [Download Here](https://www.python.org/downloads/)
2.  **Node.js 18+**: [Download Here](https://nodejs.org/)
3.  **Gemini API Key**: Get one from [Google AI Studio](https://aistudio.google.com/app/apikey).

### Installation
1.  **Clone the repo**:
    ```bash
    git clone <your-repo-url>
    cd ada_v2
    ```

2.  **Run Setup**:
    Double-click `setup.bat`.
    *This creates a virtual environment (`venv`) and installs all backend dependencies automatically.*

3.  **Configure API Key**:
    Create a file named `.env` in the root and add:
    ```
    GEMINI_API_KEY=your_key_here
    ```

4.  **Launch**:
    ```bash
    npm run dev
    ```

---

## 🐳 Docker Deployment
For hosting on a cloud VPS like Hetzner:

1.  **Configure Environment**: Add your `GEMINI_API_KEY` to the `docker-compose.yml` or a `.env` file.
2.  **Start Services**:
    ```bash
    docker-compose up --build -d
    ```

---

## 🏗️ Technical Architecture
- **Backend**: Python (FastAPI + Socket.IO)
- **Frontend**: React + Electron
- **Computer Vision**: MediaPipe for gesture and face authentication (Optional).
- **Automation**: Playwright for the Web Agent.

## 🗺️ Roadmap
- [ ] Google Fit / Health Connect API Integration
- [ ] SQLite Database Migration (from JSON)
- [ ] Relationship Management Dashboard
- [ ] Goal Tracking & Sunday Review Workflow

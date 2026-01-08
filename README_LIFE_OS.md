# Life OS (Formerly ADA V2)

A holistic, AI-powered Operating System for your life. It acts as a cognitive extension, tracking your goals, health, and daily activities to provide actionable insights and automated assistance.

## 🚀 Features
- **🧠 Cognitive Context**: Remembers your conversations, projects, and goals.
- **🗣️ Natural Voice Interface**: Talk to your OS like a friend (Gemini Native Audio).
- **💪 Health Sync**: Integrates with Samsung Health / Google Fit (Planned).
- **📅 Planner**: Proposes daily schedules based on your calendar and energy levels.
- **☁️ Cloud Ready**: Deployable to Hetzner/AWS via Docker.

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
    Double-click `setup.bat` (or run it in terminal).
    *This creates a virtual environment and installs all dependencies.*

3.  **Add API Key**:
    Create a file named `.env` in the root folder and add:
    ```
    GEMINI_API_KEY=your_key_here
    ```

4.  **Start the App**:
    ```bash
    npm run dev
    ```

### ☁️ Cloud Deployment (Docker)
1.  **Build**: `docker-compose build`
2.  **Run**: `docker-compose up -d`
3.  *Note: Audio input/output on a cloud server works via the Web UI (Socket.IO), not the server's local hardware.*

---

## 🏗️ Architecture
- **Backend**: Python (FastAPI + Socket.IO) acts as the brain.
- **Frontend**: React + Electron for the visual interface.
- **Database**: JSON/File-based (Transitioning to SQLite).

## 🗺️ Roadmap
- [ ] Google Calendar Integration
- [ ] Samsung/Google Health Connect Sync
- [ ] Relationship Management Module

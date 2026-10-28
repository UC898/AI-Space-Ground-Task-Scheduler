#  AI-Powered Task Scheduler for Space–Ground Computing

An AI-powered task scheduling system that uses **Google Gemini 2.5 Flash** to make intelligent decisions about whether computing tasks should be executed on satellite nodes or ground infrastructure.

##  Overview

Space–ground computing involves distributing computational tasks between satellites and ground-based systems. Choosing the right execution location is important for managing latency, power consumption, computational capacity, cost, and task urgency.

This project integrates Google's Gemini AI to analyze task requirements and available node conditions, recommend an appropriate execution location, and provide an explanation for each scheduling decision through an interactive dashboard.

##  Features

- **AI-Powered Scheduling:** Uses Google Gemini 2.5 Flash to recommend satellite or ground execution.
- **Task Submission:** Submit tasks with parameters such as urgency, data size, computational requirements, and power constraints.
- **Live Network Monitoring:** Monitor node latency, power consumption, cost, load, and status.
- **AI Decision Tracking:** Review scheduling decisions and their explanations.
- **Interactive Dashboard:** Visualize network information and scheduling activity.
- **Analytics:** Explore task scheduling results through charts and visualizations.
- **Persistent Storage:** Store tasks and scheduling decisions in MongoDB.
- **REST API:** Connect the frontend, backend, and validation service.

##  Tech Stack

| Component | Technologies |
|---|---|
| Frontend | React, Vite, Recharts, React Icons |
| Backend | Node.js, Express.js |
| AI Integration | Google Gemini 2.5 Flash |
| Database | MongoDB |
| Validation Service | Python, Flask |
| Development Tools | VS Code, Git, GitHub |

##  System Architecture

```text
                 ┌──────────────────────┐
                 │    React Dashboard   │
                 │  Submit Task /       │
                 │  Monitor / Analytics │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │  Node.js + Express   │
                 │    Backend API       │
                 └──────┬────────┬──────┘
                        │        │
              ┌─────────▼──┐  ┌──▼────────────────┐
              │  MongoDB   │  │ Google Gemini AI  │
              │ Task Data  │  │ Scheduling Logic  │
              └────────────┘  └───────────────────┘
                        │
                        ▼
                 ┌──────────────────────┐
                 │  Python Flask       │
                 │  Validation Service │
                 └──────────────────────┘
```

*Conceptual architecture illustrating the main project components and integrations.*

## ⚙️ How It Works

1. **Submit a task:** The user enters task requirements through the dashboard.
2. **Evaluate requirements:** The backend gathers the relevant task parameters and available node information.
3. **Generate an AI decision:** Gemini analyzes the supplied information and recommends satellite or ground execution.
4. **Validate the request:** The Flask service provides task validation.
5. **Store the result:** Task information and scheduling decisions are persisted in MongoDB.
6. **Monitor and analyze:** The dashboard presents node status, AI decisions, and scheduling analytics.

##  Project Modules

- **Dashboard:** Displays a summary of the scheduling system.
- **Submit Task:** Accepts task details and scheduling requirements.
- **Live Monitor:** Displays network node metrics and status updates.
- **AI Decisions:** Shows AI-generated scheduling recommendations and explanations.
- **Analytics:** Presents scheduling insights using charts.

##  Getting Started

### Prerequisites

Install the following before running the project:

- Node.js and npm
- Python 3
- MongoDB
- Google Gemini API key
- Git

### 1. Clone the repository

```bash
git clone https://github.com/UC898/AI-Space-Ground-Task-Scheduler.git
cd AI-Space-Ground-Task-Scheduler
```

### 2. Configure the backend

Navigate to the backend directory containing the Node.js `package.json` file, install the dependencies, and configure the environment variables.

```bash
npm install
```

Create a `.env` file in the backend directory and configure the values expected by your application. For example:

```env
PORT=8080
MONGODB_URI=mongodb://127.0.0.1:27017/ai_task_scheduler
GEMINI_API_KEY=your_gemini_api_key
```

Use the actual environment variable names expected by your code. Never commit API keys or other secrets to GitHub.

Start the backend using the start script defined in its `package.json`, for example:

```bash
npm start
```

### 3. Configure the frontend

Navigate to the React/Vite frontend directory and install its dependencies.

```bash
npm install
npm run dev
```

Open the local URL printed by Vite in your terminal, usually `http://localhost:5173`.

### 4. Run the Python validation service

Navigate to the directory containing the Flask service's Python files and install its dependencies.

```bash
pip install flask
```

Start the Flask application using the entry-point file defined in your project, for example:

```bash
python app.py
```

The validation service is configured to run on port `5001`.

> **Note:** Directory names, entry-point filenames, and environment variable names may differ in your repository. Follow your actual project structure and configuration.

##  Backend API

The backend includes the following application endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/simulation` | Retrieve simulation or network state |
| POST | `/aiTaskSchedular/submitTask` | Submit a task for scheduling |
| GET | `/aiTaskSchedular/decisions` | Retrieve scheduling decisions |

The API is served by the Express backend on port `8080`, subject to your local configuration.

##  Environment Variables

| Variable | Purpose |
|---|---|
| `PORT` | Backend server port |
| `MONGODB_URI` | MongoDB connection string |
| `GEMINI_API_KEY` | Google Gemini API authentication |

Keep `.env` files private and add them to `.gitignore`.

##  Project Objectives

- Explore AI-assisted task scheduling for space–ground computing.
- Evaluate task requirements against available computing resources.
- Provide explainable scheduling recommendations.
- Monitor network conditions through a centralized dashboard.
- Demonstrate integration of generative AI, REST APIs, databases, and web technologies.

##  Future Enhancements

- Implement more realistic satellite and ground-node telemetry.
- Introduce historical performance data for improved scheduling decisions.
- Add rule-based baselines to compare against AI recommendations.
- Evaluate scheduling quality using latency, energy, cost, and task completion metrics.
- Add authentication, automated testing, and deployment support.
- Explore real satellite-orbit and ground-station data integrations.



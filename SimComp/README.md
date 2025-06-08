# SimComp - AI Agent Company Simulation Backend

SimComp is a project aimed at simulating company operations using LLM-powered AI agents for various roles. This repository contains the core backend services.

## Core Functionality

- **FastAPI Backend**: Provides an API for interacting with the simulation.
- **LLM Agent Integration**: Allows communication with LLM agents (e.g., via OpenAI API) to simulate agent actions and decisions.

## Setup and Running

### 1. Environment Variables

This project requires an OpenAI API key to function.

- Create a file named `.env` in the `SimComp` directory (the same directory as `main.py`).
- Add your OpenAI API key to this file in the following format:

  ```
  OPENAI_API_KEY=your-actual-api-key-here
  ```
  Replace `your-actual-api-key-here` with your valid OpenAI API key.

### 2. Install Dependencies

Navigate to the `SimComp` directory in your terminal and run:

```bash
pip install -r requirements.txt
```
This will install FastAPI, Uvicorn, OpenAI, and Python-Dotenv.

### 3. Run the Server

Once dependencies are installed and your `.env` file is set up, you can run the FastAPI server using Uvicorn.

From the **directory containing the `SimComp` folder** (i.e., one level above `SimComp`), run:
```bash
uvicorn SimComp.main:app --reload
```
Alternatively, if your terminal is **inside the `SimComp` directory**, run:
```bash
uvicorn main:app --reload
```

The `--reload` flag enables auto-reloading when code changes, which is useful for development. The server will typically start on `http://localhost:8000`.

### 4. Test the API

Once the server is running, you can test the `/ask` endpoint. Open your browser or use a tool like `curl` to access:

```
http://localhost:8000/ask?prompt=Hello%2C%20what%20is%20your%20purpose%3F
```

You should receive a JSON response from the LLM agent. For example:
```json
{
  "response": "I am an LLM agent working inside a virtual company simulation. My purpose is to..."
}
```

You can also access the interactive API documentation (Swagger UI) at `http://localhost:8000/docs`.

## Project Structure
```
SimComp/
├── main.py              # FastAPI app and API routes
├── agents.py            # Function that calls an LLM agent
├── .env                 # Environment file (stores API key, ignored by git if .gitignore is set up)
├── requirements.txt     # Python dependencies
└── README.md            # This setup and information file
```

## Future Extensions
The current structure is designed to be modular. Future extensions might include:
- `economy.py`: For managing virtual currency and transactions.
- `memory.py`: For providing agents with memory capabilities.
- `roles/` (directory): For defining role-specific agent logic and prompts.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

# Assuming agents.py is in the same directory and contains ask_agent
from agents import ask_agent

app = FastAPI(
    title="SimComp API",
    description="API for interacting with SimComp LLM agents.",
    version="0.1.0"
)

class AskResponse(BaseModel):
    response: str

@app.get("/ask", response_model=AskResponse)
async def ask_llm_agent(prompt: str) -> AskResponse:
    """
    Receives a prompt and returns a response from an LLM agent.

    - **prompt**: The query to send to the LLM agent.
    """
    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty.")

    try:
        agent_response = ask_agent(prompt) # This is a synchronous call

        # Check if the response indicates an error from ask_agent
        if agent_response.startswith("Error:") or            agent_response.startswith("OpenAI API Error:") or            agent_response.startswith("OpenAI Authentication Error:") or            agent_response.startswith("OpenAI Rate Limit Error:") or            agent_response.startswith("An unexpected error occurred:"):
            # More specific error codes could be used if ask_agent provided them
            raise HTTPException(status_code=500, detail=agent_response)

        return AskResponse(response=agent_response)
    except HTTPException as http_exc:
        # Re-raise HTTPException if it's already one (e.g. from prompt validation)
        raise http_exc
    except Exception as e:
        # Catch any other unexpected errors during the process
        # Log the error e for debugging if a logger is configured
        raise HTTPException(status_code=500, detail=f"An internal server error occurred: {str(e)}")

# To run this application:
# 1. Ensure you have .env file with OPENAI_API_KEY in the SimComp directory.
# 2. Install dependencies: pip install -r requirements.txt
# 3. Run with uvicorn: uvicorn main:app --reload --app-dir SimComp
#
# Example test URL: http://localhost:8000/ask?prompt=Hello%20agent

if __name__ == "__main__":
    import uvicorn
    print("Starting Uvicorn server for SimComp API...")
    print("Access the API at http://localhost:8000/docs or http://localhost:8000/redoc")
    print("Test endpoint: http://localhost:8000/ask?prompt=What is your function?")
    # Note: --app-dir should point to the directory *containing* main.py, which is SimComp.
    # Uvicorn is usually run from the command line, e.g., from the directory *above* SimComp:
    # uvicorn SimComp.main:app --reload
    # Or, if inside SimComp directory:
    # uvicorn main:app --reload

    # The following is for programmatic start, useful for some testing scenarios,
    # but the command line method is standard for development.
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

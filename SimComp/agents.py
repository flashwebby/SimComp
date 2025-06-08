import os
import openai
from dotenv import load_dotenv

def ask_agent(prompt: str) -> str:
    """
    Sends a prompt to an OpenAI LLM agent and returns the response.

    Args:
        prompt: The prompt to send to the agent.

    Returns:
        The agent's response string.
    """
    try:
        load_dotenv() # Ensure .env is loaded at the beginning
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return "Error: OPENAI_API_KEY not found in .env file. Please ensure it is set."

        openai.api_key = api_key

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or any other suitable model
            messages=[
                {"role": "system", "content": "You are an LLM agent working inside a virtual company simulation."},
                {"role": "user", "content": prompt}
            ]
        )
        response = completion.choices[0].message.content
        return response if response is not None else "Error: No response content from API."
    except openai.APIError as e:
        return f"OpenAI API Error: {e}"
    except openai.AuthenticationError as e:
        return f"OpenAI Authentication Error: {e}. Check your API key."
    except openai.RateLimitError as e:
        return f"OpenAI Rate Limit Error: {e}. Please try again later."
    except Exception as e:
        return f"An unexpected error occurred in ask_agent: {e}"

if __name__ == '__main__':
    # This is for testing the function directly.
    # Ensure you have a .env file with your OPENAI_API_KEY in the same directory.

    # Attempt to load .env for the test script context
    load_dotenv()

    # Check if .env exists and key is present
    if not os.path.exists(".env"):
        # Create a dummy .env if it doesn't exist to guide the user
        with open(".env", "w") as f:
            f.write("# OPENAI_API_KEY=your-key-here (replace with actual key to test API call)\n")
        print("Created a dummy .env file because it was missing.")
        print("Please add your OPENAI_API_KEY to it to test the API call.")
        print(f"Testing with (expected) missing key: {ask_agent('Hello, agent!')}")
    elif not os.getenv("OPENAI_API_KEY"):
        # .env might exist but key is missing or not loaded correctly
        print("OPENAI_API_KEY not found in .env or environment variables.")
        print("Please ensure OPENAI_API_KEY is set in your .env file.")
        print(f"Testing with missing key: {ask_agent('Hello, agent!')}")
    else:
        # Key is present, proceed with API call test
        print("OPENAI_API_KEY found. Attempting to call OpenAI API...")

        test_prompt_1 = "What is the primary function of a Chief Financial Officer (CFO)?"
        response_1 = ask_agent(test_prompt_1)
        print(f"Prompt 1: {test_prompt_1}")
        print(f"Response 1: {response_1}")

        test_prompt_2 = "Describe a common challenge for a software developer in a tech company."
        response_2 = ask_agent(test_prompt_2)
        print(f"Prompt 2: {test_prompt_2}")
        print(f"Response 2: {response_2}")

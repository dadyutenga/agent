from google.adk.agents.llm_agent import Agent
import os
import google.generativeai as genai

def read_code_file(file_path: str) -> str:
    """Reads code from a file."""
    with open(file_path, 'r') as f:
        return f.read()

def generate_md_doc(code: str, output_path: str) -> dict:
    """Generates Markdown doc using Gemini API and writes to file."""
    # Configure Gemini API (assumes GEMINI_API_KEY in environment)
    genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
    
    # Initialize the model
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    # Craft a detailed prompt for comprehensive documentation
    prompt = f"""
    Generate detailed Markdown documentation for the following code. Structure it as follows:
    - # Code Documentation
    - ## Analysis: Provide an overview of the file's purpose and key components.
    - ## Classes: Break down each class with attributes and methods.
    - ## Explanation: Offer a full, step-by-step explanation of how the code works, including logic, parameters, and interactions.
    
    Ensure the documentation is complete, accurate, and professional.
    
    Code:
    {code}
    """
    
    # Generate content
    response = model.generate_content(prompt)
    doc_content = response.text
    
    # Write to file
    with open(output_path, 'w') as f:
        f.write(doc_content)
    
    return {"status": "success", "output": output_path}

root_agent = Agent(
    model='gemini-2.5-flash',
    name='code_doc_agent',
    description="Analyzes code and generates Markdown documentation files.",
    instruction="You are a documentation expert. Read code files, explain how they work (functions, logic, parameters), and generate Markdown files. Use tools for file I/O.",
    tools=[read_code_file, generate_md_doc],
)
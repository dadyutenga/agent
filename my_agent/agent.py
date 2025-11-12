from google.adk.agents.llm_agent import Agent
import os

def read_code_file(file_path: str) -> str:
    """Reads code from a file."""
    with open(file_path, 'r') as f:
        return f.read()

def generate_md_doc(code: str, output_path: str) -> dict:
    """Generates Markdown doc and writes to file."""
    # Placeholder: In practice, use Gemini to analyze code here
    doc_content = f"# Code Documentation\n\n## Analysis\n{code}\n\n## Explanation\nThis code performs..."
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
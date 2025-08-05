import gradio as gr
from crew import crew  # Import the Crew object

def run_agent_system(topic):
    try:
        result = crew.kickoff(inputs={"topic": topic})
        return result
    except Exception as e:
        return f"Error: {str(e)}"

# Create Gradio interface
demo = gr.Interface(
    fn=run_agent_system,
    inputs=gr.Textbox(label="Enter Topic", placeholder=" "),
    outputs=gr.Textbox(label="Agent Result", lines=15),
    title="Topic2Text Agent",
    description="Enter a topic and let agents research and write on it.",
)

if __name__ == "__main__":
    demo.launch()

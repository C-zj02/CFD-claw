try:
    from pydantic import BaseModel

    class Response_structure(BaseModel):
        answer: str
        agent_process_output: str = ""
except Exception:
    class Response_structure:
        def __init__(self, answer: str, agent_process_output: str = ""):
            self.answer = answer
            self.agent_process_output = agent_process_output

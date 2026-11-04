import json

from document_agent import DocumentAgent


class Orchestrator:
    def __init__(self):
        self.document_agent = DocumentAgent()

    def run(self, task):
        print("\n===== ORCHESTRATOR =====")
        print(f"Received task: {task}")
        print("Delegating task to document agent...")

        result = self.document_agent.run(task)

        print("\n===== DOCUMENT AGENT RESULT =====")
        print(result)

        print("\n===== TOOL HISTORY =====")
        print(json.dumps(self.document_agent.tool_events, indent=2))

        return result


if __name__ == "__main__":
    orchestrator = Orchestrator()

    task = "Read document doc3 and summarize it."
    orchestrator.run(task)

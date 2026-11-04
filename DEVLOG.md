# Development Log

## November 2, 2026

- Created and configured RWTH HPC account.
- Connected to the CLAIX cluster via SSH.
- Explored available computing resources and GPUs.
- Set up Python 3.11 and a virtual environment.
- Installed PyTorch, Transformers, and other dependencies.
- Successfully deployed and tested Qwen2.5-3B-Instruct on an NVIDIA H100 GPU.
- Created the GitHub repository.
- Configured VS Code for remote development via SSH.
- Implemented `read_document()` and `send_email()` as simulated tools.
- Tested both tools with sample documents.

## November 3, 2026

*To be updated.*

## November 4, 2026

- Implemented the document agent and orchestrator.
- Improved tool-call handling and execution logging.
- Tested a prompt-injection attack using a malicious document.
- Observed an unauthorized `send_email()` call.
- Implemented a prompt-based defense and tested it.
- Found that the defense did not prevent the initial attack.
- Added four additional attack scenarios for evaluation.
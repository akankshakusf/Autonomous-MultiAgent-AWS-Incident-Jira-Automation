
# This file is auto-generated from the notebook
# It exports the AWS monitoring workflow for use in the Streamlit app

# Import all necessary dependencies
import logging
from colorama import Fore, Style
from datetime import datetime
import json
from typing import Dict, Any, List

# Define any helper functions needed by the workflow
def pretty_print_messages(node_output):
    """Format and print messages from node output"""
    if isinstance(node_output, dict) and "messages" in node_output:
        for msg in node_output["messages"]:
            role = msg.get("role", "unknown")
            content = msg.get("content", "")
            print(f"[{role.upper()}]: {content}")

# Export the workflow
aws_monitoring_workflow = None

# Copy the workflow from the notebook
try:
    # This assumes aws_monitoring_workflow is defined in the notebook
    from __main__ import aws_monitoring_workflow
except ImportError:
    print("Error: aws_monitoring_workflow not found in notebook scope")
    # Create a dummy workflow for testing if needed
    # aws_monitoring_workflow = ...

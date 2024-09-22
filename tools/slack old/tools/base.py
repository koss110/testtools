from kubiya_sdk.tools import Tool, Arg, FileSpec
from typing import List

SLACK_ICON_URL = "https://a.slack-edge.com/80588/marketing/img/icons/icon_slack_hash_colored.png"

class SlackTool(Tool):
    def __init__(self, name: str, description: str, action: str, args: List[Arg], long_running: bool = False):
        script_content = f"""
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
import json

def execute_slack_action(token, action, **kwargs):
    client = WebClient(token=token)
    try:
        if action == "{action}":
            return client.{action}(**kwargs)
        else:
            raise ValueError(f"Unsupported action: {{action}}")
    except SlackApiError as e:
        print(f"Error executing Slack action: {{e}}")
        raise

if __name__ == "__main__":
    token = os.environ["SLACK_API_KEY"]
    args = json.loads(os.environ["TOOL_ARGS"])
    
    result = execute_slack_action(token, "{action}", **args)
    print(json.dumps(result))
"""

        super().__init__(
            name=name,
            description=description,
            icon_url=SLACK_ICON_URL,
            type="docker",
            image="python:3.12",
            content="python -c 'exec(open(\"script.py\").read())'",
            with_files=[
                FileSpec(name="script.py", content=script_content)
            ],
            args=args,
            env=["SLACK_API_KEY"],
            long_running=long_running
        )

def create_slack_tool(name: str, description: str, action: str, args: List[Arg], long_running: bool = False) -> SlackTool:
    return SlackTool(name, description, action, args, long_running)
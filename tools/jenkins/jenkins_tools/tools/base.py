from kubiya_sdk.tools.models import Tool

JENKINS_ICON_URL = "https://cdn-icons-png.flaticon.com/256/25/25231.png"

class JenkinsTool(Tool):
    def __init__(self, name, description, content, args, long_running=False, mermaid_diagram=None):
        env = ["JENKINS_URL", "JENKINS_USER", "JENKINS_TOKEN"]
        super().__init__(
            name=name,
            description=description,
            icon_url=JENKINS_ICON_URL,
            type="docker",
            image="python:slim",
            content=content,
            args=args,
            secrets=env,
            long_running=long_running,
            mermaid=mermaid_diagram
        )

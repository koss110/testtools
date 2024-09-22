from kubiya_sdk.tools import Arg
from .base import JenkinsTool
from kubiya_sdk.tools.registry import tool_registry


hello_world = JenkinsTool(
    name="hello_world",
    description="Hello world",
    content="""
#!/usr/bin/env python3
print('Hello world')
    """,
    args=[]
)

tool_registry.register("jenkins", hello_world)
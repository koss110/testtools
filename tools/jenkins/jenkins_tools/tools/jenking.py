from kubiya_sdk.tools import Arg
from kubiya_sdk.tools.base import JenkinsTool
from kubiya_sdk.tools.registry import tool_registry

hello_world = JenkinsTool(
    name="hello_world",
    description="A simple Hello World tool for Jenkins",
    content="""
#!/usr/bin/env python3
import sys

def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
    """,
    args=[
        Arg(
            name="name",
            type="string",
            description="Name to greet",
            required=False,
            default="World"
        )
    ]
)

tool_registry.register("jenkins", hello_world)
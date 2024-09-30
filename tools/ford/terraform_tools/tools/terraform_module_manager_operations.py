# File: terraform_module_manager_operations.py

from kubiya_sdk.tools import Arg
from .terraform_module_manager_base import TerraformModuleManager
from kubiya_sdk.tools.registry import tool_registry

# Terraform Module Manager Tool
manage_terraform_modules = TerraformModuleManager(
    name="manage_terraform_modules",
    description="Analyze GitHub repo (optionally a specific folder), update Terraform modules, run plan, create PR, and update Jira ticket",
    action="manage_modules",
    args=[
        Arg(name="github_repo", type="str", description="GitHub repository URL", required=True),
        Arg(name="repo_folder", type="str", description="Specific folder path in the repository (optional)", required=False),
        Arg(name="services_required", type="str", description="Comma-separated list of required services", required=True),
        Arg(name="jira_ticket_id", type="str", description="Jira ticket ID", required=True),
    ],
)

# Register the Terraform Module Manager tool
tool_registry.register("terraform", manage_terraform_modules)
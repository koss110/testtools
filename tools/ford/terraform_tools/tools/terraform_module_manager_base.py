# File: terraform_module_manager_base.py

from kubiya_sdk.tools.models import Tool, Arg, FileSpec
import json
import os

TERRAFORM_ICON_URL = "https://www.terraform.io/assets/images/logo-terraform-main.svg"

class TerraformModuleManager(Tool):
    def __init__(self, name, description, action, args, long_running=False, mermaid_diagram=None):
        env = ["GH_TOKEN", "JIRA_OAUTH_TOKEN"]
        
        arg_names_json = json.dumps([arg.name for arg in args])
        
        script_content = f"""
import subprocess
import sys
import os
import json
import requests
from git import Repo
from jira import JIRA

# ... (previous functions remain unchanged)

def execute_terraform_action(action, github_repo, repo_folder, services_required, jira_ticket_id, **kwargs):
    try:
        # Clone the repository
        local_path = "/tmp/repo"
        clone_repo(github_repo, local_path)
        
        # Navigate to the specified folder or use root if not specified
        working_dir = local_path
        if repo_folder:
            working_dir = os.path.join(local_path, repo_folder)
            if not os.path.exists(working_dir):
                raise Exception(f"Specified folder {{repo_folder}} does not exist in the repository")
        
        # Analyze modules and determine if task can be completed
        # This is a placeholder for the actual implementation
        can_complete_task = True
        
        if can_complete_task:
            # Update dev/main.tf file
            dev_tf_path = os.path.join(working_dir, "dev", "main.tf")
            module_code = "# Placeholder for actual module code"
            update_terraform_file(dev_tf_path, module_code)
            
            # Run terraform plan
            plan_output = run_terraform_plan(os.path.join(working_dir, "dev"))
            
            # Create pull request
            pr_title = "Update Terraform Modules"
            if repo_folder:
                pr_title += f" in {{repo_folder}}"
            create_pull_request(github_repo, f"update-terraform-modules-{{repo_folder or 'root'}}", pr_title, "Automated update of Terraform modules")
            
            # Update Jira ticket
            folder_info = f" for {{repo_folder}}" if repo_folder else ""
            update_jira_ticket(jira_ticket_id, f"Terraform plan completed successfully{{folder_info}}. Pull request created.", "last_ford_staff@example.com")
            
            return {{"status": "success", "plan_output": plan_output}}
        else:
            folder_info = f" for {{repo_folder}}" if repo_folder else ""
            update_jira_ticket(jira_ticket_id, f"Unable to complete task{{folder_info}}. Required modules not found.", "ford_staff@example.com")
            return {{"status": "failure", "reason": "Required modules not found"}}
    
    except Exception as e:
        folder_info = f" in {{repo_folder}}" if repo_folder else ""
        update_jira_ticket(jira_ticket_id, f"Error occurred{{folder_info}}: {{str(e)}}", "ford_staff@example.com")
        return {{"status": "error", "error_message": str(e)}}

if __name__ == "__main__":
    gh_token = os.environ["GH_TOKEN"]
    jira_token = os.environ["JIRA_OAUTH_TOKEN"]
    
    arg_names = {arg_names_json}
    args = {{}}
    for arg in arg_names:
        if arg in os.environ:
            args[arg] = os.environ[arg]
    
    result = execute_terraform_action("{action}", **args)
    print(json.dumps(result, indent=2))
"""
        super().__init__(
            name=name,
            description=description,
            icon_url=TERRAFORM_ICON_URL,
            type="docker",
            image="python:3.11",
            content="python /tmp/script.py",
            args=args,
            secrets=env,
            long_running=long_running,
            mermaid=mermaid_diagram,
            with_files=[
                FileSpec(
                    destination="/tmp/script.py",
                    content=script_content,
                )
            ],
        )
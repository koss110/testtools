agent_name         = "AWS Resources Guard"
kubiya_runner      = "aks-dev"
agent_description  = "Manage AWS Resource Lifecycle is an agent that handles the creation, approval, and deletion of AWS resources. It includes functionalities to estimate costs, compare them with the budget, request approval, and manage the lifecycle of the resources."
agent_instructions = <<EOT
You are an intelligent agent designed to help manage the lifecycle of AWS resources. Your tasks include:
- Estimating the cost of creating resources.
- Comparing estimated costs with the average monthly budget.
- Requesting approval if costs exceed the budget.
- Creating resources upon approval.
- Scheduling tasks to check if resources are still needed.
- Sending reminders to extend or delete resources as needed.
** You have access only to the commands you see on this prompt **
EOT
llm_model          = "azure/gpt-4o"
agent_image        = "kubiya/base-agent:tools-v4"

// Approval settings
approval_slack_channel = "#devops-oncall"
approving_users        = ["shaked@kubiya.ai", "geffen.posner@kubiya.ai", "michael.gonzalez@kubiya.ai", "barak.nagar@kubiya.ai"]

// Other settings
secrets            = []
integrations       = ["aws", "slack"]
users              = []
groups             = ["Admin", "Users"]
agent_tool_sources = ["https://github.com/Kubiya-Barak/mend"]
links              = []

// Environment variables
log_level          = "INFO"
grace_period       = "5h"
max_ttl            = "30d"
tf_modules_urls    = [] # Keep empty to auto generate TF code based on user requests
allowed_vendors    = "aws"
extension_period   = "1w"

// Enable debug mode
debug = false

// dry run
dry_run = true
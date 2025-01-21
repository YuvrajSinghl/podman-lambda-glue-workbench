
Here's a README file for your Podman Lambda Glue Workbench project:

📌 Podman Lambda Glue Workbench
A lightweight and efficient development environment for running AWS Lambda and AWS Glue jobs locally using Podman. This setup enables seamless testing and debugging of serverless applications directly within VS Code.

🚀 Features & Benefits
✅ Local AWS Glue & Lambda Execution – Run jobs without deploying to AWS.
✅ Practical - Connect seamlessly with existing AWS resources like S3, SecretManager etc.
✅ Podman-Based Isolation – No need for Docker; fully supports rootless containers.
✅ VS Code Integration – Develop, test, and iterate seamlessly.
✅ Preloaded Dependencies – Comes with necessary AWS libraries.
✅ Fast Development Workflow – Avoids frequent container rebuilds.

🛠 Prerequisites
Before setting up the project, ensure you have the following installed:
Podman
AWS CLI (Configured with your AWS credentials)
VS Code with:
Python Extension (for AWS Glue jobs)
Remote Explorer (Microsoft)
WSL (Microsoft)

🔧 Setup Instructions
Clone the Repository
git clone https://github.com/YuvrajSinghl/podman-lambda-glue-workbench.git

Step-1 Open VS Code
Step-2 Go to Remote Explorer -> Select Target as WSL Targets -> Under WSL Targets connect to **podman-machine-default**, this will open a new VS code window.
Step-3 In this new window open this cloned repo.
Step-4 Configure AWS credential in ".aws" file so Glue and Lambda could connect to live aws services, and update code as desired.
Step-5 To run glue or lambda, Press CTRL+SHIFT+P and under tasks select "Run Glue Job" or Run Lambda Function"

⚠️_If you are running this code for the first time make sure you build image for desired service. It could be done by 'Run Task'_

🎯 Use Cases
Develop AWS Glue ETL scripts in a controlled local environment.
Test AWS Lambda functions without deploying them.
Debug data pipelines efficiently.
Enhance workflow for AWS-related development using Podman.
🏆 Contributing
Feel free to fork the repository, create a branch, and submit a pull request. Contributions are welcome!

📜 License
This project is licensed under the MIT License.



# Complete Developer Environment Setup Guide

This guide covers the essential setup steps for AWS, Git/GitHub, IDEs, and Python development.

---

## **Setup Script**

Follow these steps sequentially for a smooth setup.

### 1. **AWS Setup**
#### Create an AWS Account
- Visit [AWS Sign-Up](https://aws.amazon.com/) and create an account.
- Complete email verification, payment method setup, and phone verification.

#### Configure IAM User
```bash
# Log in to AWS Management Console → IAM → Users → Create User
# Select "Programmatic Access" and attach "AdministratorAccess" policy.
```
- Save your **Access Key ID** and **Secret Access Key**.

#### Install and Configure AWS CLI
```bash
# Install AWS CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Verify installation
aws --version

# Configure AWS CLI
aws configure
# Enter Access Key, Secret Key, default region (e.g., us-east-1), and output format (e.g., json).
```

---

### 2. **Git & GitHub Setup**
#### Install Git
```bash
# On macOS (using Homebrew)
brew install git

# On Linux (Debian/Ubuntu)
sudo apt-get update && sudo apt-get install git

# On Windows
# Download Git from https://git-scm.com/ and install.
```

#### Configure Git
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

#### Set Up SSH Key
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Start the SSH agent and add your key
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copy the SSH key to GitHub
cat ~/.ssh/id_ed25519.pub
# Add the key to GitHub → Settings → SSH and GPG Keys → New SSH Key.
```

#### Test SSH Connection
```bash
ssh -T git@github.com
```

---

### 3. **Install IDEs**
#### Visual Studio Code
```bash
# Download VS Code: https://code.visualstudio.com/
# Install Python extension from the Extensions menu (Ctrl+Shift+X).
```

#### PyCharm
```bash
# Download PyCharm: https://www.jetbrains.com/pycharm/
# Choose Community (Free) or Professional (Paid).
```

#### Jupyter Notebook
```bash
pip install notebook
jupyter notebook  # Launches in a browser.
```

---

### 4. **Python, Pip, and Pipenv Setup**
#### Install Python
```bash
# On macOS/Linux
python3 --version  # Verify if Python is already installed.

# On Windows
# Download Python from https://www.python.org/ and check "Add Python to PATH" during installation.

# Verify installation
python --version
```

#### Install Pip
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

#### Install Pipenv (Virtual Environment Manager)
```bash
pip install pipenv
pipenv install && pipenv shell  # Create and activate a virtual environment.
pipenv install requests         # Example: Install a package.
```

---

### 5. **Workflow Summary**
- **AWS**: Set up IAM user, CLI, and credentials.
- **Git/GitHub**: Configure Git, SSH, and connect repositories.
- **IDE**: Use VS Code, PyCharm, or Jupyter Notebook for coding.
- **Python**: Use Pipenv for managing dependencies.

#### Start a Project
```bash
# Clone a GitHub repository
git clone git@github.com:username/repo.git

# Open project in VS Code
code .
```

---

# BraveAIWebSearch 🔍🤖

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful AI-powered web search tool built with Python. Leverages modern libraries to deliver efficient and intelligent search capabilities.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features ✨
- AI-enhanced web search capabilities
- Secure environment variable management
- Pydantic data validation
- Asynchronous HTTP requests
- Easy-to-use command line interface

## Installation 💻

### Prerequisites
- Python 3.8+
- pip package manager

### Setup Instructions
```bash
# Clone the repository
git clone https://github.com/your-username/BraveAIWebSearch.git

# Navigate to project directory
cd BraveAIWebSearch

# Install dependencies
pip install -r requirements.txt
```

> **Tip**: Consider using a virtual environment:
> ```bash
> python -m venv venv
> source venv/bin/activate  # Linux/MacOS
> .\venv\Scripts\activate  # Windows
> ```

## Usage 🚀

### Basic Execution
```bash
python agent.py
```

### Configuration
Create a `.env` file in the project root with your credentials:
```env
OPENAI_API_KEY=your_api_key_here
BRAVE_API_KEY=your_brave_api_key
# Add other required environment variables
```

## Dependencies 📦

| Package | Version | Purpose |
|---------|---------|---------|
| httpx | ^0.24.0 | Async HTTP client |
| pydantic-ai | ^1.0.0 | AI integration |
| python-dotenv | ^1.0.0 | Environment management |
| python-magic | ^0.4.27 | File type detection |

Install all dependencies with:
```bash
pip install -r requirements.txt
```

## Contributing 🤝

I welcome contributions! Please follow these steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Disclaimer**: This project is not affiliated with Brave Software or OpenAI.

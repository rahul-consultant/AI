# Eazee: Voice-Driven E-Visa Assistant for the Visually Impaired

## Overview
Eazee is an innovative application designed to assist visually impaired individuals in filling out their visa applications through voice commands. The application leverages advanced AI technologies, including speech recognition and text-to-speech, to provide a seamless user experience.

## Features
- Voice-driven interaction for filling out visa applications.
- Automatic photo capture for visa application forms.
- PDF generation for completed visa applications.
- Integration with OpenAI's API for intelligent responses and assistance.

## Project Structure
```
evisa-visual-impaired
├── src
│   ├── main.py          # Entry point of the application
│   ├── utils            # Utility functions for various functionalities
│   │   ├── audio.py     # Audio processing functions
│   │   ├── pdf.py       # PDF generation functions
│   │   ├── photo.py     # Image capture functions
│   │   └── openai_api.py # OpenAI API interaction functions
│   └── types            # Type definitions for the application
│       └── index.py     # Data types and structures
├── requirements.txt      # Project dependencies
├── .env.example          # Environment variable template
├── .vscode               # IDE configuration files
│   ├── launch.json       # Debugging configuration
│   └── settings.json     # Project-specific settings
└── README.md             # Project documentation
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd evisa-visual-impaired
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Copy `.env.example` to `.env` and fill in the necessary API keys and configurations.

## Usage
1. Run the application:
   ```
   python src/main.py
   ```

2. Follow the voice prompts to fill out your visa application.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
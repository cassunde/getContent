# Daily News Digest

This application is designed to fetch news content from specified URLs, summarize it using the Google Gemini API, and then send the summarized news digest via email. It can be configured to fetch daily news or specific tech-related news.

## Features

- **Content Extraction**: Uses Jina AI to extract clean content from web pages.
- **AI Summarization**: Leverages Google Gemini 1.5 Flash to generate concise summaries of the extracted content.
- **Email Delivery**: Sends the summarized news digest to a specified recipient via SMTP.
- **Configurable News Sources**: Easily switch between daily news sources and tech-specific news sources.
- **Environment Variable Support**: Securely manage API keys and email credentials using environment variables.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker (recommended for easy setup)
- Python 3.9+ (if running directly without Docker)

### Installation

#### Using Docker (Recommended)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mattheuscassunde/getContent.git
   cd getContent
   ```

2. **Create a `.env` file:**
   Create a file named `.env` in the root directory of the project and add your environment variables. This file will be automatically loaded by the `dotenv` library.

   ```
   GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
   JINA_API_KEY="YOUR_JINA_API_KEY"
   SENDER_EMAIL="your_email@example.com"
   SENDER_PASSWORD="your_email_password"
   RECIPIENT_EMAIL="recipient_email@example.com"
   SMTP_SERVER="your_smtp_server"
   SMTP_PORT="your_smtp_port"
   
# AI-Powered WhatsApp Chatbot (Bangla & English)

A smart, AI-powered WhatsApp chatbot that supports both **Bangla & English**, providing **AI-generated responses** as well as **keyword-based replies**. This bot can handle general inquiries, automate tasks, and provide intelligent conversations.

## Features
✅ **AI-Powered Responses** using OpenAI/GPT models  
✅ **Keyword-Based Replies** for predefined commands  
✅ **Multi-Language Support** (Bangla & English)  
✅ **WhatsApp Integration** using Twilio API  
✅ **Customizable & Scalable**  
✅ **Runs on Python & Flask**

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/mdzubayerhossain/whatsapp-chatbot.git
cd whatsapp-chatbot
```

### 2. Install Dependencies
Make sure you have Python installed. Then, run:
```sh
pip install -r requirements.txt
```

### 3. Set Up Twilio API
- Sign up on [Twilio](https://www.twilio.com/) and get **SID, Auth Token, and WhatsApp number**.
- Create a `.env` file and add your Twilio credentials:
```sh
TWILIO_ACCOUNT_SID=your_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_WHATSAPP_NUMBER=your_twilio_whatsapp_number
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Run the Bot
```sh
python app.py
```

## How It Works
1. Users send messages to the WhatsApp bot.
2. If a **keyword** matches, the bot replies with a predefined response.
3. If no keyword matches, it uses **AI (GPT) to generate responses**.
4. The bot supports both **Bangla & English** messages automatically.

## Example Commands
| Command | Response |
|---------|----------|
| `help` | Shows available commands |
| `news` | Fetches the latest news |
| `joke` | Tells a funny joke |
| `weather Dhaka` | Provides current weather in Dhaka |
| `who are you?` | AI-generated introduction |

## Contributing
We welcome contributions! Feel free to open issues or submit PRs.

## License
This project is licensed under the MIT License.

## Contact
📧 Email: mdzubayerhossainpatowari  
⭐ GitHub: [https://github.com/yourusername/whatsapp-chatbot](https://github.com/mdzubayerhossain/whatsapp-chatbot)

🚀 **Star this repo if you find it useful!** ⭐


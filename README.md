AI-Powered WhatsApp Chatbot (Bangla & English)
'
A smart, AI-powered WhatsApp chatbot that supports both Bangla & English, providing AI-generated responses
as well as keyword-based replies. This bot can handle general inquiries, automate tasks, and provide intelligent conversations.
'
Features:
- AI-Powered Responses using OpenAI/GPT models
- Keyword-Based Replies for predefined commands
- Multi-Language Support (Bangla & English)
- WhatsApp Integration using Twilio API
- Customizable & Scalable
- Runs on Python & Flask
'
Installation:
'
1. Clone the Repository:
Clone this repository to your local machine:
```sh
git clone https://github.com/mdzubayerhossain/whatsapp-chatbot.git
cd whatsapp-chatbot
```
'
2. Install Backend Dependencies:
Make sure you have Python installed, then run:
```sh
pip install -r requirements.txt
```
'
3. Set Up Twilio API:
Sign up on Twilio and get your SID, Auth Token, and WhatsApp number.
Create a .env file in the root directory and add your Twilio credentials:
```env
TWILIO_ACCOUNT_SID=your_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_WHATSAPP_NUMBER=your_twilio_whatsapp_number
OPENAI_API_KEY=your_openai_api_key_here
```
'
4. Run the Backend:
Run the backend application:
```sh
python app.py
```
The backend should now be running on http://localhost:5000.
'
Frontend Setup (React):
This section covers setting up the frontend of the AI-powered WhatsApp chatbot, where users can interact with the bot.
'
1. Clone the Frontend Repository:
```sh
git clone https://github.com/yourusername/whatsapp-chatbot-frontend.git
cd whatsapp-chatbot-frontend
```
'
2. Install Frontend Dependencies:
Run the following command to install necessary packages:
```sh
npm install
```
'
3. Set Up Proxy for API Requests:
To avoid issues with CORS in development, set up a proxy in the src/setupProxy.js file for API requests to the Flask backend:
```js
const { createProxyMiddleware } = require('http-proxy-middleware');
'
module.exports = function (app) {
  app.use(
    '/webhook',
    createProxyMiddleware({
      target: 'http://localhost:5000',
      changeOrigin: true,
    })
  );
};
```
'
4. Start the Frontend Application:
After installation, run the React app:
```sh
npm start
```
The frontend will be available at http://localhost:3000.
'
How It Works:
Users send messages to the WhatsApp bot.
If a keyword matches, the bot replies with a predefined response.
If no keyword matches, it uses AI (GPT) to generate responses.
The bot supports both Bangla & English messages automatically.
'
Example Commands:
Command       Response
help          Shows available commands
news          Fetches the latest news
joke          Tells a funny joke
weather Dhaka Provides current weather in Dhaka
who are you?  AI-generated introduction
'
Contributing:
We welcome contributions! Feel free to open issues or submit pull requests. To contribute:
- Fork this repository
- Create a feature branch
- Commit your changes
- Push to your branch
- Create a pull request
'
License:
This project is licensed under the MIT License.
'
Contact:
📧 Email: mdzubayerhossainpatowari@gmail.com
⭐ GitHub: https://github.com/mdzubayerhossain/whatsapp-chatbot
'
🚀 Star this repo if you find it useful! ⭐
'
Key Sections in the README.md:
- Features: Highlights the functionality of the WhatsApp chatbot.
- Installation Instructions: Step-by-step guide to set up both the backend and frontend.
- How It Works: Explains the workflow of the chatbot and how it processes messages.
- Example Commands: Provides users with examples of commands they can send to the bot.
- Contributing: Guides potential contributors on how to get involved.
- License & Contact: Provides license information and contact details for project maintainers.
'
This should give users all the necessary details to set up, run, and contribute to your AI-powered WhatsApp chatbot.

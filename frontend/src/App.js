import React, { useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [userMessage, setUserMessage] = useState('');
  const [chatHistory, setChatHistory] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleMessageChange = (e) => {
    setUserMessage(e.target.value);
  };

  const handleSendMessage = async () => {
    if (!userMessage) return;

    // Add user message to the chat history
    const newChatHistory = [...chatHistory, { sender: 'user', message: userMessage }];
    setChatHistory(newChatHistory);
    setUserMessage('');
    setLoading(true);

    try {
      // Send message to the backend and get response
      const response = await axios.post('http://localhost:5000/webhook', { message: userMessage });
      
      // Add bot response to the chat history
      const botResponse = response.data.message;
      setChatHistory([...newChatHistory, { sender: 'bot', message: botResponse }]);
    } catch (error) {
      console.error('Error sending message:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>AI-Powered WhatsApp Chatbot</h1>
        <div className="chat-window">
          {chatHistory.map((chat, index) => (
            <div key={index} className={`message ${chat.sender}`}>
              <span>{chat.message}</span>
            </div>
          ))}
          {loading && <div className="loading">Bot is typing...</div>}
        </div>
        <div className="input-container">
          <input
            type="text"
            value={userMessage}
            onChange={handleMessageChange}
            placeholder="Type a message..."
          />
          <button onClick={handleSendMessage}>Send</button>
        </div>
      </header>
    </div>
  );
}

export default App;

import React, { useState } from 'react';

import './App.css';




import { MessageWindow } from './components/MessageWindow'; 
import { MessageInput } from './components/MessageInput';


export interface  Message {
  role: 'user' | 'bot'
  text: string
}
export default function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [results, setResults] = useState<string[]>([]);


  const [query, setQuery] = useState('');
  const [method, setMethod] = useState('keyword');
  
  const handleSearch = async (text: string) => {

    setMessages(ms => [...ms, {role: 'user', text}]);
    setLoading(true);
    

    try {
      const url = new URL('http://localhost:8000/search');
      url.searchParams.append('query', query);
      url.searchParams.append('method', method);
      const res = await fetch(url.toString());

      if (!res.ok) {
        throw new Error('Network response error');
      }

      const response = await res.json();

      setResults(response.data);
    } catch (err) {
      console.error('Search failed:', err);
      setResults([]);
    }
    setLoading(false);
  };

  return (
    <div className="chat-ui">
      <header className="header">ThreadWise</header>
      <MessageWindow messages={messages} loading={loading} />
      <MessageInput onSearch={handleSearch} disabled={loading} />
    </div>
  );
}
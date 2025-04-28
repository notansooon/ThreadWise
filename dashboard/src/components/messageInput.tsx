import React from 'react';
import { useState } from 'react';





export const MessageInput = () => {


    const [text, setText] = useState('');
    const [disabled, setDisabled] = useState(false);



    
    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (!text.trim()) return; // Prevent empty submissions
    ]

        
    
    
    
    
    
    return (
        <>

<form onSubmit={handleSubmit} className="input-form">
      <input
        className="input-text"
        value={text}
        onChange={({ target: { value } }) => setText(value)}
        disabled={disabled}
        placeholder="Type a message..."
      />
      <button
        type="submit"
        className="send-button"
        disabled={disabled}
      >
        Send
      </button>
    </form>

        
        
        </>
    )






}






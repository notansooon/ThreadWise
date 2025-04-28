import React from 'react';
import { useState } from 'react';





export const MessageInput = () => {


    const [text, setText] = useState('');
    const [disabled, setDisabled] = useState(false);



    
    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (!text.trim()) return; 
        setText('');
    }


    
    
    return (
        <>

      <form onSubmit={handleSubmit} className="input-form">
            <input
              className="input-text"
              value={text}
              onChange={(e) => setText(e.target.value)}
              
              placeholder="Type a message..."
            />
            <button
              type="submit"
              className="send-button"
              
            >
              Send
            </button>
          </form>

        
        
        </>
    )

  }






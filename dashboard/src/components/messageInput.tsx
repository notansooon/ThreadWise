import React from 'react';
import { useState } from 'react';
import '../App.css';




interface MessageInputProps {
    
    onSearch?: (message: string) => void;
    disabled?: boolean;
}



export const MessageInput: React.FC<MessageInputProps> = ({onSearch, disabled = false}) => {


    const [text, setText] = useState('');
    
   
    const handleSearch = (e: React.FormEvent) => {
      e.preventDefault();
      if (onSearch) {
        onSearch(text);
        setText(''); // Clear the input after sending
      }
        

    }
    
    
    return (
        <>

      <form onSubmit={handleSearch} className="input-form">
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








import '../App.css';
import React from "react";
import type { Message } from '../App';



interface MessageWindowProps { 
    messages: Message[];
    loading: boolean;



}

export const MessageWindow: React.FC<MessageWindowProps> = ({ messages, loading }) => {
    return (
        <div className="message-list">
            {messages.map((message, index) => (
                <div key={index} className="message">
                    {message.text}
                </div>
            ))}
            {loading && <div className="loading">Loading...</div>}
        </div>
    );
};

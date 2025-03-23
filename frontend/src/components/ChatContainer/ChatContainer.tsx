"use client";

import React, { useState } from "react";
import MessageItem from "../MessageItem/MessageItem";
import ChatInput from "../ChatInput/ChatInput";
import { ScrollArea } from "@/components/ui/scroll-area";

const ChatContainer: React.FC = () => {
  const [messages, setMessages] = useState<{ message: string; isUser: boolean }[]>([]);

  const addMessage = (message: string, isUser: boolean) => {
    setMessages((prev) => [...prev, { message, isUser }]);
  };

  return (
    <div className="flex flex-col h-[600px] max-w-xl mx-auto border rounded-lg shadow-lg">
      <ScrollArea className="flex-1 p-4 overflow-y-auto">
        {messages.length === 0 ? (
          <p className="text-center text-gray-500">No messages yet.</p>
        ) : (
          messages.map((msg, index) => (
            <MessageItem key={index} message={msg.message} isUser={msg.isUser} />
          ))
        )}
      </ScrollArea>
      <ChatInput onSendMessage={addMessage} />
    </div>
  );
};

export default ChatContainer;

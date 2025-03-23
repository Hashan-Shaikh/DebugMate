import React from "react";
import { cn } from "@/lib/utils";
import { Card } from "@/components/ui/card";

interface MessageItemProps {
  message: string;
  isUser: boolean;
}

const MessageItem: React.FC<MessageItemProps> = ({ message, isUser }) => {
  return (
    <div className={cn("flex", isUser ? "justify-end" : "justify-start")}>
      <Card
        className={cn(
          "p-3 max-w-lg rounded-lg shadow-md",
          isUser ? "bg-blue-500 text-white" : "bg-gray-100 text-black"
        )}
      >
        {JSON.stringify(message)}
      </Card>
    </div>
  );
};

export default MessageItem;

import React from "react";
import ReactMarkdown from "react-markdown";
import rehypeHighlight from "rehype-highlight";
import "highlight.js/styles/github-dark.css"; // Syntax highlighting style
import { cn } from "@/lib/utils";
import { Card } from "@/components/ui/card";

interface MessageItemProps {
  message: string;
  isUser: boolean;
}

const MessageItem: React.FC<MessageItemProps> = ({ message, isUser }) => {
  return (
    <div className={cn("flex", isUser ? "justify-end" : "justify-start", "mt-2")}>
      <Card
        className={cn(
          "p-3 max-w-lg rounded-lg shadow-md",
          isUser ? "bg-blue-500 text-white" : "bg-gray-100 text-black"
        )}
      >
        <ReactMarkdown rehypePlugins={[rehypeHighlight]}>{message}</ReactMarkdown>
      </Card>
    </div>
  );
};

export default MessageItem;

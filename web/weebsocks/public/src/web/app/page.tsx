"use client";

import ChatBubble from "@/components/ChatBubble";
import { useEffect, useRef, useState } from "react";

type Message = {
  message: string,
  sender?: string,
  sent?: boolean
}

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [newMessage, setNewMessage] = useState("");
  const [ws, setWs] = useState<WebSocket>();
  const chatBox = useRef<HTMLDivElement>(null);

  const sendMessage = (ws: WebSocket | undefined, message: string) => {
    ws?.send(JSON.stringify({ message: message, sender: "user" }));
  }

  const scrollChat = () => {
    chatBox.current?.scrollTo({ top: chatBox.current?.scrollHeight, behavior: "smooth" });
  }

  const handleKeyDown = (ws: WebSocket | undefined, message: string) => (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter" && message) {
      setMessages((prevMessages) => [...prevMessages, { message: message, sent: true }]);
      sendMessage(ws, message);
      setNewMessage("");
    }
  }

  useEffect(() => {
    fetch("/api/token/generate")
      .then((res) => res.json())
      .then((data) => {
        const ws = new WebSocket("/api/ws?token=" + data.data);
        setWs(ws);

        ws.onmessage = (event) => {
          const message: Message = JSON.parse(event.data);
          setMessages((prevMessages) => [...prevMessages, message]);
        };
      });
  }, []);

  useEffect(() => {
    scrollChat();
  }, [messages]);
  return (
    <div className="flex flex-col justify-between bg-neutral-900 p-8 w-1/2 rounded-xl">
      <div className="flex flex-col gap-4 overflow-y-scroll" ref={chatBox}>
        {messages.map((message, index) => (
          <ChatBubble key={index} message={message.message} sender={message.sender} sent={message.sent} />
        ))}
      </div>
      <div className="flex pt-8">
        <input type="text" placeholder="Message" value={newMessage} className="bg-neutral-800 rounded-xl p-4 w-full flex-1 focus:outline-none" onChange={(e) => setNewMessage(e.target.value)} onKeyDown={handleKeyDown(ws, newMessage)} />
      </div>
    </div>
  );
}

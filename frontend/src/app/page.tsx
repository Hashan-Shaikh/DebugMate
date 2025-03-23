import ChatContainer from "../components/ChatContainer/ChatContainer";
import Navbar from "../components/NavBar/NavBar";

export default function Home() {
  return (
    <div className="flex flex-col h-screen bg-gray-50">
      <Navbar />
      <div className="flex flex-1 items-center justify-center">
        <ChatContainer />
      </div>
    </div>
  );
}

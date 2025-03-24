import axios from "axios";

const API_BASE_URL = "http://localhost:8000"; // Replace with your FastAPI URL

export const sendMessageToAPI = async (query: string) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/chat`, {
      params: { query }, // Sending message as a query parameter
    });
    return response.data.result; // Assuming FastAPI returns { reply: "AI response" }
  } catch (error) {
    console.error("API Error:", error);
    return "Error fetching response from AI.";
  }
};

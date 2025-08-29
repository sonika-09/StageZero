import axios from "axios";

const BASE_URL = "http://localhost:8000"; // Backend server

export const fetchClassifiedLogs = async () => {
  try {
    const res = await axios.get(`${BASE_URL}/classify`);
    return res.data;
  } catch (error) {
    console.error("Error fetching classified logs:", error);
    throw error;
  }
};

export const loadLogs = async () => {
  try {
    const res = await axios.get(`${BASE_URL}/load_logs`);
    return res.data;
  } catch (error) {
    console.error("Error loading logs:", error);
    throw error;
  }
};

export const classifyLogs = async () => {
  try {
    const res = await axios.get(`${BASE_URL}/classify_logs`);
    return res.data;
  } catch (error) {
    console.error("Error classifying logs:", error);
    throw error;
  }
};

export const sendToWatsonx = async () => {
  try {
    const res = await axios.get(`${BASE_URL}/send_to_watsonx`);
    return res.data;
  } catch (error) {
    console.error("Error sending to Watsonx:", error);
    throw error;
  }
};

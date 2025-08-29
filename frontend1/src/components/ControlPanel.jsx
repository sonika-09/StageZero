import React from "react";

const ControlPanel = ({ onLoad, onClassify, onSend }) => {
  return (
    <div className="flex gap-4 my-4">
      <button className="bg-blue-500 text-white px-4 py-2 rounded" onClick={onLoad}>
        Load Logs
      </button>
      <button className="bg-green-500 text-white px-4 py-2 rounded" onClick={onClassify}>
        Classify Logs
      </button>
      <button className="bg-purple-500 text-white px-4 py-2 rounded" onClick={onSend}>
        Send to Watsonx
      </button>
    </div>
  );
};

export default ControlPanel;

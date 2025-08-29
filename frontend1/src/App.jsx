import React, { useState, useEffect } from "react";
import LogTable from "./components/LogTable";
import ClassifiedTable from "./components/ClassifiedTable";
import ControlPanel from "./components/ControlPanel";
import { fetchClassifiedLogs, loadLogs, classifyLogs, sendToWatsonx } from "./api/api";

const App = () => {
  const [logs, setLogs] = useState([]);
  const [classifiedLogs, setClassifiedLogs] = useState([]);

  const handleLoadLogs = async () => {
    const data = await loadLogs();
    setLogs(data.all_logs_file ? require(data.all_logs_file) : []);
  };

  const handleClassifyLogs = async () => {
    await classifyLogs();
    const data = await fetchClassifiedLogs();
    setClassifiedLogs(data);
  };

  const handleSendToWatsonx = async () => {
    const res = await sendToWatsonx();
    alert(JSON.stringify(res, null, 2));
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Hackverse Log Dashboard</h1>
      <ControlPanel
        onLoad={handleLoadLogs}
        onClassify={handleClassifyLogs}
        onSend={handleSendToWatsonx}
      />
      <h2 className="text-xl mt-4 mb-2">All Logs</h2>
      <LogTable logs={logs} />
      <h2 className="text-xl mt-4 mb-2">Classified Logs</h2>
      <ClassifiedTable logs={classifiedLogs} />
    </div>
  );
};

export default App;

import React from "react";

const ClassifiedTable = ({ logs }) => {
  return (
    <table className="min-w-full border border-gray-300">
      <thead>
        <tr>
          <th className="border px-4 py-2">Filename</th>
          <th className="border px-4 py-2">Text</th>
          <th className="border px-4 py-2">Matched Techniques</th>
        </tr>
      </thead>
      <tbody>
        {logs.map((log, idx) => (
          <tr key={idx}>
            <td className="border px-4 py-2">{log.filename}</td>
            <td className="border px-4 py-2">{log.text}</td>
            <td className="border px-4 py-2">{log.matched_techniques.join(", ")}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default ClassifiedTable;

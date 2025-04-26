import React from 'react';

interface Result {
  id: string;
  content: string;
  time: string;
}

interface ResultsListProps {
  results: Result[];
}

export const ResultsList: React.FC<ResultsListProps> = ({ results }) => {
  if (results.length === 0) {
    return <p className="text-center text-gray-600">No results yet. Try searching above.</p>;
  }
  
  return (
    <div className="bg-white rounded-xl shadow p-4">
      <h2 className="text-xl font-semibold mb-4">Results</h2>
      <ul className="space-y-2">
        {results.map((item) => (
          <li key={item.id} className="border-b py-2">
            <p className="text-sm text-gray-600">{item.time}</p>
            <p className="text-lg">{item.content}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};
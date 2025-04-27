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
    return <p>No results yet. Try searching above.</p>;
  }
  
  return (
    <div>
      <h2>Results</h2>
      <ul>
        {results.map((item) => (
          <li key={item.id}>
            <p>{item.time}</p>
            <p>{item.content}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};
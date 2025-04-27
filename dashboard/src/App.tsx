import React, { useState } from 'react';

import { SearchBox } from './components/SearchBox';
import { ResultsList } from './components/ResultsList'; 

export default function App() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [method, setMethod] = useState('keyword');
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    setLoading(true);
    try {
      const url = new URL('http://localhost:8000/search');
      url.searchParams.append('query', query);
      url.searchParams.append('method', method);
      const res = await fetch(url.toString());

      if (!res.ok) {
        throw new Error('Network response error');
      }

      const response = await res.json();

      setResults(response.data);
    } catch (err) {
      console.error('Search failed:', err);
      setResults([]);
    }
    setLoading(false);
  };

  return (
    <div>
      <h1>🧠 ThreadWise Memory Search</h1>
      <SearchBox
        query={query}
        setQuery={setQuery}
        method={method}
        setMethod={setMethod}
        onSearch={handleSearch}
        loading={loading}
      />
      <div>
        <ResultsList results={results} />
      </div>
    </div>
  );
}
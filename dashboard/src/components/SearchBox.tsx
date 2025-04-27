import React from 'react';

interface SearchBoxProps {
  query: string;
  setQuery: (value: string) => void;
  method: string;
  setMethod: (value: string) => void;
  onSearch: () => void;
  loading: boolean;
}

export const SearchBox: React.FC<SearchBoxProps> = ({
  query,
  setQuery,
  method,
  setMethod,
  onSearch,
  loading,
}) => {
  return (
    <div>
      <input
        type="text"
        placeholder="Ask a question..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />

      <select
        value={method}
        onChange={(e) => setMethod(e.target.value)}
      >
        <option value="keyword">Keyword Search</option>
        <option value="semantic">Semantic Search</option>
      </select>

      <button
        onClick={onSearch}
        disabled={loading}
      >
        {loading ? 'Searching...' : 'Search'}
      </button>
    </div>
  );
};
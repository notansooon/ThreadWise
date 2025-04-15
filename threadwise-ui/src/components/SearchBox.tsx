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
    <div className="bg-white shadow-md rounded-xl p-4 max-w-2xl mx-auto">
      <input
        type="text"
        className="w-full p-2 border border-gray-300 rounded mb-4"
        placeholder="Ask a question..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />

      <select
        className="w-full p-2 mb-4 border border-gray-300 rounded"
        value={method}
        onChange={(e) => setMethod(e.target.value)}
      >
        <option value="keyword">Keyword Search</option>
        <option value="semantic">Semantic Search</option>
      </select>

      <button
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        onClick={onSearch}
        disabled={loading}
      >
        {loading ? 'Searching...' : 'Search'}
      </button>
    </div>
  );
};
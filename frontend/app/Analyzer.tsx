"use client";

import { useState } from "react";

type Result = {
  accuracy: number;
  result: "positive";
  inputText: string;
};

const mockFetchResult = (inputText: string) => {
  let timeoutId: ReturnType<typeof setTimeout>;
  return new Promise<Result>((resolve) => {
    timeoutId = setTimeout(() => {
      resolve({
        result: "positive",
        accuracy: Math.random(),
        inputText,
      });
      clearTimeout(timeoutId);
    }, 3000);
  });
};

export const Analyzer = () => {
  const [isFetchingResult, setIsFetchingResult] = useState(false);
  const [inputText, setInputText] = useState("");
  const [error, setError] = useState("");

  const [result, setResult] = useState<Result | null>(null);

  return (
    <div className="flex my-10 flex-col ">
      <label className="text-lg">Enter your input text:</label>
      <textarea
        className=" border border-gray-700 min-h-[200px] p-4 mt-2 mb-6 disabled:cursor-not-allowed"
        title={isFetchingResult ? "Fetching results..." : ""}
        onChange={(e) => {
          setError("");
          setResult(null);
          setInputText(e.target.value.trim());
        }}
        autoFocus
        disabled={isFetchingResult}
      />

      <button
        type="button"
        className=" hover:bg-black self-start text-gray-200 hover:text-white p-2  bg-gray-800 cursor-pointer rounded-md disabled:cursor-not-allowed disabled:hover:bg-slate-500"
        disabled={isFetchingResult}
        title={isFetchingResult ? "Fetching results..." : ""}
        onClick={() => {
          if (!inputText) {
            setError("Input text is required.");
            return;
          } else {
            setIsFetchingResult(true);
            setResult(null);
            setError("");
            mockFetchResult(inputText)
              .then((result) => {
                setResult(result);
              })
              .finally(() => setIsFetchingResult(false));
          }
        }}
      >
        Analyze Sentiment
      </button>

      {error && (
        <div className="my-6">
          <div className=" underline font-bold underline-offset-4 text-red-500 mb-2">
            ERROR:
          </div>
          <p className=" text-gray-500">{error}</p>
        </div>
      )}

      {result && (
        <div className="my-6">
          <div className=" underline font-bold underline-offset-4 text-blue-500 mb-2">
            RESULT:
          </div>
          <pre className=" text-gray-800">
            {JSON.stringify(result, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
};

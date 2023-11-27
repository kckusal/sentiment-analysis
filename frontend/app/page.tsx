import Image from "next/image";
import { Analyzer } from "./Analyzer";

export default function Home() {
  return (
    <main className=" p-24 grid grid-cols-1 ">
      <h1 className=" font-extrabold text-3xl">
        Welcome to Sentiment Analyzer!
      </h1>
      <p className=" text-lg text-slate-500">
        This tool lets you enter a text and returns a sentiment analysis result,
        classifying the text input to be <strong>positive</strong> or{" "}
        <strong>negative</strong>.
      </p>

      <Analyzer />
    </main>
  );
}

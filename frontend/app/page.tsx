import Image from "next/image";
import { Analyzer } from "./Analyzer";

export default function Home() {
  return (
    <main className=" p-4 md:p-8 lg:p-16 xl:p-24 grid grid-cols-1 ">
      <h1 className=" font-extrabold text-2xl md:text-3xl">
        Welcome to Sentiment Analyzer!
      </h1>
      <p className=" text-lg text-slate-500">
        This tool lets you enter a text and returns a sentiment analysis result,
        classifying the text input to be <strong>positive</strong> or{" "}
        <strong>negative</strong>.
      </p>

      <div>
        <p className=" mt-8 font-semibold">
          Try these examples (taken randomly from Amazon products site):
        </p>
        <ul className=" pl-4 list-inside list-disc text-sm text-gray-600">
          <li>
            This was a good product. The person it was bought for loved it. Got
            lots of use out of it.
          </li>
          <li>
            I returned above item because it doesn&apos;t work with me MacBook
            Pro. I have not received my refund yet. Please double check why my
            refund takes so long. Thank you.
          </li>
        </ul>
      </div>

      <Analyzer />
    </main>
  );
}

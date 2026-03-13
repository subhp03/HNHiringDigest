export default function ThankYouPage() {
  return (
    <main className="min-h-screen flex items-center justify-center px-4">
      <div className="w-full max-w-2xl min-h-[25vh] rounded-2xl border border-white/10 bg-black/60 backdrop-blur-md px-10 py-16 flex items-center justify-center text-center">
        <p className="text-white text-xl">
          Thank you for signing up!
          <br />
          <span className="text-gray-400 text-base">Emails will arrive every week.</span>
        </p>
      </div>
    </main>
  );
}

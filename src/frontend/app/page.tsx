import { AuthView } from "@neondatabase/auth/react/ui";

export default function Home() {
  return (
    <main className="min-h-screen flex flex-col items-center justify-center gap-8 px-4">
      <AuthView
        pathname="sign-up"
        redirectTo="/thank-you"
        classNames={{ header: "text-center" }}
        localization={{ ALREADY_HAVE_AN_ACCOUNT: "", 
          SIGN_UP_DESCRIPTION: "Receive weekly job alerts from Hacker News hiring threads for Bangalore & Hyderabad.",
          SIGN_IN: "Already have an account?",
        }}
      />
    </main>
  );
}

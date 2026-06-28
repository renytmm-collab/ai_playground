import sys

from config import API_KEY, BASE_URL, MODEL, validate_config


try:
    from openai import APIConnectionError, APIStatusError, AuthenticationError, NotFoundError, OpenAI
except ImportError:
    OPENAI_AVAILABLE = False
else:
    OPENAI_AVAILABLE = True


def configure_output_encoding():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")


def create_client():
    return OpenAI(api_key=API_KEY, base_url=BASE_URL)


def ask_llm(client, messages):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
    )

    if not response.choices:
        raise RuntimeError("The model returned no choices.")

    reply = response.choices[0].message.content
    if not reply:
        raise RuntimeError("The model returned an empty message.")

    return reply


def remove_last_user_message(messages):
    if messages and messages[-1]["role"] == "user":
        messages.pop()


def print_request_error(error_message, messages):
    remove_last_user_message(messages)
    print(f"Error: {error_message}")


def main():
    configure_output_encoding()
    print("Hello 小叶")

    if not OPENAI_AVAILABLE:
        print("Error: openai is not installed. Please run: pip install -r requirements.txt")
        return

    config_error = validate_config()
    if config_error:
        print(f"Error: {config_error}")
        return

    client = create_client()
    messages = [
        {"role": "system", "content": "You are a helpful command-line chatbot."}
    ]
    print("Type exit or quit to leave.")

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print()
            print("Goodbye!")
            break

        if user_input.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})

        try:
            reply = ask_llm(client, messages)
        except AuthenticationError:
            print_request_error("API key authentication failed. Please check your .env file.", messages)
        except NotFoundError:
            print_request_error(f"model not found: {MODEL}", messages)
        except APIConnectionError:
            print_request_error("network connection failed. Please check your internet connection.", messages)
        except APIStatusError as exc:
            print_request_error(f"request failed with status {exc.status_code}: {exc.message}", messages)
        except RuntimeError as exc:
            print_request_error(str(exc), messages)
        except Exception as exc:
            print_request_error(f"unexpected request failure: {exc}", messages)
        else:
            messages.append({"role": "assistant", "content": reply})
            print(f"Bot: {reply}")


if __name__ == "__main__":
    main()

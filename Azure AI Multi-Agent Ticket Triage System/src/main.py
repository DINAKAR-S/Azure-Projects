from src.services.triage_service import run_triage

def main():

    ticket = input("Enter support ticket: ")

    result = run_triage(ticket)

    print("\nResult:\n")

    for msg in result:
        if msg.text_messages:
            print(msg.text_messages[-1].text.value)


if __name__ == "__main__":
    main()
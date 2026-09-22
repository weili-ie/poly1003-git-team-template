from responses.low import get_response as low_response
from responses.medium import get_response as medium_response
from responses.high import get_response as high_response
from responses.welcome import get_welcome


def main():
    print()
    print(get_welcome())
    print()
    energy = input("How is your energy today? low / medium / high: ").strip().lower()
    if energy == "low":
        print(low_response())
    elif energy == "medium":
        print(medium_response())
    elif energy == "high":
        print(high_response())
    else:
        print("I don't recognize that option yet.")


if __name__ == "__main__":
    main()

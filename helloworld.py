def say_hello(name):
    print(f"Good Morning, {name}")

def main():
    print("This is from the main function")
    name = input("Enter your name:")
    say_hello(name)

if __name__ == "__main__":
    main()
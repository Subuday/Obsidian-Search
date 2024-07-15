from index import index
from search import search

def main():
    while True:
        user_input = input("Search...\n")
        items = search(user_input)
        for (name, similarity) in items:
            print(f"{name} - ({similarity})")

if __name__ == "__main__":
    main()
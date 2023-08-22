# Description

**Cross-Site Scripting (XSS)** is a type of security vulnerability commonly found in web applications. It occurs when a web application allows an attacker to inject malicious scripts into the content that is then served to other users. These scripts are executed in the context of a victim's browser, allowing the attacker to perform various malicious actions.

If we visited `http://10.14.59.83/index.php?page=feedback`

We will find a FeedBack form with: 
	- name (mandatory)
	- Message (normaly mandatory but there is an error in the JS code)

# Attack

As for inputs in any websites we try if the developer did filter the input to prevent XXS.

Let's try and inject some javascript tags. we are going to put `script` in the Name and submit it.. and we got the flag.

```
The flag is : 0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e
```
# Prevention

1. **Input Validation and Sanitization:**
   - Validate and sanitize user input to ensure it matches the expected format.
   - Sanitize input by removing or escaping special characters.

2. **Output Encoding:**
   - Encode dynamic content before displaying it to prevent code execution.
   - Use context-specific encoding functions for HTML, JavaScript, URLs, etc.

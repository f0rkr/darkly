# Description

By Browsing the survey route we get a voting form.


We can vote by changing the Grade. As we see the Grade dropdown is like this
`<option value="10">10</option>`

# Attack

What we are going to do is to change to value of the option to a bigger value and see what's going to happen.

<option value="1000000000000000">10</option>


```
The flag is 03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa
```

And we got the flag.

# Prevention
 - we must check in backend if the value is in the valid range. (1 - 10)
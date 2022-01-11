# check_live_subdomain
a python file to minimise your huge subdomain.txt , can be in use in Bug Bounty / Peneteration testing.

## Requirements?
1. python3
2. python modules - 'os,requests,multiprocessing,socket'.
3. a 'subdomain.txt' in which you gathered uniq subdomains related to your target. like :-
```bash
$ ls -la
-rwx------ 1 maay maay 52539 Jan 11 02:47 subdomains.txt
```

## How to use?
after having the huge subdomain list, **paste** this python file in same dir where you have 'subdomain.txt' and run it. Finally u will get 'live.txt' file made by this python file. like:-
```bash
$ ./check_live_subdomain.py
569)  partner.glance.inmobi.com  ->  20.198.188.225 & code -  200
590)  post.iff.inmobi.com  ->  52.221.11.60 & code -  200
615)  pulse.inmobi.com  ->  40.81.254.85 & code -  200
etc..

$ wc live.txt
105  105 2644 live.txt

$ head live.txt
partner.glance.inmobi.com,200
post.iff.inmobi.com,200
pulse.inmobi.com,200
etc..
```

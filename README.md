# bitrix_scan


# wfuzz
```
cd /opt
git clone --depth 1 https://github.com/HiMiC/bitrix_scan.git
cd bitrix_scan

# словарь сделан для поиска в директории /bitrix/
wfuzz -w /opt/bitrix_scan/bitrix_wordlist.txt --hc 404 https://testphp.vulnweb.com/bitrix/FUZZ
```



```

wfuzz --script=backups -z list,robots.txt 
https://testphp.vulnweb.com/bitrix/php_interface/dbconn.php.FUZZ

wfuzz --script=backups -z list,dbconn.php  -p 192.168.1.39:8082 https://testphp.vulnweb.com/bitrix/php_interface/FUZZ

 

wfuzz --script=backups -z list,dbconn.php  -p 192.168.1.39:8082 https://testphp.vulnweb.com/bitrix/php_interface/dbconn.phpFUZZ

wfuzz --script=backups -z list,bitrix 
https://testphp.vulnweb.com/bitrixFUZZ


```


# URL
https://www.netangels.ru/support/cloud-hosting/vulnerabilities-cms-bitrix/
2024 год
https://habr.com/ru/articles/787326/

2022 год
attacking_bitrix.pdf
https://github.com/cr1f/writeups 
https://t.me/webpwn/317
https://spy-soft.net/cve-2022-27228-ntlm-relay/

2020 год
https://blog.deteact.com/ru/bitrix-waf-bypass/

# Other

https://github.com/snk0752/quick-tricks/
```
go install github.com/indigo-sadland/quick-tricks@latest

Настоящий репозиторий удален. (как ставить из этого репозитория неизвестно)
```

https://github.com/k1rurk/check_bitrix
```
cd /opt
git clone --depth 1 https://github.com/k1rurk/check_bitrix.git
cd /opt/check_bitrix

python3 test_bitrix.py -t https://example.com scan -s http://subdomain.oastify.com 
```
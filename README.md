# SenderMailgunPython
 
[![Python 3.7](https://img.shields.io/badge/python-3.7-yellow.svg)](https://www.python.org/)
[![Build](https://img.shields.io/badge/Supported_OS-Linux-orange.svg)]()
[![Build](https://img.shields.io/badge/Supported_OS-Mac-orange.svg)]()
![GitHub](https://img.shields.io/github/license/MrCl0wnLab/SenderMailgunPython?color=blue)

Modulo Python criado para envio simples de email via API Mailgun

```
 + Autor: MrCl0wn
 + Blog: http://blog.mrcl0wn.com
 + GitHub: https://github.com/MrCl0wnLab
 + Twitter: https://twitter.com/MrCl0wnLab
 + Email: mrcl0wnlab\@\gmail.com
```

## Access Your Domains
> https://app.mailgun.com/app/sending/domains

## Access Your Private API key
> https://app.mailgun.com/app/account/security/api_keys



## Implementation Code
```python
import sendmailgun

# Instantiate the client.
sendmailgun.API_KEY = 'YOUR_KEY_MAILGUN'

emails = ['xxx@gmail.com','yyy@gmail.com','ZZZ@bol.com.br']

body = ' <h1>click teste!!!xxx</h1>'

for email_target in emails:

    post_data = {
    'from': 'Your Name <you@your-mail.com.br>',
    'to': [email_target],
    'subject':'Your subject',
    'html':body
    }

    # Action sender.
    sendmailgun.send_mail('marketing.your-mail.com.br',post_data)
    print(mailgun.RESULT_SEND)
```
## Video
[![asciicast](https://asciinema.org/a/PfmqNN6TPhpSrSYwlPO4t28oy.svg)](https://asciinema.org/a/PfmqNN6TPhpSrSYwlPO4t28oy)

## Result
![Screenshot](https://i.imgur.com/9jzunUU.png)

## Reference:
> https://documentation.mailgun.com/en/latest/api-sending.html#sending


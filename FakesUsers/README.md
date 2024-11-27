# FakesUsers
FakesUsers - Python library that regenerates random names, phone numbers, addresses, email and much more.

## Content
- [About the project](#About-the-project)
- [New version](#New-vesion)
- [Install and Import](#Install-and-Import)
- [Basic Concepts](#Basic-Concept)
- [Example code](#Example-Code)
- [Information on creator](#Information-on-creator)

## About the project
FakesUsers -- is a project designed to generate random information from its database. It can be used for any purpose, as well as modified and improved in some way. filcher2011 is working on the project. He works hard on the project and tries to release updates more often.

## New vesion
New version FakesUsers 3.7. The fake_job() function was added, and the genRegion() function was also removed

## Install and Import
In order to import the library, you need to install it :)
Enter the cmd command to install this library
```sh
pip install FakesUsers
```
After that, in your file with the .py extension, write . . .
```sh
from FakesUsers import Fu
fu = Fu("ru/en/de")
```
PS:If you put Fu('ru'), then all names, numbers and addresses will be regenerated as relevant for Russia. otherwise, if you specify Fu('en'), all names, phone numbers, and addresses will be regenerated to the US. Otherwise, if you specify Fu('de'), all names, phone numbers and addresses will be regenerated for Germany.

Displaying a random name
```sh
fake_name('gender')
```
PS:If you write 'male' in brackets, then only male names will be generated, the opposite if you put 'female' in brackets

Displaying a random name
```sh
fake_lastname('gender')
```
PS:If you write 'male' in brackets, then only male lastnames will be generated, the opposite if you put 'female' in brackets

Displaying a random phone number
```sh
fake_number()
```

Displaying a random addres
```sh
fake_addres(True/False)
```
PS:True means that the address will be generated along with the city. Opposite with False

Displaying a random email
```sh
fake_email()
```

Displaying a random password
```sh
fake_pass()
```

Displaying a random city
```sh
fake_city()
```

Displaying a random Cart's number
```sh
fake_banknumber()
```

Displaying a random date of birth
```sh
fake_dob()
```

Displaying a random login
```sh
fake_login()
```

Displaying a random auto number
```sh
fake_autonumber()
```

Displaying a random website(link)
```sh
fake_link()
```

Displaying a random text
```sh
fake_text()
```

And displaying a random job
```sh
fake_job()
```

## Example Code
Let's look at a simple code that will output a random man's and woman's name, phone number and address
Code
```sh
from FakesUsers import Fu

fu = Fu('en')

print(fu.fake_name('male'))
print(fu.fake_name('female'))
print(fu.fake_city())
print(fu.fake_addres(True))
print(fu.fake_addres(False))
print(fu.fake_number())
print(fu.fake_email())
print(fu.fake_autonum())
print(fu.fake_pass())
print(fu.fake_link())
print(fu.fake_banknumber())
print(fu.fake_dob())
print(fu.fake_lastname('male'))
print(fu.fake_lastname('female'))
print(fu.fake_text())
print(fu.fake_job())
```
Result
```sh
Justin Cashman
Trinity Blare
San-Antonio city
Chicago City, 106 San-Alnaser Streed
42 Red Streed
+10069997590
beebag@outlook.qq
MBD-537
25246fu4516553225246
kitstant.com
1094 1940 4237 3418
18.3.1972
Absher
Bishop
You gone on a visit
Police Officer
```

## Information on creator
filcher2011 == I've been a Python programmer for about 2 years now. He does small projects :)
Telegram-channel: https://t.me/filchercode \
Financial support: https://www.donationalerts.com/r/filcher2011 

Αρχικά συνδεόμαστε στο vagrant box ή στον απομακρυσμένο server.

```
## vagrant
cd /path/to/vagrantfile
vagrant up
vagrant ssh


## okeanos
ssh vagrant@okeanos_ip
```

Δημιουργία python virtual environment και εγκατάσταση django.

```
mkdir .venvs
virtualenv .venvs/django
source .venvs/django/bin/activate
pip install django
git clone https://github.com/maellak/django_intro.git
cd django_intro

./manage.py runserver 0.0.0.0:8050
```

Επισκεφτείτε τη διεύθυνση:

vagrant | okeanos
--------|--------
192.168.33.10:8050 | okeanos_ip:8050

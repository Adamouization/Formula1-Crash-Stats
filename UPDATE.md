Upgrade pip
`pip3 install --upgrade pip`

Update all packages to latest
`pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U`

Freeze requirements
`pip3 freeze > requirements.txt`
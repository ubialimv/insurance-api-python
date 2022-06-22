https://www.newline.co/courses/create-a-serverless-slackbot-with-aws-lambda-and-python/installing-python-3-and-pyenv-on-macos-windows-and-linux#pyenv-on-ubuntu-linux-1804

curl https://pyenv.run | bash

sudo apt update

sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

pyenv install 3.9.13

pyenv versions

python --version

pip --version

pyenv virtualenv 3.9.13 insurance-api

pyenv activate insurance-api

touch requirements.txt

pip install -r requirements.txt

vi requirements.txt

fastapi==0.78.0

pip install -r requirements.txt

pip freeze

vi requirements.txt

colocar as depedencias da dependecia no requirements

pip install -r requirements.txt




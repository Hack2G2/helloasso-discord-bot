# HelloAsso Discord Bot

![HelloAsso logo](https://www.helloasso.com/_nuxt/img/logo-helloasso-midnight.0e553e3.svg)

## Setup

### Discord and HelloAsso configuration

1. Create a Discord application and bot, [here](https://discord.com/developers/applications).

2. On the left side menu, create an OAuth2 URL with the following permissions :
- Manage roles
- View channels
- Send messages

You now can add your bot to your Discord server using the OAuth2 URL.

3. Set your callback URL in HelloAsso to `http://<YOUR_IP>:<PORT>/<SECRET_PATH>`.

### Technical installation

1. Rename the file `.env.sample` to `env` and fill it with our Discord Token.

2. Run the bot :

With docker-compose :

```bash
docker-compse up -d
```

With docker :

```bash
docker build . -t helloasso
docker run -it --rm -p 5000:5000 helloasso
```

Without docker :

```bash
python3 -m pip install -r requirements.txt
python3 main.py
```


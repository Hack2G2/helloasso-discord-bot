# HelloAsso Discord Bot

![HelloAsso logo](https://www.helloasso.com/_nuxt/img/logo-helloasso-midnight.0e553e3.svg)

## Setup

1. Install Python dependencies.

```shell
python3 -m pip install -r requirements.txt
```

2. Create a Discord application and bot, [here](https://discord.com/developers/applications).

3. On the left side menu, create an OAuth2 URL with the following permissions :
- Manage roles
- View channels
- Send messages

You now can add your bot to your Discord server using the OAuth2 URL.

4. Rename the file `.env.sample` to `env` and fill it with our Discord Token.

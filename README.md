# TweetForward

TweetForward is a simple, dockerized, Python application to forward tweets to other messaging API's. Twitter's streaming api is used to maintain a connection with Twitter, and forward tweets to given clients.

## Version Tags

This image provides various versions that are available via tags. `latest` tag usually provides the latest stable version. Others are considered under development and caution must be exercised when using them.

| Tag | Description |
| :----: | --- |
| latest | Stable TweetForward releases |
| (branch)-(commit) | Unstable TweetForward releases |

## Application Setup

The application runs in the background and maintains a constant twitter stream.

### 1. Create a Twitter app and store your credentials

Head over to [developer.twitter.com](https://developer.twitter.com/en/apps) and register a new application. **Remeber, you’ll need elevated access for this!**

After registration, grab your application’s `API Key`, `API Secret`, `Access Token` and `Access Secret`.

### 2. Setup Telegram for forwarding.

You can either setup, and use, this application with your own Telegram app and bot credentials, or by using the default ones.

#### 2.1 Provide your own Telegram app and bot

Go to [my.telegram.org](https://my.telegram.org/) and create a new app. Locate and use your `API ID` and `API Hash`.

Create a Telegram bot through [@BotFather](https://t.me/botfather/) and copy your bot token. Make sure to add your bot, as admin, to the channel/chat where you want to receive tweets.

#### 2.2 Use the default Telegram bot

Simply add our default bot, [DUCKMADE TweetForward](https://t.me/duckmade_tweet_forward_bot), to your desired channel as an admin. This channel is where you’ll receive tweets.

## Usage

Here are some example snippets to help you get started creating a container.

### docker-compose (recommended)

```yaml
---
version: "3"
services:
  tweet-forward:
    image: ghrc.io/duckmade/tweet-forward
    container_name: tweet-forward
    restart: unless-stopped
    environment:
      - API_KEY: <key>
      - API_SECRET: <secret>
      - ACCESS_TOKEN: <token>
      - ACCESS_SECRET: <secret>
      - FOLLOW: <user-ids>
      - TRACK: <topics>
```

### docker cli

```bash
docker run -d \
  --name=tweet-forward \
  --restart unless-stopped \
  -e API_KEY=<key> \
  -e API_SECRET=<secret> \
  -e ACCESS_TOKEN=<token> \
  -e ACCESS_SECRET=<secret> \
  -e FOLLOW=<user-ids> \
  -e TRACK=<topics> \
  ghrc.io/duckmade/tweet-forward
```

## Parameters

Container images are configured using parameters passed at runtime (such as those above).

| Parameter | Function |
| :----: | --- |
| `-e API_KEY=<key>` | Twitter API key |
| `-e API_SECRET=<secret>` | Twitter API secret |
| `-e ACCESS_TOKEN=<token>` | Twitter access token |
| `-e ACCESS_SECRET=<secret>` | Twitter access token secret |
| `-e FOLLOW=<user-ids>` | Optional - Comma separated string of Twitter user ID's |
| `-e TRACK=<topics>` | Optional - Comma separated string of Twitter topics |
| `-e RETWEETS=<boolean>` | Optional - Do you want to forward retweets? |
| `-e CLIENTS=<clients>` | Optional - Comma separated string of forward clients to use. *Pick from: `telegram`.* |
| `-e TELEGRAM_CHANNEL=<channel>` | Optional - Telegram channel to forward to. Required when `telegram` client is used. |
| `-e TELEGRAM_ID=<id>` | Optional - Telegram API ID when using your own bot. |
| `-e TELEGRAM_HASH=<hash>` | Optional - Telegram API hash when using your own bot. |
| `-e TELEGRAM_TOKEN=<token>` | Optional - Telegram bot token when using your own bot. |

## Request Errors

In general the application will stop on crucial problems, however the API package will try to maintain the connection to Twitter when rate-limited (`code 420`). The status code is always printed to the console. It’s meaning can be look up on [Twitter’s developer page](https://developer.twitter.com/en/docs/twitter-api/enterprise/powertrack-api/guides/connecting).


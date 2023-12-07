# PythonDiscordBot

This is a discord bot written in python. This language was chosen since the API is well documented and seems to work better than its node.js counterpart

# Pushing to Docker Hub

To push to Docker Hub, use the following command:

```bash
docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t aaronvansanten/discord-bot:latest --push .
```

It might complain that you have no builder, in that case, run the following:

```bash
docker buildx create --name sillygoose --bootstrap --use
```

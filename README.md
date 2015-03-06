# mamoslack
Slack Slash command and Bot. A Django app that can listen to the [Slash] command
or behave like a [bot].

# Slash command
It should support a variety of command but for now we'll implement a command
to search Google Sites for certain keywords. Example:-

```
/alpha search ezsms faq
```
In above command, every thing after `search` will be treated as keywords. To speed
things up, all search that has a result will be cached. It will be stored in a MySQL
database so that the next search for the same keyword will return result from the
database instead of doing another request to Google API.

The cache can be disabled via the command parameter:-

```
/alpha search ezsms faq --no-cache
```

Everything start with `--` will be treated as options to the command.

# Bot
The bot can respond to a number of commands, or watch for certain characters in
message, and replied accordingly. For example, the bot can give the current time
in certain time zone:-

```
@alpha time now in Tokyo.
```

[Slash]:https://api.slack.com/slash-commands
[bot]:https://api.slack.com/bot-users

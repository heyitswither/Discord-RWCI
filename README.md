# Discord-RWCI
A bridge for Discord and RWCI

## Installation

```
git clone https://github.com/heyitswither/Discord-RWCI
cd Discord-RWCI
pip install -r requirements.txt
```

## Usage

Edit the `config.yml` file with your settings

Run normally

Example output:

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
RWCI client ready!
discord-link
Watching ws://localhost:5000
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Discord client ready!
Discord-RWCI#6543 368829819447672834
Watching #tmp in Wither Server
```

## Config

The following is an example confgiuration.

```
rwci:
        gateway: ws://localhost:5000
        channel: general
        username: discord-link
        password: discord-link
discord:
        channel_id: 368183566338752532
        token: MzY5MTgwNDQyMzAzMzk3OTAx.DMUxsQ.SWa1yg_pum3J5pFiIOc1a2XmPm4
```

You can leave the rwci:channel key blank to receive messages from any channel.

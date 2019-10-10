## NOTE

This has been changed to use alphavantage.co because Google Finance does not seem to work reliably anymore (IPs get blocked and it just plain out doesn't work)

You can get a free API key with a limited number of queries per second and so this has been tweaked to just refresh every 60s now.

Then just put the api-key into `alphavantage-creds.txt` to get it to work

## rtscli - Realtime Stock Ticker CLI
<a target="_blank" href="https://opensource.org/licenses/MIT" title="License: MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a> <a target="_blank" href="http://makeapullrequest.com" title="PRs Welcome"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg"></a>

- A stock ticker that runs in console
- It grabs info from Google Finance Api every 10 seconds, or if you press R
- It's pretty simple but if you wanna read through a blog post instead: https://aranair.github.io/posts/2017/06/28/building-a-python-cli-stock-ticker-with-urwid/

## Screenshot

![Demo](https://github.com/aranair/rtscli/blob/master/rtscli-demo.png?raw=true "Demo")

## Dependencies

Currently this is dependent on the list below but the next step is to build this into an executable so
all that stuff with python and pip can be skipped.

- Python2.7
- pip
- Bunch of other python packages

## Install via Pip

```
pip install rtscli
```

## Running it

```bash
$ cp tickers.txt.sample tickers.txt
$ rtscli
```

## Tickers.txt Sample

Format: Name, Ticker(Alphavantage format), cost price, shares held

```
GLD,GLD,139,1
```

## Downloading and building manually

```
$ git clone git@github.com:aranair/rtscli.git
$ pip install -e .
$ rtscli
```
## Future Developments

Not sure if this is of interest to anyone but if you'll like to see anything on this, raise an issue or something.

## License

MIT

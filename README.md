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

Format: Name, Ticker(Google format), cost price, shares held

```
Xinyi Solar,HKG:0968,2.368,12345
China Resources Power,HKG:0836,13.84,12345
Bank of China,HKG:3988,3.825,12345
Sitoy Group,HKG:1023
iShares India,HKG:2836
Evergrande,HKG:3333
Ping An,HKG:2318
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

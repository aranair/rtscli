rtscli - Realtime Stock Ticker CLI
===================================

## What is this?

- A stock ticker that runs in terminal
- It automatically grabs info from Google Finance Api every 10 seconds.
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

- `cp tickers.txt.sample tickers.txt`
- run `rtscli`

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

## License

MIT

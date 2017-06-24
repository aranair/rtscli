rtscli - Realtime Stock Ticker CLI
===================================

## What is this?

- A stock ticker that runs in terminal
- It automatically grabs info from Google Finance Api every 10 seconds.

## Screenshot

![Demo](https://github.com/aranair/corgi/blob/master/rtscli.png?raw=true "Demo")

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

- Add tickers.txt in the format below
- run `rtscli`

## Sample Tickers File

```
Xinyi Solar,HKG:0968
China Resources Power,HKG:0836
Bank of China,HKG:3988
Sitoy,HKG:1023
iShares India,HKG:2836
Evergrande,HKG:3333
Ping An,HKG:2318
```

## Downloading manually

```
$ git clone git@github.com:aranair/rtscli.git
$ pip install -e .
$ rtscli
```

## License

MIT

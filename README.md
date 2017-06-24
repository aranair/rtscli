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

## How to use it?

```
$ git clone git@github.com:aranair/rtscli.git
$ pip install -e .
$ rtscli
```

If you'll like to change the stocks, simply update `tickers.txt`

## License

MIT

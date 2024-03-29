# MooresCloudVisuals

> Ohhh look at the pretty lights

A collection of **Python** scripts for the Moores Cloud Holiday (_no longer in production_) - a string of 50 programmable lights over WiFi.

## Setup

Optional tidy sandbox setup, else jump to Usage

```sh
python -m pip install --user virtualenv
python -m virtualenv env
```

## Usage

Set the Shell environment variables to set the location of your lights once with `export HOLIDAY_ADDRESS=192.168.178.24` _or_ pass it as the first argument in the script call, eg. `python script_name.py 192.168.178.24`)

## Sets

1. `python cpu-meter.py` - from <https://github.com/pipelineoptika/holiday-cpu-meter/> (CPU Meter) - looks good at Xmas (green + red) with some drum & bass playing
1. `python snowfall.py` - random triggered white light animates along the length of the lights leaving decay to fade slowly
1. `python 2colorspin.py` - takes 2 colors ARGs and moves them along

## Contributing

Please feel free to fork and add to this list of scripts.

To be merged, scripts should:

- Use the local sub-moduled **HolidaySecretAPI**, eg `from secretapi.holidaysecretapi import HolidaySecretAPI`
- allow the first ARG to be the holiday location address, **AND**
- allow the `HOLIDAY_ADDRESS` environment variable to be read

I plan to make this a module so it's done once (not in each script).

> _Long live the [Moores Cloud Holiday](http://www.moorescloud.com/)_ (the fact that it timesout's is part of the (nerd) joke - _not funny_)

## TODO

- [ ] Build a controller to load each script
- [ ] Controller to handle the Holiday address once for each sub-script
- [ ] Write more animations (on going...)

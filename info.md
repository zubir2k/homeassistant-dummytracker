# Home Assistant: Dummy Device Tracker 📌
[![hacs_badge](https://img.shields.io/badge/HACS-Integration-41BDF5.svg)](https://github.com/hacs/integration)
![GitHub all releases](https://img.shields.io/badge/dynamic/json?color=41BDF5&logo=home-assistant&label=Download%20Count&suffix=%20installs&cacheSeconds=15600&url=https://analytics.home-assistant.io/custom_integrations.json&query=$.dummy_tracker.total)
[![Buy](https://img.shields.io/badge/Belanja-Coffee-yellow.svg)](https://zubirco.de/buymecoffee)
[![GitHub Release](https://img.shields.io/github/release/zubir2k/homeassistant-dummytracker.svg)](https://github.com/zubir2k/homeassistant-dummytracker/releases/)

## What is it? 🧐
This integration creates a dummy `device_tracker` entity with GPS coordinates based on your selected location.

## But.. why? 🤷🏻‍♂️
The idea started when I was creating the Appdaemon eSolatGPS where I needed to test various GPS coordinates.
The earlier version uses Appdaemon where it relies the GPS from a `input_text` entity and was limited to ONLY 1 location at a time.

With this integration, you can create as many `device_tracker` as you want 🎉

There are many use cases that you can benefit from this.
1. Trying out location triggered automation
2. Wanted to assign a person entity to a permanent location
3. Testing 

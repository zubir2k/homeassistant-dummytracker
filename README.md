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

## Wanna Give It a Try? 😉
The normal drill, get `HACS` if you still haven't done that. Then head to the settings where you can add a repository. \
Otherwise, just click the button below:

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=zubir2k&repository=homeassistant-dummytracker&category=integration)

After installation completed, restart your Home Assistant
- Next, go to your `Settings > Devices & services` menu and click at the `Add Integration`
- Look for `Dummy Device Tracker`
- Enter the GPS coordinates OR drag the pin to your desired location.
- Give it a name and press `Submit` to save changes.

Congrats! a new `device_tracker` entity has been created. 

## I love it! 🤩
Thank you.. do leave a ⭐ to this repo.

## And.. just to be clear ⚠
This dummy tracker is intended for simulation and testing. Any form of misuse or reliance on this tracker for real-world scenarios is strongly discouraged. The developers are not responsible for any consequences arising from incorrect use of this tool. Use it at your own risk.

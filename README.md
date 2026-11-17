![logo@2x](https://github.com/user-attachments/assets/44277989-5174-48c8-b5a4-e10f042b15b3)

[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg)](https://github.com/hacs/default)
[![hacs_badge](https://img.shields.io/badge/HACS-Integration-41BDF5.svg)](https://github.com/hacs/integration)
![GitHub all releases](https://img.shields.io/badge/dynamic/json?color=41BDF5&logo=home-assistant&label=Download%20Count&suffix=%20installs&cacheSeconds=15600&url=https://analytics.home-assistant.io/custom_integrations.json&query=$.dummy_tracker.total)
[![Buy](https://img.shields.io/badge/Belanja-Coffee-yellow.svg)](https://zubirco.de/buymecoffee)
[![GitHub Release](https://img.shields.io/github/release/zubir2k/homeassistant-dummytracker.svg)](https://github.com/zubir2k/homeassistant-dummytracker/releases/)

## What is it? 🧐  
This integration creates a dummy `device_tracker` entity with GPS coordinates based on your selected location.  

## But... why? 🤷🏻‍♂️  
The idea started when I was developing the [eSolatGPS](https://github.com/zubir2k/homeassistant-esolatgps), where I needed to test various GPS coordinates.  
The earlier version used AppDaemon, relying on the GPS from an `input_text` entity, which was limited to ONLY one location at a time.  

With this integration, you can create as many `device_tracker` entities as you want! 🎉  

There are many use cases where this can come in handy:  
1. Testing location-triggered automation  
2. Assigning a person entity to a permanent location  
3. Experimenting with GPS-based functionality  

## Installation
#### With Marketplace/HACS
[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=zubir2k&repository=homeassistant-dummytracker&category=integration)

> [!Tip]
> If you are unable to use the button above, manually search for Dummy Device Tracker in Marketplace/HACS.

#### Manual
1. Copy the `dummy_tracker` directory from `custom_components` in this repository and place inside your Home Assistant's `custom_components` directory.
2. Restart Home Assistant
3. Follow the instructions in the `Setup` section

> [!WARNING]
> If installing manually, in order to be alerted about new releases, you will need to subscribe to releases from this repository.

## Setup
[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=dummy_tracker)

> [!Tip]
> If you are unable to use the button above, follow the steps below:
> 1. Navigate to the Home Assistant Integrations page (Settings --> Devices & Services)
> 2. Click the `+ ADD INTEGRATION` button in the lower right-hand corner
> 3. Search for `Dummy Device Tracker`
> 4. Enter the GPS coordinates OR drag the pin to your desired location, give it a name and press `Submit`.

Congrats! A new `device_tracker` entity has been created. 🎊  
(Well, don't forget you will still require to assign the `device_tracker` to a person entity 🙋🏻‍♂️)

### Moving the pin later 📍  
Go to `Settings > Devices & Services > Dummy Device Tracker`, pick your tracker and hit `Configure`. Drag the pin, submit, and the tracker jumps there right away.

## What's new in v1.1.0 ✨  
- Ready for Home Assistant 2026.11 (minimum is now 2025.8.0).  
- Fixed: moving a tracker via `Configure` now actually updates its location.  
- Each tracker now shows up as its own device.  
- No more polling every 60 seconds; the location is static, so the state is written once.  
- The fake `battery_level` attribute is gone (Home Assistant deprecated it on device trackers; it stops working in 2027.7).  

## I love it! 🤩  
Thank you! If you like it, please consider leaving a ⭐ for this repo.  

## Tracking Animals Used in the Real World 🐾  
Various animals are commonly tracked for research, conservation, or other purposes:  
- **Homing Pigeons** 🐦 – Used for navigation and message delivery, guided by Earth's magnetic field.  
- **Hunting Dogs** 🐕 – Trained for tracking scents in hunting and search-and-rescue missions.  
- **Falcons** 🦅 – Sometimes equipped with GPS trackers to study flight patterns.  
- **Marine Animals** 🦈 – Sharks, sea turtles, and whales are tagged with GPS to monitor their movements.  
- **Big Cats** 🐆 – Cheetahs, leopards, and lions wear GPS collars for wildlife research.  
- **Bears & Wolves** 🐻🐺 – GPS collars help study their migration and habitat use.  

## And... just to be clear ⚠  
This dummy tracker is intended for simulation and testing. Any form of misuse or reliance on this tracker for real-world scenarios is strongly discouraged. The developers are not responsible for any consequences arising from incorrect use of this tool. Use it at your own risk. No known tracking animals were harmed during the making of this integration. 🐾  


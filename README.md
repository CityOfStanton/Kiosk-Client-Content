<!-- omit in toc -->
# Kiosk Client Content

This repository contains all of the configuration data for the [Kiosk Client](https://github.com/CityOfStanton/Kiosk-Client/) deployments. This content not only controls what is displayed, but also houses the assets used in the Orchestration files.

- [Current Configuration](#current-configuration)
- [Location Map](#location-map)
- [Structure](#structure)
  - [Assets](#assets)
  - [Settings](#settings)
  - [Location Names](#location-names)
    - [StantonCityPark](#stantoncitypark)
    - [StantonCityHall](#stantoncityhall)

## Current Configuration

* ![Static Badge](https://img.shields.io/badge/Input1-Concession%20Stand%20Menu-blue?logo=tv)
* ![Static Badge](https://img.shields.io/badge/Input2-Concession%20Stand%20Menu-green?logo=tv)
* ![Static Badge](https://img.shields.io/badge/Input3-Tournament%20Menu-yellow?logo=tv)
* ![Static Badge](https://img.shields.io/badge/Input4-Softball%20%20Registration%20Logo-purple?logo=tv)
* ![Static Badge](https://img.shields.io/badge/Input5-City%20Park%20Calendar%20--%20Week%20View-red?logo=tv)

## Location Map

| Computer Name | Status | Orientation | Location |
| - | - | :-: | - |
| Output 1 | Active | Vertical | Facing outside the window next to the entrance closest to the parking lot. |
| Output 2 | *Planned* | Horizontal | Mounted on the ceiling opposite the concession stand on the right, closest to the splash park. |
| Output 3 | *Planned* | Horizontal | Mounted on the ceiling opposite the concession stand on the left, closest to the baseball fields. |
| Output 4 | *Planned* | Horizontal | Mounted on the wall closest to the red playground on the left side. |
| Output 5 | Active | Horizontal | Mounted on the wall closest to the red playground on the right side. |
| Output 6 | *Planned* | Horizontal | Facing outside the walk-up window, closest to the baseball fields. |
| Output 7 | Active | Horizontal | Mounted to the left of the concession stand, closest to the baseball fields. |
| Output 8 | Active | Horizontal | Mounted to the right of the concession stand, closest to the splash park. |

## Structure

This outlines the structure of the repo.

### Assets

These are images, documents, etc. that are used in the Orchestration files.

### Settings

This is a collection of reusable Orchestration files. These should not be directly referenced.

### Location Names

Location where each Kiosk Client deployment points. Each device is named on-site to match its corresponding name in this directory. This allows for the Orchestrations to be updated dynamically without having to directly access the Kiosk devices.

#### StantonCityPark

All active Orchestration locations for the Stanton City Park.

#### StantonCityHall

All active Orchestration locations for Stanton City Hall.

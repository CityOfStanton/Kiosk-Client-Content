<!-- omit in toc -->
# Kiosk-Client-Content

This repository contains all of the configuration data for the [Kiosk Client](https://github.com/CityOfStanton/Kiosk-Client/) deployments. This content not only controls what is displayed, but also houses the assets used in the Orchestration files.

- [Structure](#structure)
  - [Assets](#assets)
  - [Settings](#settings)
  - [Location Names](#location-names)
    - [StantonCityPark](#stantoncitypark)
    - [StantonCityHall](#stantoncityhall)

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

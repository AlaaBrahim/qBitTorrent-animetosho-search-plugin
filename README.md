# qBittorrent AnimeTosho Search Plugin

## Overview

This is a search plugin for qBittorrent that allows you to search for anime torrents on AnimeTosho directly from the qBittorrent interface.

## Features

- Seamless integration with qBittorrent.
- Search for anime torrents on AnimeTosho without leaving the qBittorrent application.
- Quickly find and add anime torrents to your download queue.

## Installation

1. Open qBittorrent.
2. Navigate to the "Search" tab.
3. Click on the "Search Plugins" button.
4. In the Search Plugins window, click on the "Install a new one".
5. Click on the "Web link" tab
6. Paste the following web link: `https://raw.githubusercontent.com/AlaaBrahim/qBitTorrent-animetosho-search-plugin/main/animetosho.py` and click "OK".

## Usage

1. Open qBittorrent.
2. Navigate to the search view and select the plugin Anime Tosho.
3. Enter your search query in the search bar.
4. Press Enter to initiate the search.
5. Browse the search results and click on a result to view more details.
6. Click the "Add" button to add the selected torrent to your download queue.

## Screenshots

![AnimeTosho Search](/screenshots/screenshot.png)

## Code Quality Assurance

We use GitHub Actions to ensure the code quality of this plugin. On every pull request and push, the following checks are performed:

- Linting with PyFlakes.
- Security analysis with Bandit.
- Code formatting with Pycodestyle.

The workflow configuration can be found in the [CI workflow file](.github/workflows/ci.yaml).

## Contributing

If you would like to contribute to the development of this plugin, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/new-feature` or `git checkout -b bugfix/fix-description`.
3. Make your changes and commit them: `git commit -m 'Your commit message'`.
4. Push to the branch: `git push origin feature/new-feature`.
5. Open a pull request on the [GitHub repository](https://github.com/AlaaBrahim/qBitTorrent-animetosho-search-plugin).

## Issues

If you encounter any issues or have suggestions, please open an issue on the [GitHub repository](https://github.com/AlaaBrahim/qBitTorrent-animetosho-search-plugin/issues).

## License

This project is licensed under the [MIT License].

Happy torrenting!

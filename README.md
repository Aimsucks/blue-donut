<h1 align="center">Blue Donut</h1>

<div align="center">
  <strong><i>Tools to help Legacy Coalition members live in their space.</i></strong>
  <br>
  <br>

  <a href="https://github.com/Aimsucks/blue-donut/">
    <img src="https://img.shields.io/pypi/pyversions/Django?style=for-the-badge" alt="Python Versions" />
  </a>

  <a href="https://github.com/Aimsucks/blue-donut/issues">
    <img src="https://img.shields.io/github/issues/aimsucks/blue_donut?style=for-the-badge" alt="PyPi" />
  </a>

  <a href="https://discordapp.com/invite/UCK8ase">
    <img src="https://img.shields.io/discord/645977792265322506?color=%237289DA&label=DISCORD&style=for-the-badge" alt="Discord" />
  </a>

  <a href="https://github.com/Aimsucks/blue-donut/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/aimsucks/blue-donut?style=for-the-badge" alt="Discord" />
  </a>
</div>

<br>

<div align="center">
  This is a website that hosts a multitude of features. Currently the only supported feature (and on this repo) is a built-in route planner that is still being actively developed.
  The route planner currently only supports manual input. Automatic updates are being actively worked on.
</div>

## Installation

Install Poetry and then install the requirements.

```commandline
pip install poetry
poetry install
```

Configure your settings by copying/renaming `blue_donut/example.local.py` to `blue_donut/local.py` and editing the file to fill in missing information.

```commandline
cp blue_donut/example.local.py blue_donut/local.py
nano blue_donut/local.py
```

Run all migrations, download the maps, and then run the development server.

```commandline
poetry run python manage.py migrate
poetry run python manage.py sde_get_map
poetry run python manage.py runserver
```

## License

This project is licensed under MIT.

## Contributing

Feel free to contribute to this project, a helping hand is always appreciated.
If you have any feature suggestions, don't hesitate to make an issue.

[Join our discord server](https://discordapp.com/invite/UCK8ase).

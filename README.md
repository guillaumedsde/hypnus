# 💤 Hypnus

Hypnus is a small utility to turn off your computer if the [EDF Tempo](https://particulier.edf.fr/fr/accueil/gestion-contrat/options/tempo/details.html) day is red.

Hypnus is implemented using the python standard library exclusively (it does not require external dependencies to run) and is compatible with the following python versions:

- 3.8
- 3.9
- 3.10
- 3.11
- 3.12

## ⚙️ How does it work?

1. Queries the free [api-couleur-tempo.fr](https://www.api-couleur-tempo.fr) API to determine today's Tempo color.
2. If that color is red, it turns off the computer (provided the current user has enough permissions for it)

## 🏁 Getting started

Hypnus is a small utility that executes once, it purposefully does not implement any scheduling.

You can install and run it like so:

```bash
pip install hypnus
hypnus
```

You can schedule the `hypnus` command to run every day at 6:00 AM (time at which the Tempo color changes).

## 🔮 Roadmap

- [x] Published Pypi package
- [ ] Published multiarchitecture docker image
- [ ] Published static binary

## ⚖️ License

See the [`LICENSE`](LICENSE) file.
from morpheus import power, tempo


def _main() -> None:
    day_color = tempo.get_todays_tempo_color()

    if day_color is tempo.TempoDayColor.RED:
        power.shutdown()


if __name__ == "__main__":
    _main()

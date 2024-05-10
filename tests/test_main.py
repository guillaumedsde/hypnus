import logging
from unittest import mock

import pytest

from morpheus import main
from morpheus.tempo import TempoDayColor


@pytest.mark.parametrize(
    "tempo_color",
    TempoDayColor,
    ids=TempoDayColor._member_names_,
)
@mock.patch("morpheus.main.power.shutdown", autospec=True)
@mock.patch("morpheus.main.tempo.get_todays_tempo_color", autospec=True)
def test_main_shutdown_on_day_color(
    mock_get_todays_tempo_color: mock.MagicMock,
    mock_shutdown: mock.MagicMock,
    tempo_color: TempoDayColor,
    caplog: pytest.LogCaptureFixture,
) -> None:
    caplog.set_level(logging.INFO)
    mock_get_todays_tempo_color.return_value = tempo_color

    main._main()

    mock_get_todays_tempo_color.assert_called_once_with()

    assert f"Today is a {tempo_color.name} day" in caplog.text

    shutdown_message_in_logs = "Shutting down computer" in caplog.text

    if tempo_color is TempoDayColor.RED:
        mock_shutdown.assert_called_once_with()
        assert shutdown_message_in_logs
    else:
        mock_shutdown.assert_not_called()
        assert not shutdown_message_in_logs

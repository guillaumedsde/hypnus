import json
from unittest import mock

import pytest

from morpheus import tempo


@pytest.mark.parametrize(
    "expected_day_color",
    tempo.TempoDayColor,
    ids=tempo.TempoDayColor._member_names_,
)
@mock.patch("morpheus.tempo.urllib.request.urlopen", autospec=True)
def test_get_todays_tempo_color(
    mock_url_open: mock.MagicMock,
    expected_day_color: tempo.TempoDayColor,
) -> None:
    json_day_info = json.dumps(
        {
            "dateJour": "2024-05-10",
            "codeJour": expected_day_color.value,
            "periode": "2023-2024",
        },
    )
    mock_url_open.return_value.__enter__.return_value.read.return_value = json_day_info
    day_color = tempo.get_todays_tempo_color()

    assert day_color == expected_day_color

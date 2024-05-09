from unittest import mock

import pytest

from morpheus import power


@mock.patch("morpheus.power.sys.platform", new="win32")
@mock.patch("ctypes.WinDLL", create=True)
def test_shutdown_windows(mock_win_dll: mock.MagicMock) -> None:
    mock_win_dll_instance = mock.MagicMock()
    mock_win_dll.return_value = mock_win_dll_instance

    power.shutdown()

    mock_win_dll.assert_called_once_with("user32")
    mock_win_dll_instance.ExitWindowsEx.assert_called_once_with(
        power.EWX_POWEROFF,
        power.SHTDN_REASON_MAJOR_OTHER,
    )


@pytest.mark.parametrize("platform", power.POSIX_PLATFORMS)
@mock.patch("morpheus.power.subprocess.run", autospec=True)
def test_shutdown_posix(mock_run: mock.MagicMock, platform: str) -> None:
    with mock.patch("morpheus.power.sys.platform", new=platform):
        power.shutdown()

    mock_run.assert_called_once_with(
        ("shutdown", "-h", "now"),
        check=True,
    )
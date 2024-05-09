import ctypes
import subprocess
import sys


class ShutdownNotImplementedForPlatformError(NotImplementedError): ...


class CouldNotShutdownError(RuntimeError): ...


# NOTE: shutdown type
EWX_POWEROFF = 0x00000008
# NOTE: shutdown reason
SHTDN_REASON_MAJOR_OTHER = 0x00000000


def _windows_shutdown() -> None:
    user32 = ctypes.WinDLL("user32")
    user32.ExitWindowsEx(EWX_POWEROFF, SHTDN_REASON_MAJOR_OTHER)


def _posix_shutdown() -> None:
    subprocess.run(["shutdown", "-h", "now"], check=False)  # noqa: S603


def shutdown() -> None:
    """Shutdown the computer, supports multiple platforms.

    Raises:
        ShutdownNotImplementedForPlatformError:
            When current platform not supported.
        CouldNotShutdownError:
            When an error occured while shutting down computer.
    """
    match sys.platform:
        case "win32":
            _windows_shutdown()
        case (
            "linux"
            | "linux2"
            | "darwin"
            | "freebsd7"
            | "freebsd8"
            | "freebsdN"
            | "openbsd6"
        ):
            _posix_shutdown()
        case _:
            raise ShutdownNotImplementedForPlatformError

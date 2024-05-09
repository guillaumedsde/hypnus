import subprocess
import sys


class ShutdownNotImplementedForPlatformError(NotImplementedError): ...


class CouldNotShutdownError(RuntimeError): ...


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
            import ctypes

            user32 = ctypes.WinDLL("user32")
            user32.ExitWindowsEx(0x00000008, 0x00000000)
        case (
            "linux"
            | "linux2"
            | "darwin"
            | "freebsd7"
            | "freebsd8"
            | "freebsdN"
            | "openbsd6"
        ):
            subprocess.run(["shutdown", "-h", "now"], check=False)  # noqa: S603
        case _:
            raise ShutdownNotImplementedForPlatformError

import os
import platform


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
    match platform.system():
        case "Windows":
            exit_code = os.system("shutdown -s")
        case "Linux" | "Darwin":
            exit_code = os.system("shutdown -h now")
        case _:
            raise ShutdownNotImplementedForPlatformError
    if exit_code != 0:
        raise CouldNotShutdownError

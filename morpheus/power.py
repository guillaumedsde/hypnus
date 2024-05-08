import os
import platform


class ShutdownNotImplementedForPlatformError(NotImplementedError): ...


def shutdown() -> None:
    """Shutdown the computer, supports multiple platforms.

    Raises:
        ShutdownNotImplementedForPlatformError: When current platform not supported.
    """
    match platform.system():
        case "Windows":
            os.system("shutdown -s")
        case "Linux" | "Darwin":
            os.system("shutdown -h now")
        case _:
            raise ShutdownNotImplementedForPlatformError

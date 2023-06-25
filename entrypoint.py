# !/usr/bin/env python
import subprocess
import sys

from configs.web import WebConfig

if __name__ == "__main__":
    _component = sys.argv[1]
    match _component:
        case "web":
            cfg: WebConfig = WebConfig()  # type: ignore[call-arg]
            subprocess.call(
                f"uvicorn web.run:app --host {cfg.LISTEN_HOST} --port {cfg.LISTEN_PORT}",
                shell=True,  # noqa[S602]
            )
        case "migrator":
            subprocess.call("alembic upgrade head", shell=True)  # noqa[S602]
        case _:
            msg = "Unknown component"
            raise ValueError(msg)

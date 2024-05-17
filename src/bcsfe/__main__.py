import traceback
import requests
import sys

from bcsfe import cli

try:
    ve = requests.get("https://bcpulse.net/bcsfeguip/api/version", timeout=3).text
    if ve != "0BTLasfOBXwfkeHvPGMc45tgRQPf3wAzA/Fpn8DWOas=":
        print("에디터 서버가 오프라인입니다.")
        sys.exit(1)
    else:
        cli.main.Main().main()
except KeyboardInterrupt:
    cli.main.Main.leave()
except Exception as e:
    tb = traceback.format_exc()
    cli.color.ColoredText.localize("error", error=e, traceback=tb)
    try:
        cli.main.Main.exit_editor()
    except Exception:
        pass
    except KeyboardInterrupt:
        pass

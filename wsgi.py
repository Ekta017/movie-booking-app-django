import os
from django.core.management import call_command

if os.environ.get("RENDER"):
    try:
        call_command("migrate", interactive=False)
    except Exception:
        pass
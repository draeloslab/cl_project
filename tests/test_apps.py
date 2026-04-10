import subprocess
import sys
from pathlib import Path

import pytest

APPLICATIONS_DIR = Path(__file__).parent.parent / "applications"

app_dirs = sorted([d for d in APPLICATIONS_DIR.iterdir() if d.is_dir()])


@pytest.mark.parametrize("app_dir", app_dirs, ids=[d.name for d in app_dirs])
def test_app_runs_successfully(app_dir: Path):
    result = subprocess.run(
        [sys.executable, "-m", "cl.app.run", str(app_dir), str(app_dir / "default.json")],
        capture_output=True,
        text=True,
    )
    assert "Application run completed successfully" in result.stdout, (
        f"Expected success message not found for {app_dir.name}.\n"
        f"stdout:\n{result.stdout}\n"
        f"stderr:\n{result.stderr}"
    )


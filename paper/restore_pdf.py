"""Restore the original D01.pdf from lossless binary parts."""

from __future__ import annotations

import hashlib
from pathlib import Path


EXPECTED_SHA256 = "4e31a7907dc46e4328589e90500e179561fcb7d20aca3c708cb5115026f478d6"


def main() -> None:
    paper_dir = Path(__file__).resolve().parent
    parts = sorted((paper_dir / "parts").glob("D01.pdf.part-*"))
    if not parts:
        raise FileNotFoundError("No PDF parts were found in paper/parts")

    output = paper_dir / "D01.pdf"
    digest = hashlib.sha256()
    with output.open("wb") as target:
        for part in parts:
            data = part.read_bytes()
            target.write(data)
            digest.update(data)

    actual_sha256 = digest.hexdigest()
    if actual_sha256 != EXPECTED_SHA256:
        output.unlink(missing_ok=True)
        raise ValueError(
            f"SHA-256 mismatch: expected {EXPECTED_SHA256}, got {actual_sha256}"
        )

    print(f"Restored: {output}")
    print(f"SHA-256: {actual_sha256}")


if __name__ == "__main__":
    main()

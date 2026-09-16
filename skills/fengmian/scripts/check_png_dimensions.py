#!/usr/bin/env python3
"""Check PNG dimensions without third-party dependencies."""

from __future__ import annotations

import argparse
import struct
from pathlib import Path


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def read_png_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        signature = handle.read(8)
        if signature != PNG_SIGNATURE:
            raise ValueError(f"not a PNG file: {path}")
        length = struct.unpack(">I", handle.read(4))[0]
        chunk_type = handle.read(4)
        if chunk_type != b"IHDR" or length < 8:
            raise ValueError(f"missing PNG IHDR chunk: {path}")
        return struct.unpack(">II", handle.read(8))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path)
    parser.add_argument("--width", type=int, required=True)
    parser.add_argument("--height", type=int, required=True)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    actual = read_png_size(args.image)
    expected = (args.width, args.height)
    if actual != expected:
        raise SystemExit(
            f"dimension mismatch for {args.image}: expected {expected[0]}x{expected[1]}, "
            f"got {actual[0]}x{actual[1]}"
        )
    print(f"{args.image}: {actual[0]}x{actual[1]}")


if __name__ == "__main__":
    main()

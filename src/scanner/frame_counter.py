from __future__ import annotations
from dataclasses import dataclass
from functools import total_ordering
from typing import List, Optional

from dataclasses_json import dataclass_json


SPECIAL_FRAME_NAMES = {
    "00": -1,
}


@total_ordering
@dataclass_json
@dataclass(frozen=True)
class FrameCounter:
    current_frame_index: int = 0

    def next(self) -> FrameCounter:
        return FrameCounter(self.current_frame_index + 1)

    def __str__(self):
        if self.current_frame_index >= 0:
            return str(self.current_frame_index)
        else:
            for k, v in SPECIAL_FRAME_NAMES.items():
                if v == self.current_frame_index:
                    return k

        raise AssertionError("Frame name should exist")

    def __eq__(self, other: object) -> bool:
        if isinstance(other, FrameCounter):
            return self.current_frame_index == other.current_frame_index
        return NotImplemented

    def __lt__(self, other: object):
        if isinstance(other, FrameCounter):
            return self.current_frame_index < other.current_frame_index
        return NotImplemented


def from_string(frame_name: str) -> Optional[FrameCounter]:
    if not frame_name:
        return None

    frame_index = SPECIAL_FRAME_NAMES.get(frame_name)
    if frame_index is None:
        frame_index = int(frame_name, base=10)

    return FrameCounter(frame_index)


def list_typical_frames() -> List[str]:
    return [str(FrameCounter(idx)) for idx in range(-1, 37)]

from pathlib import Path
from PIL import Image
import numpy as np


class DatasetCase:
    def __init__(self, case_id: str, input_path: Path, expected_path: Path):
        self.case_id = case_id
        self.input_path = input_path
        self.expected_path = expected_path

    def load_input(self) -> Image.Image:
        return Image.open(self.input_path).convert("RGBA")

    def load_expected_mask(self) -> np.ndarray:
        img = Image.open(self.expected_path).convert("RGBA")
        alpha = np.array(img)[:, :, 3]
        return alpha > 0


def load_dataset(root: Path) -> list[DatasetCase]:
    cases = []

    for case_dir in sorted(root.iterdir()):
        if not case_dir.is_dir():
            continue

        input_path = case_dir / "input.png"
        expected_path = case_dir / "expected.png"

        if not input_path.exists() or not expected_path.exists():
            raise RuntimeError(f"Invalid dataset case: {case_dir}")

        cases.append(
            DatasetCase(
                case_id=case_dir.name,
                input_path=input_path,
                expected_path=expected_path,
            )
        )

    return cases


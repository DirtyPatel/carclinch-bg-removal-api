import gc
import numpy as np
from pathlib import Path
from collections import defaultdict
from dataset import load_dataset
from models import run_model, clear_model_sessions
from metrics import dice, iou
from PIL import Image

# config

MODELS = [
    "u2net",
    "u2netp",
    "silueta",
    "isnet-general-use",
    "sam",
    "birefnet-general",
    "birefnet-general-lite",
    "bria-rmbg",
]

DATASET_ROOT = Path("dataset")
CACHE_ROOT = Path(".cache")
MAX_SIZE = (1024, 1024)
DICE_THRESHOLD = 0.95  # must pass threshold to pass the test


def load_or_run_model(case, model_name):
    model_cache = CACHE_ROOT / model_name
    model_cache.mkdir(parents=True, exist_ok=True)
    cache_path = model_cache / f"{case.case_id}.npy"

    gt_mask = case.load_expected_mask()

    if cache_path.exists():
        pred_mask = np.load(cache_path)
        # ensure cached mask matches current GT shape
        if pred_mask.shape == gt_mask.shape:
            return pred_mask
        print(f"  [Cache Mismatch] Shape changed for {case.case_id}. Re-running.")

    input_img = case.load_input()

    if input_img.width > MAX_SIZE[0] or input_img.height > MAX_SIZE[1]:
        ratio = min(MAX_SIZE[0] / input_img.width, MAX_SIZE[1] / input_img.height)
        new_size = (int(input_img.width * ratio), int(input_img.height * ratio))
        input_img = input_img.resize(new_size, Image.Resampling.LANCZOS)

    output = run_model(input_img, model_name)
    if output.ndim == 3:
        output = output[:, :, 3] > 0

    if output.shape != gt_mask.shape:
        pred_img = Image.fromarray(output.astype(np.uint8) * 255)
        pred_img = pred_img.resize(
            (gt_mask.shape[1], gt_mask.shape[0]), Image.Resampling.NEAREST
        )
        pred_mask = np.array(pred_img) > 0
    else:
        pred_mask = output

    np.save(cache_path, pred_mask)
    return pred_mask


def print_detailed_stats(model_name, results):
    dices = np.array([r["dice"] for r in results])
    ious = np.array([r["iou"] for r in results])

    # identify failures
    failures = [r for r in results if r["dice"] < DICE_THRESHOLD]

    print(f"Analysis: {model_name}")

    stats_table = [
        ["Metric", "Mean", "Median", "Std Dev", "Min", "Max"],
        [
            "Dice",
            f"{np.mean(dices):.4f}",
            f"{np.median(dices):.4f}",
            f"{np.std(dices):.4f}",
            f"{np.min(dices):.4f}",
            f"{np.max(dices):.4f}",
        ],
        [
            "IoU",
            f"{np.mean(ious):.4f}",
            f"{np.median(ious):.4f}",
            f"{np.std(ious):.4f}",
            f"{np.min(ious):.4f}",
            f"{np.max(ious):.4f}",
        ],
    ]

    for row in stats_table:
        print(
            f"{row[0]:<10} {row[1]:>10} {row[2]:>10} {row[3]:>10} {row[4]:>10} {row[5]:>10}"
        )

    if failures:
        print(f"\nTHRESHOLD FAILURES (Dice < {DICE_THRESHOLD}):")
        for f in failures:
            print(f"  - {f['case']}: Dice={f['dice']:.4f}, IoU={f['iou']:.4f}")
    else:
        print(f"\nAll files passed threshold ({DICE_THRESHOLD})")
    print(f"\n{'=' * 65}\n")


def evaluate(dataset_root: Path):
    cases = load_dataset(dataset_root)
    all_results = defaultdict(list)

    for model in MODELS:
        for case in cases:
            gt_mask = case.load_expected_mask()
            pred_mask = load_or_run_model(case, model)

            all_results[model].append(
                {
                    "case": case.case_id,
                    "dice": dice(gt_mask, pred_mask),
                    "iou": iou(gt_mask, pred_mask),
                }
            )
            del gt_mask, pred_mask

        print_detailed_stats(model, all_results[model])

        clear_model_sessions()
        gc.collect()

    return all_results


if __name__ == "__main__":
    evaluate(DATASET_ROOT)

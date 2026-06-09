import os
import torch
import torch.nn as nn
from pathlib import Path


# Classes excluded from training — digits and letters requiring hand motion.
ASL_EXCLUDE = frozenset({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Z'})


def download_asl_dataset(data_dir="data/asl_data", exclude=None):
    """Download the ASL-HG dataset from HuggingFace Hub and return as DataFrames.

    If sign_mnist_train.csv and sign_mnist_valid.csv already exist in *data_dir*,
    they are loaded and returned directly (no network access).  Otherwise the
    dataset is downloaded from HuggingFace Hub, each image is converted to a
    28×28 grayscale representation and flattened, and the results are saved as
    CSV files before being returned.

    The CSV format intentionally mirrors the original sign-language MNIST layout:
        label  pixel1  pixel2  ...  pixel784

    where *label* is a contiguous integer in [0, 23] and the pixel values are
    uint8 integers in [0, 255].

    Label mapping (alphabetical order after exclusions):
        A=0  B=1  C=2  D=3  E=4  F=5  G=6  H=7  I=8
        K=9  L=10 M=11 N=12 O=13 P=14 Q=15 R=16 S=17
        T=18 U=19 V=20 W=21 X=22 Y=23

    Args:
        data_dir : directory for the cached CSV files (default: "data/asl_data")
        exclude  : set of class-name strings to skip (default: ASL_EXCLUDE)

    Returns:
        (train_df, valid_df) — pandas DataFrames ready for MyDataset
    """
    import numpy as np
    import pandas as pd

    data_dir = Path(data_dir)
    train_csv = data_dir / "sign_mnist_train.csv"
    valid_csv = data_dir / "sign_mnist_valid.csv"

    if train_csv.exists() and valid_csv.exists():
        print(f"Loading cached dataset from '{data_dir}' …")
        return pd.read_csv(train_csv), pd.read_csv(valid_csv)

    print("Downloading ASL dataset from HuggingFace Hub …")
    from datasets import load_dataset

    exclude  = ASL_EXCLUDE if exclude is None else frozenset(exclude)
    hf_ds    = load_dataset("juanjodurillo/asl-hg")

    # Build label mapping: original integer → new contiguous integer (sorted alphabetically)
    all_classes      = hf_ds["train"].features["label"].names   # list[str], indexed by label int
    keep_sorted      = sorted(c for c in all_classes if c not in exclude)
    name_to_new      = {c: i for i, c in enumerate(keep_sorted)}
    old_to_new       = {idx: name_to_new[name]
                        for idx, name in enumerate(all_classes)
                        if name in name_to_new}

    pixel_cols = [f"pixel{i + 1}" for i in range(784)]
    split_map  = {"train": train_csv, "test": valid_csv}  # HF "test" → our "valid"

    data_dir.mkdir(parents=True, exist_ok=True)
    result = {}

    for hf_split, csv_path in split_map.items():
        ds = hf_ds[hf_split]
        print(f"Processing {hf_split} ({len(ds):,} images) …")

        rows = []
        for item in ds:
            orig_idx = item["label"]
            if orig_idx not in old_to_new:
                continue
            new_label = old_to_new[orig_idx]
            # Convert to 28×28 grayscale, flatten to 784 uint8 values
            pixels = np.array(
                item["image"].convert("L").resize((28, 28)),
                dtype=np.uint8
            ).flatten().tolist()
            rows.append([new_label] + pixels)

        df = pd.DataFrame(rows, columns=["label"] + pixel_cols)
        df.to_csv(csv_path, index=False)
        split_label = "valid" if hf_split == "test" else hf_split
        print(f"  {len(df):,} rows saved → '{csv_path}'")
        result[split_label] = df

    print("Dataset ready.")
    return result["train"], result["valid"]


class MyConvBlock(nn.Module):
    def __init__(self, in_ch, out_ch, dropout_p):
        kernel_size = 3
        super().__init__()

        self.model = nn.Sequential(
            nn.Conv2d(in_ch, out_ch, kernel_size, stride=1, padding=1),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(),
            nn.Dropout(dropout_p),
            nn.MaxPool2d(2, stride=2)
        )

    def forward(self, x):
        return self.model(x)


def get_batch_accuracy(output, y, N):
    pred = output.argmax(dim=1, keepdim=True)
    correct = pred.eq(y.view_as(pred)).sum().item()
    return correct / N


def train(model, train_loader, train_N, random_trans, optimizer, loss_function, device):
    loss = torch.zeros((), device=device)
    correct = torch.zeros((), device=device)

    model.train()
    for x, y in train_loader:
        output = model(random_trans(x))
        optimizer.zero_grad()
        batch_loss = loss_function(output, y)
        batch_loss.backward()
        optimizer.step()

        loss    += batch_loss.detach()
        correct += output.argmax(dim=1).eq(y).sum()

    accuracy = correct / train_N
    print('Train - Loss: {:.4f} Accuracy: {:.4f}'.format(loss.item(), accuracy.item()))


def validate(model, valid_loader, valid_N, loss_function, device):
    loss = torch.zeros((), device=device)
    correct = torch.zeros((), device=device)

    model.eval()
    with torch.no_grad():
        for x, y in valid_loader:
            output = model(x)
            loss    += loss_function(output, y)
            correct += output.argmax(dim=1).eq(y).sum()

    accuracy = correct / valid_N
    print('Valid - Loss: {:.4f} Accuracy: {:.4f}'.format(loss.item(), accuracy.item()))

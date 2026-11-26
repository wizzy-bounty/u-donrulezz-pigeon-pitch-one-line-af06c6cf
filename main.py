import os

ENTRY_TEXT = "Our CAC is one french fry and our LTV is the entire flock — do the math, then fund the math."


def entry_text():
    return ENTRY_TEXT


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(entry_text())


if __name__ == "__main__":
    main()

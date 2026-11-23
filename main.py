import os

LINE = "My robot vacuum eats my charging cables, then beeps for rescue like a toddler who swallowed a Lego — I wanted a cleaner and adopted a needy pet."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)

if __name__ == "__main__":
    print(f"{len(LINE)} chars: {LINE}")

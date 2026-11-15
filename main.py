"""ai-excited-01-v2: a colossal blue whale breaching out of a tiny teacup.

The program copies the entry image beside this file to the output
directory as entry.png. Python 3.13, standard library only.

Clean round-2 rebuild: a fresh image generated in-session, same joyful
whale-breaching-from-a-teacup concept as round 1.
"""

import hashlib
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

os.makedirs(os.path.dirname(DST), exist_ok=True)
shutil.copyfile(SRC, DST)

# The output must be byte-identical to the image shipped in the repo.
with open(SRC, "rb") as f:
    src_hash = hashlib.sha256(f.read()).hexdigest()
with open(DST, "rb") as f:
    dst_hash = hashlib.sha256(f.read()).hexdigest()
assert src_hash == dst_hash, "entry.png copy is not byte-identical"

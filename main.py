"""One sentence for a traveler from 1800, in the tongue of his own century.

One book holds every book ever written; a letter slipped inside it reaches
any door on earth before the ink is dry. Writes the entry text to
/output/entry.txt with no trailing newline.
"""

from pathlib import Path

entry_sentence = "One book holds every book ever written, and a letter slipped inside it reaches any door on earth before the ink is dry."

output_path = Path("/output/entry.txt")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(entry_sentence, encoding="utf-8")

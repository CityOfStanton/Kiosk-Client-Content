"""
update_badges.py

Walks every leaf Settings.json under StantonCityPark/, reads the `name`
property, and updates any matching Shields.io Static Badge in README.md.

Badge format expected in README.md:
  ![Static Badge](https://img.shields.io/badge/<FOLDER_NAME>-<label>-<color>?logo=tv)

The <FOLDER_NAME> is matched against the direct parent folder name of each
Settings.json file found. The <label> portion (between the first and last
dash segments) is replaced with the URL-encoded name from the JSON file.

Usage:
  python update_badges.py --repo-root <path_to_repo_root>
"""

import argparse
import json
import os
import re
import sys


def url_encode_badge_label(text: str) -> str:
    """Encode a string for use in a Shields.io badge label.

    Shields.io uses a custom encoding:
      - Spaces  -> %20
      - Hyphens -> --   (a single hyphen would be interpreted as a separator)
      - Underscores -> __
    """
    text = text.replace("-", "--")
    text = text.replace("_", "__")
    text = text.replace(" ", "%20")
    return text


def find_settings_files(stanton_root: str):
    """Yield (folder_name, settings_json_path) for every Settings.json
    found anywhere under *stanton_root*."""
    for dirpath, _dirnames, filenames in os.walk(stanton_root):
        for filename in filenames:
            if filename.lower() == "settings.json":
                folder_name = os.path.basename(dirpath)
                yield folder_name, os.path.join(dirpath, filename)


def read_name_from_settings(settings_path: str) -> str | None:
    """Return the value of the top-level `name` key, or None on failure."""
    try:
        with open(settings_path, encoding="utf-8") as fh:
            data = json.load(fh)
        return data.get("name")
    except (json.JSONDecodeError, OSError) as exc:
        print(f"  WARNING: Could not read {settings_path}: {exc}", file=sys.stderr)
        return None


def update_badges_in_readme(readme_path: str, badge_map: dict[str, str]) -> bool:
    """Replace badge labels in *readme_path* using *badge_map*.

    *badge_map* maps folder_name -> URL-encoded label string.

    Returns True if any substitutions were made.
    """
    with open(readme_path, encoding="utf-8") as fh:
        content = fh.read()

    original = content
    for folder_name, encoded_label in badge_map.items():
        # Shields.io badge URL structure:
        #   /badge/<left_label>-<right_label>-<color>[?query]
        #
        # The encoded label itself may contain "--" (escaped hyphens) which
        # would confuse a pattern that uses "-" as a separator.  To avoid
        # that, we match the *current* label as "everything that isn't the
        # trailing -<color> segment", where the color segment is defined as a
        # single bare hyphen followed by one or more word/percent chars up to
        # the closing ")" or "?".
        #
        # Group 1: prefix  ...badge/<FOLDER>-
        # Group 2: current label  (greedy, but we make it give back the color)
        # Group 3: trailing -<color>[?query])
        #
        # The color segment is a bare "-" (not "--") followed by non-")"
        # chars, so we use a negative-lookbehind on group 3 to ensure the
        # hyphen that starts it is not itself preceded by another hyphen.
        pattern = (
            r"(!\[Static Badge\]\(https://img\.shields\.io/badge/"
            + re.escape(folder_name)
            + r"-)"          # group 1: up to and including the first separator dash
            + r"(.+?)"       # group 2: current label (non-greedy)
            + r"((?<!-)(?<!\-)-[a-zA-Z0-9%]+(?:\?[^)]*)?)\)"  # group 3: -color[?query])
        )

        def make_replacement(enc_label):
            def _replace(m):
                return f"{m.group(1)}{enc_label}{m.group(3)})"
            return _replace

        new_content, count = re.subn(
            pattern, make_replacement(encoded_label), content
        )
        if count:
            print(f"  Updated badge for '{folder_name}' -> '{encoded_label}' ({count} occurrence(s))")
            content = new_content
        else:
            print(f"  No badge found for folder '{folder_name}' – skipping.")

    if content != original:
        with open(readme_path, "w", encoding="utf-8") as fh:
            fh.write(content)
        return True

    return False


def main():
    parser = argparse.ArgumentParser(description="Update README badges from Settings.json files.")
    parser.add_argument(
        "--repo-root",
        default=os.getcwd(),
        help="Path to the repository root (default: current working directory)",
    )
    args = parser.parse_args()

    repo_root = os.path.abspath(args.repo_root)
    stanton_root = os.path.join(repo_root, "StantonCityPark")
    readme_path = os.path.join(repo_root, "README.md")

    if not os.path.isdir(stanton_root):
        print(f"ERROR: StantonCityPark directory not found at {stanton_root}", file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(readme_path):
        print(f"ERROR: README.md not found at {readme_path}", file=sys.stderr)
        sys.exit(1)

    print(f"Scanning for Settings.json files under: {stanton_root}")

    badge_map: dict[str, str] = {}
    for folder_name, settings_path in find_settings_files(stanton_root):
        print(f"  Found: {settings_path}")
        name = read_name_from_settings(settings_path)
        if name:
            encoded = url_encode_badge_label(name)
            # If multiple Settings.json files share the same parent folder name,
            # the last one found wins. In practice each folder name should be unique.
            badge_map[folder_name] = encoded
            print(f"    name='{name}'  encoded='{encoded}'")
        else:
            print(f"    WARNING: 'name' property missing in {settings_path}")

    if not badge_map:
        print("No valid Settings.json files found. Nothing to update.")
        sys.exit(0)

    print(f"\nUpdating badges in: {readme_path}")
    changed = update_badges_in_readme(readme_path, badge_map)

    if changed:
        print("\nREADME.md was updated successfully.")
    else:
        print("\nNo changes were needed in README.md.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Build assets/card.svg: colored ASCII cat on the left, neofetch-style info on the right.

    python3 card/make_card.py              # uses card/config.json
    python3 card/make_card.py --uptime 19  # override the uptime

Needs Pillow (pip install pillow). GitHub stats come from the public GitHub API;
if that fails, the last numbers in card/stats.json are used.
"""
import argparse, json, os, urllib.request
from html import escape
from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# ---- look -------------------------------------------------------------------
BG, BORDER = "#161b22", "#30363d"
KEY, VAL, DOT, TXT = "#ffa657", "#a5d6ff", "#616e7f", "#c9d1d9"
FONT = "ConsolasFallback, Consolas, 'SF Mono', Menlo, 'DejaVu Sans Mono', monospace"
FS, CW, LH = 16, 9.65, 20          # font size, char width, line height (px)
PANEL_W = 60                        # right panel width in characters
AFS, ACW, ALH = 10, 6.03, 12      # smaller font for the ASCII art = more detail
RAMP = " .'`^\",:;Il!i><~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


def ascii_art(path, rows, tint):
    im = Image.open(path).convert("RGBA")
    cols = round(rows * im.width / im.height * ALH / ACW)
    im = im.resize((cols, rows), Image.LANCZOS)
    rgb = ImageOps.autocontrast(im.convert("RGB"), cutoff=2); rgb.putalpha(im.getchannel("A")); im = rgb
    lines = []
    for y in range(rows):
        cells = []
        for x in range(cols):
            r, g, b, a = im.getpixel((x, y))
            if a < 110:
                cells.append((" ", None)); continue
            lum = (0.299 * r + 0.587 * g + 0.114 * b) / 255
            ch = RAMP[min(len(RAMP) - 1, int((0.18 + 0.82 * lum) * (len(RAMP) - 1)))]
            v = 0.35 + 0.65 * lum                # keep dark fur visible on a dark card
            if tint:                              # warm duotone, like an old photo
                lo, hi = (120, 92, 60), (255, 236, 205)
                col = tuple(round(lo[i] + (hi[i] - lo[i]) * v) for i in range(3))
            else:
                col = tuple(min(255, round(c * 0.65 + 255 * v * 0.35)) for c in (r, g, b))
            q = tuple(c // 8 * 8 for c in col)   # merge near colors into one tspan
            cells.append((ch, "#%02x%02x%02x" % q))
        lines.append(cells)
    return lines, cols


def github_stats(user):
    cache = os.path.join(HERE, "stats.json")
    try:
        def get(url):
            req = urllib.request.Request(url, headers={"User-Agent": "profile-card",
                                                       "Accept": "application/vnd.github+json"})
            with urllib.request.urlopen(req, timeout=15) as r:
                return json.load(r)
        u = get(f"https://api.github.com/users/{user}")
        repos = get(f"https://api.github.com/users/{user}/repos?per_page=100&type=owner")
        commits = get(f"https://api.github.com/search/commits?q=author:{user}&per_page=1")
        s = {"repos": u["public_repos"], "followers": u["followers"],
             "stars": sum(r["stargazers_count"] for r in repos),
             "commits": commits["total_count"]}
        json.dump(s, open(cache, "w"), indent=2)
        return s
    except Exception as e:
        print("GitHub API failed, using cached stats:", e)
        return json.load(open(cache))


# ---- right panel: list of lines, each a list of (text, color) -----------------
def kv(key, val, width=PANEL_W):
    dots = width - len(". ") - len(key) - 2 - len(val) - 1
    parts = [(". ", DOT)]
    for i, k in enumerate(key.split(".")):
        if i: parts.append((".", TXT))
        parts.append((k, KEY))
    return parts + [(":", TXT), (" " + "." * max(dots, 1) + " ", DOT), (val, VAL)]


def title(t):
    head = f"- {t} " if not t.endswith("@github") else f"{t} "
    return [(head, TXT), ("—" * (PANEL_W - len(head)), DOT)]


def panel(cfg, stats):
    out = [title(cfg["header"])]
    for sec in cfg["sections"]:
        if sec["title"]:
            out += [[], title(sec["title"])]
        for row in sec["rows"]:
            if row is None:
                out.append([(". ", DOT)]); continue
            out.append(kv(row[0], row[1].replace("{uptime}", str(cfg["uptime_years"]))))
    half = (PANEL_W - 3) // 2
    out += [[], title("GitHub Stats"),
            kv("Repos", f"{stats['repos']:,}", half) + [(" | ", TXT)] + kv("Stars", f"{stats['stars']:,}", half)[1:],
            kv("Commits", f"{stats['commits']:,}", half) + [(" | ", TXT)] + kv("Followers", f"{stats['followers']:,}", half)[1:]]
    return out


def tspans(parts):
    return "".join(f'<tspan fill="{c}">{escape(t)}</tspan>' if c else escape(t) for t, c in parts)


def build(cfg):
    stats = github_stats(cfg["github_user"])
    right = panel(cfg, stats)
    rows = len(right) + 2
    art_rows = int(rows * LH / ALH)
    art, cols = ascii_art(os.path.join(HERE, cfg.get("image", "cat.png")), art_rows, cfg.get("ascii_tint", True))

    pad = 30
    gap = 3 * CW
    width = round(pad * 2 + cols * ACW + gap + PANEL_W * CW)
    height = round(pad * 2 + rows * LH)
    x2 = pad + cols * ACW + gap
    y0 = pad + LH - 4

    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
           f'viewBox="0 0 {width} {height}" font-family="{FONT}" font-size="{FS}px">',
           f'<rect x="0.5" y="0.5" width="{width-1}" height="{height-1}" rx="15" fill="{BG}" stroke="{BORDER}"/>',
           f'<text xml:space="preserve" font-size="{AFS}px">']
    for i, cells in enumerate(art):           # left: ASCII art, runs of one color share a tspan
        runs, cur, buf = [], None, ""
        for ch, col in cells:
            if col is None:                    # a space can join any run
                col = cur
            if col != cur and buf:
                runs.append((buf, cur)); buf = ""
            cur = col
            buf += ch
        if buf: runs.append((buf, cur))
        svg.append(f'<tspan x="{pad}" y="{pad + ALH + i * ALH}">{tspans(runs)}</tspan>')
    svg.append('</text><text xml:space="preserve">')
    top = (rows - len(right)) // 2               # right: info panel, centered vertically
    for i, parts in enumerate(right):
        if parts:
            svg.append(f'<tspan x="{x2:.1f}" y="{y0 + (top + i) * LH}">{tspans(parts)}</tspan>')
    svg += ["</text>", "</svg>"]
    out = os.path.join(ROOT, "assets", "card.svg")
    open(out, "w").write("\n".join(svg) + "\n")
    print("wrote", out, f"({width}x{height})")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--uptime", type=int, help="years shown as Uptime")
    a = ap.parse_args()
    cfg = json.load(open(os.path.join(HERE, "config.json")))
    if a.uptime is not None:
        cfg["uptime_years"] = a.uptime
    build(cfg)

#!/usr/bin/env python3
"""Draw the 17 November 2026 world-news front page (1024x1024 PNG).

Pure Pillow, no network, deterministic: the same script always writes the
same bytes. The image is a newspaper front page: masthead with the date,
a lead story (Kerch Bridge) with a drawn illustration, two mid stories
(Iran/Bahrain, Xi-Trump-Putin summit) and three more (Israel vote, Japan
jets, Depardieu), plus an "also" strip. Every fact was checked against
reporting from 17 November 2026 (BBC/Reuters/AP via Just Security's Early
Edition, Algenom, Open Chronicle, TFI Online).
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 231)
INK = (22, 22, 22)
NAVY = (22, 40, 63)
RED = (179, 38, 30)
GOLD = (201, 162, 39)
RULE = (120, 110, 95)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, fill, max_w, leading):
    """Draw wrapped paragraph; returns y just below the last line."""
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def card(draw, x0, y0, x1, y1):
    draw.rectangle([x0, y0, x1, y1], fill=(255, 255, 255),
                   outline=INK, width=2)


def kicker(draw, x, y, text, color=RED, size=21):
    f = font(SANS_B, size)
    draw.text((x, y), text, font=f, fill=color)
    return y + size + 8


def headline(draw, x, y, text, max_w, size=34, leading=None):
    f = font(SERIF_B, size)
    return para(draw, x, y, text, f, INK, max_w,
                leading or int(size * 1.12))


def deck(draw, x, y, text, max_w, size=21, leading=None):
    f = font(SANS, size)
    return para(draw, x, y, text, f, (40, 40, 40), max_w,
                leading or int(size * 1.3))


# ---------------------------------------------------------------- illustration
def draw_bridge_scene(draw, x0, y0, x1, y1):
    """Stylised Kerch Bridge at dusk: a road span has fallen into the strait."""
    w, h = x1 - x0, y1 - y0
    horizon = y0 + int(h * 0.52)
    # dusk sky bands
    bands = [(46, 74, 107), (74, 96, 122), (140, 120, 90),
             (214, 158, 92), (232, 190, 120)]
    bh = (horizon - y0) // len(bands)
    for i, c in enumerate(bands):
        draw.rectangle([x0, y0 + i * bh, x1, y0 + (i + 1) * bh], fill=c)
    # sun low on the horizon
    sx, sy, sr = x0 + int(w * 0.78), horizon - 18, 26
    draw.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(240, 200, 110))
    # sea
    draw.rectangle([x0, horizon, x1, y1], fill=(31, 78, 107))
    for yy in range(horizon + 14, y1 - 8, 22):
        for xx in range(x0 + 8, x1 - 30, 46):
            draw.line([xx, yy, xx + 22, yy], fill=(90, 140, 170), width=2)
    deck_y = y0 + int(h * 0.38)
    # pylons
    for px in (x0 + int(w * 0.16), x0 + int(w * 0.84)):
        draw.rectangle([px - 5, deck_y - 62, px + 5, deck_y + 4], fill=(60, 60, 66))
        draw.line([px, deck_y - 62, x0 + int(w * 0.38), deck_y], fill=(90, 90, 96), width=2)
        draw.line([px, deck_y - 62, x0 + int(w * 0.62), deck_y], fill=(90, 90, 96), width=2)
    # deck: left span, right span, gap in the middle
    gap_l, gap_r = x0 + int(w * 0.40), x0 + int(w * 0.60)
    draw.rectangle([x0, deck_y, gap_l, deck_y + 10], fill=(52, 52, 58))
    draw.rectangle([gap_r, deck_y, x1, deck_y + 10], fill=(52, 52, 58))
    # fallen span, tilted into the water
    draw.polygon([(gap_l + 4, deck_y + 6), (gap_r - 30, deck_y + 52),
                  (gap_r - 8, deck_y + 66), (gap_l + 26, deck_y + 18)],
                 fill=(70, 70, 78))
    # explosion burst at the gap
    cx, cy = (gap_l + gap_r) // 2, deck_y - 6
    for r, c in ((34, (232, 120, 40)), (22, (240, 170, 60)), (12, (255, 220, 120))):
        pts = []
        for k in range(12):
            ang = k * 3.14159 / 6
            rr = r if k % 2 == 0 else r * 0.55
            pts.append((cx + rr * __import__("math").cos(ang),
                        cy + rr * __import__("math").sin(ang)))
        draw.polygon(pts, fill=c)
    # smoke plume (kept inside the scene)
    for (ox, oy, r, c) in ((cx - 26, deck_y - 46, 24, (120, 120, 120)),
                           (cx + 6, deck_y - 66, 28, (105, 105, 105)),
                           (cx + 30, deck_y - 84, 20, (130, 130, 130)),
                           (cx - 4, deck_y - 96, 13, (140, 140, 140))):
        draw.ellipse([ox - r, oy - r, ox + r, oy + r], fill=c)
    # caption
    draw.rectangle([x0, y1 - 26, x1, y1], fill=(22, 40, 63))
    draw.text((x0 + 10, y1 - 23),
              "The Kerch Bridge, Crimea",
              font=font(SANS, 17), fill=(255, 255, 255))


def draw_drone(draw, x, y, s, color):
    """Small quadcopter drone silhouette."""
    draw.ellipse([x + s * 0.35, y + s * 0.35, x + s * 0.65, y + s * 0.65],
                 fill=color)
    for dx, dy in ((0, 0), (s * 0.7, 0), (0, s * 0.7), (s * 0.7, s * 0.7)):
        draw.ellipse([x + dx, y + dy, x + dx + s * 0.3, y + dy + s * 0.3],
                     outline=color, width=3)
        draw.line([x + dx + s * 0.15, y + dy + s * 0.15,
                   x + s * 0.5, y + s * 0.5], fill=color, width=3)


def draw_flags(draw, x, y, s):
    """Three small flags: China, USA, Russia (abstract stripes)."""
    cols = [(222, 41, 16), (60, 90, 180), (200, 30, 30)]
    for i, c in enumerate(cols):
        fx = x + i * (s + 8)
        draw.rectangle([fx, y, fx + s, y + int(s * 0.62)], fill=c,
                       outline=INK, width=2)
        draw.line([fx + 2, y + int(s * 0.62), fx + s - 2, y + int(s * 0.62)],
                  fill=(255, 255, 255), width=3)
        draw.line([fx, y + int(s * 0.62), fx, y + s + 14], fill=INK, width=3)


# ------------------------------------------------------------------- the page
def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # masthead
    d.rectangle([0, 0, W, 104], fill=NAVY)
    d.text((W // 2, 12), "THE WORLD IN ONE IMAGE",
           font=font(SANS_B, 20), fill=GOLD, anchor="ma")
    d.text((W // 2, 40), "TUESDAY 17 NOVEMBER 2026",
           font=font(SERIF_B, 50), fill=(255, 255, 255), anchor="ma")
    d.line([24, 112, W - 24, 112], fill=RULE, width=2)

    # ---- lead story: Kerch Bridge
    card(d, 24, 122, 1000, 452)
    y = kicker(d, 48, 138, "WAR IN UKRAINE  —  LEAD STORY")
    y = headline(d, 48, y, "UKRAINE BRINGS DOWN THE KERCH BRIDGE",
                 500, size=44)
    y += 6
    y = deck(d, 48, y,
             "A second night of strikes collapses a road span into the "
             "strait and halts traffic. Russia hits Kyiv's bridges in reply.",
             500, size=22)
    deck(d, 48, y + 4,
         "Zelenskyy: \u201can unprecedented operation\u201d.",
         500, size=22)
    draw_bridge_scene(d, 580, 140, 976, 434)

    # ---- row 2: two half-width stories
    # Iran / Bahrain
    card(d, 24, 468, 500, 700)
    y = kicker(d, 44, 484, "MIDDLE EAST")
    draw_drone(d, 400, 478, 44, RED)
    y = headline(d, 44, y, "IRAN FIRES DRONES AT U.S. RADAR IN BAHRAIN",
                 412, size=32)
    deck(d, 44, y + 4,
         "Bahrain shot them down; no damage. U.S. intel reports a "
         "\u201cdirty bomb\u201d plot.",
         412, size=21)

    # Xi-Trump-Putin summit
    card(d, 524, 468, 1000, 700)
    y = kicker(d, 544, 484, "DIPLOMACY")
    draw_flags(d, 830, 480, 40)
    y = headline(d, 544, y, "XI, TRUMP AND PUTIN TO MEET IN SHENZHEN",
                 412, size=32)
    deck(d, 544, y + 4,
         "China confirms the first three-way summit, on Thursday on "
         "the sidelines of the APEC meeting it is hosting.",
         412, size=21)

    # ---- row 3: three stories
    cards = [
        (24, 344, "ISRAEL VOTES",
         "ISRAEL VOTES AMID CLAIMS",
         "Netanyahu allies accused over poll-day arrests; UK sanctions "
         "settlement builders."),
        (356, 676, "ASIA",
         "JAPAN SCRAMBLES JETS",
         "Two suspected Russian planes entered Japanese airspace; "
         "Tokyo protests strongly."),
        (688, 1000, "FRANCE",
         "DEPARDIEU PLEADS GUILTY",
         "French film star admits sexual assault in a Paris court "
         "and drops his appeal."),
    ]
    for x0, x1, kick, head, body in cards:
        card(d, x0, 712, x1, 952)
        y = kicker(d, x0 + 20, 728, kick, size=19)
        y = headline(d, x0 + 20, y, head, x1 - x0 - 40, size=27)
        deck(d, x0 + 20, y + 4, body, x1 - x0 - 40, size=19)

    # ---- footer strip
    d.rectangle([0, 964, W, H], fill=NAVY)
    d.text((W // 2, 976),
           "ALSO: Houthis reach the coast near Aden  \u2022  Tankers hit mines "
           "off Hormuz  \u2022  Mongolia's president quits",
           font=font(SANS, 19), fill=(255, 255, 255), anchor="ma")
    return img


if __name__ == "__main__":
    build().save("entry.png", optimize=True)
    print("wrote entry.png")

# news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/minhvo7332/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/minhvo7332/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

# Tuesday 17 November 2026 — the world's news in one image

A make.fun entry for competition `news-image-20261117`: sum up
17 November 2026's world news in one image.

## The image

A newspaper front page drawn programmatically with Pillow
(`draw_image.py`, deterministic — same script, same bytes):

- **Lead:** Ukraine brings down part of the Kerch Bridge — a second night
  of strikes collapses a road span into the strait; Russia hits Kyiv's
  bridges in reply.
- **Middle East:** Iran fires drones at a U.S. radar in Bahrain; U.S.
  intelligence reports a possible "dirty bomb" plot.
- **Diplomacy:** Xi, Trump and Putin to meet in Shenzhen — China confirms
  the first three-way summit, on Thursday on the APEC sidelines.
- **Israel votes** amid claims against Netanyahu allies; UK sanctions
  settlement builders.
- **Japan** scrambles fighter jets after suspected Russian aircraft enter
  its airspace.
- **France:** Depardieu pleads guilty in a Paris court.
- **Also:** Houthis reach the coast near Aden; tankers hit mines off
  Hormuz; Mongolia's president quits.

Every fact was checked against reporting from 17 November 2026
(BBC, Reuters, AP via Just Security's Early Edition, Algenom,
Open Chronicle). Attributed claims stay attributed ("U.S. intelligence
reports…").

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). No network, no
randomness: two runs write byte-identical output.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=vtp8qmbj&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>

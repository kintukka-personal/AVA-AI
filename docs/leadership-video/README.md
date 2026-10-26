# Leadership summary video

| Field | Value |
|---|---|
| Video | [`ava-leadership-summary.mp4`](ava-leadership-summary.mp4): 25 s, 1920×1080, 30 fps, original music and sound |
| Poster | [`ava-leadership-summary.jpg`](ava-leadership-summary.jpg) (also frame 0 of the video, so it shows as the thumbnail) |
| Share copy | [`share-copy.txt`](share-copy.txt) |
| Plan and storyboard | [`plan.md`](plan.md) |
| Made | 2026-10-26 |
| Status | For leadership. Not part of the live agent. |

## What it shows

1. **Problem:** 7–15 minutes hunting for the next step in D365, then a "How do I…" ticket anyway.
2. **AVA:** the front door to D365 Finance support, in Microsoft Teams, Microsoft 365 and SharePoint.
3. **In use:** a Teams chat in AVA's real answer format (cited PG and topic, Action/Description table, source link). Cited every time, never guesses, read-only.
4. **Specialists:** FIN, MAP, TAM and WIA.
5. **Results:** 3,113 conversations, 511 hours saved, 94.6% of answers rated good (last 180 days); 100% would keep using AVA, 4.6/5 usefulness, 60% send support fewer "How do I…" questions (pilot).
6. **Close:** "Ask AVA."

## Sources

| On screen | Source |
|---|---|
| 7–15 minutes | Gartner / IDC figure in the Ask Ava intro demo script (`archive/_text/comms-decks-business-case/`) |
| 3,113 · 511 hrs · 94.6% | `docs/analytics.md`, 180 days to 2026-10-23. Hours saved is Copilot Studio's estimate. |
| 100% · 4.6/5 · 60% | Pilot results, `docs/history.md` |
| Answer format, guardrails, child agents | `config/ava/instructions.md`, `docs/architecture.md` |
| Purchase Agreements example | Business case, `archive/_text/comms-decks-business-case/` |

The Teams window is a mock-up. The step rows are placeholder bars, not text from the Procedure Guide.

Left out on purpose: the credit-cost rise and the session drop in the last 90 days (see `docs/analytics.md` and `docs/open-items.md`).

## Re-rendering

Needs Node with Playwright, ffmpeg, and Python with numpy and scipy. In `source/`:

```bash
node render.js video video-noaudio.mp4   # frames from video.html
python3 audio.py score.wav               # music and sound effects
```

`video.html` loads `portrait.png` from the same folder (copy it from `docs/character-profile/`). Mux with ffmpeg, raising the audio by about 1.7 dB to reach -16 LUFS.

# Recording Rig — Camera + Body Mic + Screen, Synced

The hardware/software layer under [RECORDING.md](./RECORDING.md): how the Sony a6700, a
body mic, and the notebook screen become one synced recording — and where Zoom does and
does not fit.

## The architecture decision (read this first)

**OBS Studio is the master recorder. Zoom is, at most, a live-delivery endpoint.**

Three devices means three clocks; sync is the whole problem. The design principle:
**collapse clocks by aggregating upstream** — every signal that can travel *through*
another device before reaching the computer arrives pre-synced, and whatever remains is
fixed once with a measured offset in OBS. Recording as a live composite (rather than
separate files) means each 30–40 min session ends *finished*: no post-sync, no edit pass,
matching the one-take philosophy of [RECORDING.md](./RECORDING.md).

Why not Zoom as the recorder: Zoom re-compresses to ~1080p at low bitrate, applies
speech processing you can't undo, burns its layout into the recording, and gives no
multi-track audio. It is a meeting tool. Section 6 shows how to *feed* Zoom for a live
UF audience while OBS records the real master.

## 1. Signal chain (recommended: Tier 1)

```
body mic ──(2.4 GHz)──► receiver ──► a6700 (MI shoe or 3.5mm)
                                        │  audio embedded in camera stream
                                        ▼
                              USB-C (UVC/UAC, 4K30 or 1080p60)
                                        │
notebook screen ──(OBS display capture)─┤
                                        ▼
                                   OBS Studio ──► local MKV master
                                        │
                                        └──(virtual cam, optional)──► Zoom (live audience)
```

**Why route the mic through the camera:** the a6700's USB stream carries video *and*
audio (UVC/UAC) on one cable — mic-through-camera means voice and picture share one
clock and arrive as a single OBS source, **inherently lip-synced, forever, zero
calibration**. The only remaining offset is screen-vs-camera, which doesn't need
lip-sync precision (nobody notices a notebook scrolling 100 ms early).

### Camera settings (a6700)

| Setting | Value | Why |
|---|---|---|
| `USB Streaming` | 4K30 (or 1080p60) | native UVC/UAC — no capture card needed |
| USB cable | USB-C, 10 Gbps-rated, 2–3 m | the port is USB 3.2 Gen 2 with Power Delivery |
| Power | USB PD through the same port; keep a charged NP-FZ100 as buffer | 40 min sessions, no battery anxiety |
| `Auto Pwr OFF Temp` | **High** | prevents thermal shutdown on long takes |
| Picture profile | Off or S-Cinetone; **not** S-Log | you are not grading one-take lecture footage |
| Focus | AF-C + Face/Eye priority, wide area | you'll move; let the camera follow |
| Frame rate discipline | camera 30p ⇒ OBS canvas 30 fps ⇒ screen capture 30 fps | one timebase everywhere; use 1080p60 chain only if you want 60 |

### Body mic options (pick one)

| Option | Route | Sync story | ~Cost |
|---|---|---|---|
| **Sony ECM-W2BT / ECM-W3** | MI-shoe receiver, **digital** audio into camera — no cable | perfect (rides the camera stream) | $200–330 |
| DJI Mic 2 / Rode Wireless GO II | receiver → 3.5 mm into a6700 mic jack | perfect (same reason); set camera audio level ~4–7, disable camera wind filter, use the foam | $220–300 |
| Same kits, receiver → computer USB | appears as a USB audio interface in OBS | needs one measured offset vs the camera (see §3) — but frees the shoe and gives OBS a cleaner preamp path | same kit |

Recommendation: **through the camera** for the sync-free life. Move to receiver→computer
only if you hear preamp noise or want the shoe for something else.

## 2. OBS configuration

- **Canvas/output:** 3840×2160 @ 30 if recording the 4K stream (code legibility on
  YouTube is worth it — viewers zoom); otherwise 1920×1080 @ 30.
- **Recording:** *Hybrid MKV* (crash-safe, remuxes to MP4 automatically), NVENC/Apple
  HW encoder, CQ ~20 / ~40 Mbps at 4K.
- **Audio tracks:** Track 1 = full mix (upload-ready), Track 2 = mic only, Track 3 =
  desktop audio only. Costs nothing; rescues everything.
- **Mic filters** (on the camera source's audio): Noise Suppression (RNNoise) →
  Compressor (~4:1, −18 dB threshold) → Limiter (−3 dB). Skip the first if the room is
  quiet.
- **Desktop audio:** mute by default — notebook demos are silent; unmute deliberately
  for the [audio-DSP workshops](./Intro_DSP/Audio_Speech_DSP.ipynb) where sound *is*
  the content.

### Scenes (mapped to RECORDING.md's video structure)

| Scene | Layout | Used for |
|---|---|---|
| `A — Face` | camera full-frame | hook, session card, recap |
| `B — Lab` | notebook full + camera PiP (bottom-right, ~22%, subtle border) | rigor / live coding — the workhorse |
| `C — Split` | camera left ⅓, notebook right ⅔ | 💡 intuition cells, whiteboard-style moments |
| `D — Screen only` | notebook full, no PiP | dense plots/tables where the PiP would cover data |

Bind scenes to hotkeys (or a Stream Deck later); switching live *is* the edit.
Notebook prep per [RECORDING.md](./RECORDING.md): fresh kernel, font zoomed twice,
toolbar hidden.

## 3. Sync: formal procedure

**Case A — mic through camera (recommended):** voice/picture sync is automatic.
Screen-vs-camera offset is cosmetic; ignore unless visibly odd.

**Case B — mic receiver into the computer:** one 5-minute calibration, once per setup:

1. Record 10 s in OBS while clapping sharply on camera three times.
2. Open the recording; measure the gap between the clap *frame* (camera) and the clap
   *transient* (mic track). USB-UVC video typically lags a direct USB mic by
   ~100–200 ms.
3. Enter that value as a **positive Sync Offset (ms)** on the *mic* source
   (Advanced Audio Properties). Re-test; iterate once. Re-run only if cables, hub, or
   resolution change.

**Case C — belt-and-suspenders (optional, for irreplaceable takes):** swap the USB path
for micro-HDMI → capture card (Elgato Cam Link 4K class, ~$100–130), which lets the
a6700 *also record internally* to its SD card as a full-quality backup while OBS
records the composite. If the master is ever damaged, auto-align the backup by audio
waveform in DaVinci Resolve (free) — the clap slate at the top of each take exists for
exactly this. (Verify internal-record-during-HDMI-out on the body with your firmware
before relying on it.)

## 4. Pre-flight checklist (per session)

- [ ] Camera: USB Streaming mode, PD power connected, temp setting High, eye-AF on
- [ ] Mic: fresh charge, foam on, level check while speaking at lecture volume (peaks ~−12 dB in OBS)
- [ ] One sharp **clap on camera** after hitting record (sync slate + take marker)
- [ ] Notebook: fresh kernel, all cells pre-run once, font zoomed, do-not-disturb on the OS
- [ ] OBS: correct scene collection, disk space > 20 GB, *Start Recording* (not just streaming)
- [ ] 10-second test recording reviewed for audio **before** the real take

## 5. Shopping list

| Tier | Items | ~Cost |
|---|---|---|
| **$0 — try tonight** | USB-C cable you own + any wired lav/USB mic + OBS | $0 |
| **Core (recommended)** | 10 Gbps USB-C cable (3 m) · wireless mic kit (ECM-W2BT / DJI Mic 2 / GO II) · spare NP-FZ100 | ~$250–380 |
| **Robustness (optional)** | Cam Link 4K-class capture card · micro-HDMI→HDMI cable · dummy-battery AC coupler | ~$170 |
| **Comfort (optional)** | key light (Elgato/Amaran class) · compact tripod/desk mount · Stream Deck for scenes | ~$150–350 |

## 6. Zoom's actual roles

| Role | Verdict | How |
|---|---|---|
| Master recorder | **No** — compressed, processed, layout burned in, single audio track | — |
| **Live delivery to a UF audience while recording the master** | Yes — the right use | OBS *Start Virtual Camera* → select "OBS Virtual Camera" in Zoom video; route OBS mix via **VB-Cable** (Win) / **BlackHole** (macOS) as Zoom's mic; screen-share nothing (the notebook is already in the OBS scene). Zoom's cloud recording becomes a free low-res backup. |
| Remote guest lecturer | Yes | capture the Zoom window as one more OBS source; put the guest in scene `C` |

**Bottom line:** Zoom never touches the master. The master is OBS's local MKV —
multi-track, full-resolution, finished the moment you stop recording — which is what
[VIDEO_PLAN.md](./VIDEO_PLAN.md)'s 211 videos deserve.

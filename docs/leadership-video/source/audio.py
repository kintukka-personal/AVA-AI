# Original score + sound design for the AVA leadership video.
# 100 BPM (beat 0.6 s), D major. Scene cuts: 3.6, 6.6, 12.0, 15.0, 22.2. Length 25.0 s.
import sys
import numpy as np
from scipy.signal import butter, sosfilt, fftconvolve
from scipy.io import wavfile

SR = 48000
DUR = 25.0
N = int(SR * (DUR + 3))
rng = np.random.default_rng(7)
BEAT = 0.6

def tt(sec): return np.arange(int(sec * SR)) / SR
def hz(name):
    names = {'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11}
    p, o = name[:-1], int(name[-1])
    return 440 * 2 ** ((names[p] + 12 * (o + 1) - 69) / 12)
def lp(x, f, order=2): return sosfilt(butter(order, f, 'low', fs=SR, output='sos'), x)
def hp(x, f, order=2): return sosfilt(butter(order, f, 'high', fs=SR, output='sos'), x)
def bp(x, lo, hi, order=2): return sosfilt(butter(order, [lo, hi], 'band', fs=SR, output='sos'), x)

class Bus:
    def __init__(self): self.L = np.zeros(N); self.R = np.zeros(N)
    def add(self, sig, t0, gain=1.0, pan=0.0):
        i = int(round(t0 * SR))
        if i >= N: return
        s = sig[:N - i]
        a = (pan + 1) * np.pi / 4
        self.L[i:i + len(s)] += s * gain * np.cos(a) * 1.4142
        self.R[i:i + len(s)] += s * gain * np.sin(a) * 1.4142

pad, keys, bass, drums, sfx, send = Bus(), Bus(), Bus(), Bus(), Bus(), Bus()

# ---------- instruments ----------
def pad_note(f, dur, att=0.6, rel=1.2):
    t = tt(dur + rel)
    s = np.zeros_like(t)
    for det in (-0.06, 0.0, 0.06):
        ff = f * 2 ** (det / 12)
        ph = rng.random() * 6.283
        for h in range(1, 9):
            if ff * h > 9000: break
            s += np.sin(2 * np.pi * ff * h * t + ph * h) / h ** 1.6
    env = np.ones_like(t)
    a = t < att; env[a] = np.sin(t[a] / att * np.pi / 2) ** 2
    r = t > dur; env[r] = np.cos(np.clip((t[r] - dur) / rel, 0, 1) * np.pi / 2) ** 2
    lfo = 1 + 0.07 * np.sin(2 * np.pi * 0.27 * t + rng.random() * 6)
    return s * env * lfo / 3

def pluck(f, dur=1.8, bright=1.0):
    t = tt(dur)
    s = np.zeros_like(t)
    for h, a in [(1, 1), (2, .42), (3, .2), (4, .1), (5, .05), (6, .025)]:
        s += a * np.exp(-t * (2.0 + 1.6 * h * bright)) * np.sin(2 * np.pi * f * h * (1 + 0.0003 * h * h) * t)
    s *= 1 - np.exp(-t / 0.003)
    s *= np.clip((dur - t) / 0.08, 0, 1)
    return s

def bell(f, dur=2.4):
    t = tt(dur)
    s = np.zeros_like(t)
    for r, a, d in [(1, 1, 1.1), (2.0, .38, 1.7), (2.76, .26, 2.4), (5.4, .1, 3.6), (8.93, .04, 5.5)]:
        s += a * np.exp(-t * d) * np.sin(2 * np.pi * f * r * t)
    return s * (1 - np.exp(-t / 0.002))

def bass_note(f, dur):
    t = tt(dur + 0.25)
    s = np.sin(2 * np.pi * f * t) + 0.28 * np.sin(4 * np.pi * f * t) + 0.08 * np.sin(6 * np.pi * f * t)
    env = np.minimum(1, t / 0.025) * np.where(t > dur, np.exp(-(t - dur) / 0.06), 1.0)
    return np.tanh(1.3 * s * env) / 1.1

def kick():
    t = tt(0.5)
    f = 46 + 75 * np.exp(-t * 30)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 7)
    s += 0.06 * lp(rng.standard_normal(len(t)), 3000) * np.exp(-t * 250)
    return s

def shaker():
    t = tt(0.07)
    return hp(rng.standard_normal(len(t)), 7000) * np.exp(-t * 70) * np.minimum(1, t / 0.004)

def snap():
    t = tt(0.25)
    s = bp(rng.standard_normal(len(t)), 1400, 5200) * np.exp(-t * 30)
    s += 0.4 * np.sin(2 * np.pi * 190 * t) * np.exp(-t * 45)
    return s

def tick(f=1760, d=160):
    t = tt(0.08)
    return (np.sin(2 * np.pi * f * t) * 0.7 + 0.3 * hp(rng.standard_normal(len(t)), 4000)) * np.exp(-t * d)

def keyclick():
    t = tt(0.03)
    s = hp(rng.standard_normal(len(t)), 2500) * np.exp(-t * 420)
    s += 0.5 * np.sin(2 * np.pi * 240 * t) * np.exp(-t * 300)
    return s

def sweep_noise(dur, f0, f1, shape):
    """Noise through a one-pole lowpass whose cutoff glides f0 -> f1 (exp)."""
    n = int(dur * SR)
    x = rng.standard_normal(n)
    y = np.zeros(n)
    fc = f0 * (f1 / f0) ** (np.arange(n) / n)
    a = np.exp(-2 * np.pi * fc / SR)
    z = 0.0
    for i in range(n):
        z = (1 - a[i]) * x[i] + a[i] * z
        y[i] = z
    y = hp(y, 150)
    return y * shape(np.arange(n) / n)

def whoosh(dur=0.6, f0=500, f1=4500):
    return sweep_noise(dur, f0, f1, lambda u: np.sin(np.pi * u) ** 2.2)

# ---------- score ----------
CH = {
    'D':  ['D3', 'A3', 'D4', 'F#4'], 'Bm': ['B2', 'F#3', 'B3', 'D4'],
    'G':  ['G2', 'D3', 'B3', 'D4'],  'A':  ['A2', 'E3', 'A3', 'C#4'],
}
ARP = {
    'D':  ['D4', 'F#4', 'A4', 'D5', 'A4', 'F#4', 'A4', 'D5'],
    'Bm': ['B3', 'D4', 'F#4', 'B4', 'F#4', 'D4', 'F#4', 'B4'],
    'G':  ['G3', 'B3', 'D4', 'G4', 'D4', 'B3', 'D4', 'B4'],
    'A':  ['A3', 'C#4', 'E4', 'A4', 'E4', 'C#4', 'E4', 'C#5'],
}
ROOT = {'D': 'D2', 'Bm': 'B1', 'G': 'G1', 'A': 'A1'}
BAR = 4 * BEAT
bars = [(3.6 + i * BAR, c) for i, c in enumerate(['D', 'Bm', 'G', 'A', 'D', 'Bm', 'G', 'A'])]
END = 3.6 + 8 * BAR  # 22.8, final chord

# intro: Bm pad, dark, with clock ticks on 8ths (matching the file highlight)
intro = np.zeros(int(4.6 * SR))
for nm in CH['Bm']:
    s = pad_note(hz(nm), 3.4, att=0.25, rel=1.0)
    intro[:len(s)] += s
pad.add(lp(intro, 650) * 1.0, 0.0, 0.5)
for k in range(12):
    t0 = k * 0.3
    if t0 > 3.35: break
    acc = k % 2 == 0
    sfx.add(tick(1760 if acc else 2349, 170), t0, 0.050 if acc else 0.028, pan=-0.25 if acc else 0.25)
# soft low pulse on beats under the ticks
for k in range(6):
    t = tt(0.4)
    sfx.add(np.sin(2 * np.pi * 61.7 * t) * np.exp(-t * 11) * np.minimum(1, t / 0.01), k * BEAT, 0.16)
# riser into the reveal
rs = sweep_noise(1.5, 250, 6000, lambda u: (u ** 2.4) * np.clip((1 - u) / 0.04, 0, 1))
sfx.add(rs, 3.6 - 1.5, 0.085)
send.add(rs, 3.6 - 1.5, 0.05)

# main progression
for bi, (t0, c) in enumerate(bars):
    for j, nm in enumerate(CH[c]):
        s = pad_note(hz(nm), BAR - 0.1, att=0.45 if bi else 0.12, rel=1.3)
        pan = [-0.55, 0.55, -0.25, 0.3][j]
        pad.add(s, t0, 0.38, pan)
    # air layer for the results section
    if t0 >= 15.0:
        for nm, pn in [(ARP[c][3], -0.6), (ARP[c][2].replace('4', '5').replace('3', '4'), 0.6)]:
            pad.add(pad_note(hz(nm), BAR - 0.1, att=0.8, rel=1.2), t0, 0.12, pn)
    # bass: half notes from bar 0, with a pickup eighth from bar 2
    r = hz(ROOT[c]) * 2
    bass.add(bass_note(r, BEAT * 1.9), t0, 0.32)
    bass.add(bass_note(r, BEAT * 1.4), t0 + 2 * BEAT, 0.26)
    if bi >= 2:
        bass.add(bass_note(r * 1.4983, BEAT * 0.4), t0 + 3.5 * BEAT, 0.16)
    # keys: quarters in bar 0, eighths after
    for k in range(8):
        if bi == 0 and k % 2: continue
        nm = ARP[c][k]
        vel = 1.0 if k % 2 == 0 else 0.62
        if k == 0: vel = 1.15
        s = pluck(hz(nm), 1.6, bright=0.9)
        keys.add(s, t0 + k * BEAT / 2, 0.105 * vel, pan=(-0.35 + 0.1 * k))
        send.add(s, t0 + k * BEAT / 2, 0.06 * vel)

# drums
kicks = []
t = 6.0
while t < END - 0.01:
    on_all = t >= 13.2
    beat_idx = round((t - 3.6) / BEAT) % 4
    if on_all or beat_idx in (0, 2):
        kicks.append(t)
    t += BEAT
kicks.append(END)
for k in kicks:
    drums.add(kick(), k, 0.42)
t = 8.4
while t < END - 0.01:
    drums.add(shaker(), t + BEAT / 2, 0.05, pan=0.3)
    if t >= 15.0: drums.add(shaker(), t, 0.022, pan=-0.3)
    t += BEAT
t = 13.2 + BEAT
while t < END:
    drums.add(snap(), t, 0.085, pan=0.05); send.add(snap(), t, 0.05)
    t += 2 * BEAT

# reveal impact
t = tt(1.6)
boom = np.sin(2 * np.pi * (38 + 20 * np.exp(-t * 6)) * t) * np.exp(-t * 2.6)
sfx.add(boom, 3.6, 0.34)
sfx.add(bell(hz('D6'), 2.6), 3.62, 0.05, -0.2); send.add(bell(hz('D6'), 2.6), 3.62, 0.08)
sfx.add(bell(hz('A6'), 2.6), 3.66, 0.03, 0.25); send.add(bell(hz('A6'), 2.6), 3.66, 0.05)

# portrait flights
for t0, d, f0, f1 in [(6.3, 0.65, 600, 4200), (11.75, 0.65, 500, 4000), (14.62, 0.6, 800, 3500), (21.9, 0.75, 400, 3800)]:
    w = whoosh(d, f0, f1)
    sfx.add(w, t0, 0.07, pan=-0.2); send.add(w, t0, 0.05)
# window slide up
sfx.add(whoosh(0.4, 300, 1800), 6.5, 0.035)

# typing: 45 characters, 7.1 -> 8.2
Q = 'How do I create a purchase agreement in D365?'
for i in range(1, len(Q) + 1):
    tc = 7.1 + (i / len(Q)) * 1.1
    if Q[i - 1] == ' ' and rng.random() < 0.5: continue
    sfx.add(keyclick(), tc, 0.05 * (0.6 + 0.4 * rng.random()), pan=0.15 * (rng.random() - .5))
# send + answer
sfx.add(pluck(hz('A5'), 0.5, 1.6), 8.4, 0.06); send.add(pluck(hz('A5'), 0.5), 8.4, 0.05)
sfx.add(bell(hz('D6')), 9.0, 0.07, -0.15); send.add(bell(hz('D6')), 9.0, 0.09)
sfx.add(bell(hz('F#6')), 9.06, 0.04, 0.2); send.add(bell(hz('F#6')), 9.06, 0.05)
# guardrail chips (over the G bar)
for k, nm in enumerate(['D6', 'G6', 'B6']):
    s = pluck(hz(nm), 0.9, 1.4)
    sfx.add(s, 9.9 + k * 0.15, 0.045, pan=0.35); send.add(s, 9.9 + k * 0.15, 0.05)
# specialist nodes (over the A bar)
for k, nm in enumerate(['A4', 'C#5', 'E5', 'A5']):
    s = pluck(hz(nm), 1.2, 1.1)
    sfx.add(s, 12.3 + k * 0.15, 0.08, pan=[-0.5, 0.5, -0.5, 0.5][k]); send.add(s, 12.3 + k * 0.15, 0.06)
# results: count ticks then a bell as each row lands
for k, f in enumerate(['A6', 'B6', 'C#7', 'D7', 'E7']):
    sfx.add(tick(hz(f), 220), 15.45 + k * 0.15, 0.022, pan=0.2)
sfx.add(bell(hz('B5')), 16.2, 0.05); send.add(bell(hz('B5')), 16.2, 0.07)
lift = sweep_noise(0.9, 300, 4500, lambda u: (u ** 2) * np.clip((1 - u) / 0.05, 0, 1))
sfx.add(lift, 17.1, 0.05); send.add(lift, 17.1, 0.04)
for k, f in enumerate(['G6', 'A6', 'B6', 'D7', 'E7']):
    sfx.add(tick(hz(f), 220), 17.85 + k * 0.15, 0.022, pan=-0.2)
sfx.add(bell(hz('D6')), 18.6, 0.05); send.add(bell(hz('D6')), 18.6, 0.07)

# final chord
fin = np.zeros(int(4 * SR))
for j, nm in enumerate(['D4', 'F#4', 'A4', 'D5', 'F#5', 'A5']):
    s = pluck(hz(nm), 2.6, 0.7)
    keys.add(s, END + j * 0.05, 0.11, pan=-0.4 + 0.16 * j); send.add(s, END + j * 0.05, 0.08)
for nm in ['D3', 'A3', 'D4', 'F#4', 'A4']:
    pad.add(pad_note(hz(nm), 1.6, att=0.1, rel=1.2), END, 0.3)
bass.add(bass_note(hz('D2') * 2, 1.6), END, 0.32)
sfx.add(bell(hz('D6'), 2.6), END, 0.06); send.add(bell(hz('D6'), 2.6), END, 0.1)
sfx.add(boom, END, 0.2)

# ---------- mix ----------
def st(b): return np.stack([b.L, b.R])
# sidechain: pad + bass breathe with the kick
duck = np.ones(N)
tN = np.arange(N) / SR
for k in kicks:
    m = tN >= k
    duck[m] -= 0.32 * np.exp(-(tN[m] - k) / 0.14)
duck = np.clip(duck, 0.55, 1)
padm = np.stack([hp(lp(pad.L, 2600), 130), hp(lp(pad.R, 2600), 130)]) * duck * 0.17
bassm = np.stack([lp(bass.L, 900), lp(bass.R, 900)]) * duck * 0.36
keysm = np.stack([lp(keys.L, 5200), lp(keys.R, 5200)]) * 1.0
drumsm = st(drums) * 0.7
sfxm = st(sfx) * 1.0

# reverb: synthetic stereo hall
irt = tt(2.6)
ir = []
for ch in range(2):
    nz = lp(rng.standard_normal(len(irt)), 5500) * np.exp(-irt / 0.62)
    nz[:int(0.018 * SR)] = 0
    ir.append(nz / np.sqrt(np.sum(nz ** 2)))
wet_in = st(send) + 0.35 * padm
wet = np.stack([fftconvolve(wet_in[c], ir[c])[:N] for c in range(2)]) * 0.55

mix = padm + bassm + keysm + drumsm + sfxm + wet
for nm,x in [('pad',padm),('bass',bassm),('keys',keysm),('drums',drumsm),('sfx',sfxm),('wet',wet)]:
    print(nm,'peak %.3f rms %.4f'%(np.max(np.abs(x)),np.sqrt(np.mean(x**2))))
mix = mix[:, :int(DUR * SR)]
# fade the tail into the end
tf = np.arange(mix.shape[1]) / SR
fade = np.clip((DUR - tf) / 0.75, 0, 1) ** 1.5
mix *= fade
mix = np.stack([hp(mix[0], 28), hp(mix[1], 28)])
# gentle bus glue
mix *= 0.5 / np.max(np.abs(mix))
mix = np.tanh(mix * 1.6) / np.tanh(1.6) * 0.9
wavfile.write(sys.argv[1], SR, (mix.T * 32767).astype(np.int16))
print('ok', mix.shape, float(np.sqrt(np.mean(mix ** 2))))

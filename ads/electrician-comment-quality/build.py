"""Southline Meta ads for electricians: hook -> open loop -> relate -> body -> solution -> 'Comment QUALITY'. 9:16.
Run:  python3 build.py   ->  southline_electricians_comment_quality.mp4 (+ _preview.png)"""
import math
from PIL import Image, ImageDraw
import adkit as A
from adkit import W, eo, eio, spring, clamp, put, put_rise, text, pill, sprite, shadowed, font, tsize, fit_size

GOLD, GOLD2, RED = (229, 166, 79), (255, 216, 150), (232, 72, 72)
A.set_theme("ember",
            bg=((14, 50, 40), (5, 18, 14)),
            blobs=[(840, 420, 520, (194, 117, 26), 0.30), (180, 1500, 520, (47, 166, 129), 0.22)],
            ink=(238, 243, 240), muted=(160, 188, 175), accent=GOLD, accent2=GOLD2,
            card=(17, 42, 35), card_ink=(238, 243, 240), grid=True, light=False, grad_buttons=True)
GRAD = (GOLD, GOLD2, 0)


def with_pill(scene, label, at, y, bg=(17, 17, 16)):
    """overlay a popping pill on any scene (used for the open-loop teaser)"""
    dur, fn, ev = scene
    sp = shadowed(pill(label, 38, bg), blur=16, dy=10, alpha=80, pad=30)
    def f2(t):
        im, sh = fn(t)
        if t >= at: put(im, sp, W / 2, y, eo((t - at) / 0.25), 0.8 + 0.2 * spring((t - at) / 0.45))
        return im, sh
    return dur, f2, ev + [(at, "pop", 0.7)]


def with_text(scene, lines, at, y0):
    """overlay rising lines on any scene. lines = [(text, weight, size, colour|'grad')]"""
    dur, fn, ev = scene
    sps = [text(a, w, fit_size(a, w, sz), grad=GRAD) if c == "grad" else text(a, w, fit_size(a, w, sz), c) for a, w, sz, c in lines]
    def f2(t):
        im, sh = fn(t); y = y0
        for i, sp in enumerate(sps): put_rise(im, sp, W / 2, y, eo((t - at - i * 0.15) / 0.3)); y += sp.height * 1.05
        return im, sh
    return dur, f2, ev + [(at, "swish", 0.5)]


# ---------- RELATE: the late-night quoting text thread ----------
def bubble(msg, out):
    f = font("m", 84); tw, th, ox, oy = tsize(msg, f); w, h = tw // 2 + 84, 112
    fill, fg = (GOLD, (24, 18, 8)) if out else ((240, 243, 241), (17, 17, 16))
    def fn(d, s, im):
        d.rounded_rectangle((0, 0, w * s - 1, h * s - 1), 46 * s, fill=fill)
        d.text((42 * s - ox, h * s / 2 - th / 2 - oy), msg, font=f, fill=fg)
    return shadowed(sprite(w, h, fn), blur=14, dy=8, alpha=70, pad=30)

def typing_bubble(t):
    w, h = 150, 96
    def fn(d, s, im):
        d.rounded_rectangle((0, 0, w * s - 1, h * s - 1), 44 * s, fill=(240, 243, 241))
        for k in range(3):
            a = 0.35 + 0.65 * (0.5 + 0.5 * math.sin(t * 14 - k * 1.1))
            c = int(170 - 90 * a); d.ellipse(((42 + k * 34 - 10) * s, 38 * s, (42 + k * 34 + 10) * s, 58 * s), fill=(c, c, c))
    return sprite(w, h, fn)

def scene_text_thread(l1, l2, msgs, verdict, dur=4.4):
    """msgs = [(text, outgoing_bool, t)]; incoming messages get a typing indicator first"""
    s1, s2 = text(l1, "xb", fit_size(l1, "xb", 84)), text(l2, "bl", fit_size(l2, "bl", 108), grad=GRAD)
    sps = [bubble(m, o) for m, o, _ in msgs]; Y0, STEP = 640, 140
    VT = msgs[-1][2] + 0.6; vp = shadowed(pill(verdict, 44, RED, w="xb"), blur=18, dy=10, alpha=80, pad=30)
    def fn(t):
        im = A.bg(); put_rise(im, s1, W / 2, 320, eo(t / 0.32)); put_rise(im, s2, W / 2, 430, eo((t - 0.22) / 0.32))
        for i, ((m, out, ta), sp) in enumerate(zip(msgs, sps)):
            y = Y0 + i * STEP
            x = (W - 70 - (sp.width - 60) / 2) if out else (70 + (sp.width - 60) / 2)
            if not out and ta - 0.4 <= t < ta:
                tb = typing_bubble(t); put(im, tb, 70 + tb.width / 2, y, eo((t - ta + 0.4) / 0.12))
            if t >= ta:
                k = (t - ta) / 0.4; put(im, sp, x + (40 if out else -40) * (1 - eo(k)), y + 30 * (1 - eo(k)), clamp(k / 0.2), 0.85 + 0.15 * spring(k))
        if t >= VT: put(im, vp, W / 2, Y0 + len(msgs) * STEP + 110, 1, 0.7 + 0.3 * spring((t - VT) / 0.45))
        return im, (8 * (1 - (t - VT) / 0.15) if 0 <= t - VT < 0.15 else 0)
    ev = [(0.0, "whoosh", 0.5)] + [(ta, "swish" if o else "pop", 0.6) for _, o, ta in msgs] + [(VT, "hit", 0.9)]
    return dur, fn, ev


# ---------- BODY: the lead filter (answers the open loop) ----------
def scene_filter(l1, l2, chips, closer, dur=4.8, interval=0.36):
    """chips = [(label, good_bool)]; bad ones bounce off the funnel, good ones drop through and line up"""
    s1, s2 = text(l1, "xb", fit_size(l1, "xb", 84)), text(l2, "bl", fit_size(l2, "bl", 104), grad=GRAD)
    cl = text(closer, "xb", fit_size(closer, "xb", 66))
    sp = [pill(c, 44, None, grad=(GOLD, GOLD2, 0), w="b") if good else pill(c, 44, (58, 74, 68), fg=(190, 205, 198), w="b") for c, good in chips]
    sp = [shadowed(s, blur=12, dy=8, alpha=70, pad=24) for s in sp]
    T = [0.55 + i * interval for i in range(len(chips))]; XO = [-150, 130, -70, 180, -180, 70, 150, -110]
    slots = [(W / 2 - 220, 1240), (W / 2 + 220, 1240), (W / 2 - 220, 1370), (W / 2 + 220, 1370)]
    gi = {}; n = 0
    for i, (_, g) in enumerate(chips):
        if g: gi[i] = n; n += 1
    MY, SY = 800, 1060
    fun = Image.new("RGBA", (W, A.H), (0, 0, 0, 0)); d = ImageDraw.Draw(fun)
    poly = [(W / 2 - 330, 760), (W / 2 + 330, 760), (W / 2 + 70, 1040), (W / 2 + 70, 1110), (W / 2 - 70, 1110), (W / 2 - 70, 1040)]
    d.polygon(poly, fill=GOLD + (28,)); d.line(poly + [poly[0]], fill=GOLD + (230,), width=6, joint="curve")
    CT = T[-1] + 1.0
    def fn(t):
        im = A.bg(); put_rise(im, s1, W / 2, 320, eo(t / 0.32)); put_rise(im, s2, W / 2, 430, eo((t - 0.22) / 0.32))
        im.alpha_composite(fun); sh = 0
        for i, ((_, good), s) in enumerate(zip(chips, sp)):
            p = t - T[i]
            if p < 0: continue
            x0 = W / 2 + XO[i % len(XO)]
            if p < 0.35:
                k = eio(p / 0.35); put(im, s, x0, 580 + (MY - 580) * k, clamp(p / 0.1)); continue
            if not good:
                q = clamp((p - 0.35) / 0.5); dirn = 1 if XO[i % len(XO)] >= 0 else -1
                if q < 1: put(im, s, x0 + dirn * 460 * eo(q), MY - 140 * math.sin(math.pi * q) + 220 * q, 1 - q, 1, -dirn * 50 * q)
                if 0 <= p - 0.35 < 0.1: sh = 5
            else:
                if p < 0.65:
                    q = eio((p - 0.35) / 0.3); put(im, s, x0 + (W / 2 - x0) * q, MY + (SY + 60 - MY) * q, 1, 1 - 0.15 * q)
                else:
                    q = (p - 0.65) / 0.45; sx, sy = slots[gi[i]]
                    put(im, s, W / 2 + (sx - W / 2) * eo(q), SY + 60 + (sy - SY - 60) * eo(q), 1, 0.85 + 0.15 * spring(q))
        if t >= CT: put_rise(im, cl, W / 2, 1520, eo((t - CT) / 0.3))
        return im, sh
    ev = [(0.0, "whoosh", 0.5)] + [(T[i] + 0.35, "pop" if g else "click", 0.7 if g else 0.8) for i, (_, g) in enumerate(chips)] + \
         [(T[i] + 0.7, "coin", 0.5) for i, (_, g) in enumerate(chips) if g] + [(CT, "shimmer", 0.7)]
    return dur, fn, ev


# ---------- the ad ----------
v = A.Video()
# 1. HOOK: pattern interrupt + callout
v.add(*with_text(A.scene_dot_matrix(["STOP BUYING", "SHARED", "LEADS."], color=GOLD, dur=1.9),
                 [("Electricians,", "bl", 96, "grad"), ("watch this first.", "xb", 72, (238, 243, 240))], 0.3, 1290))
# 2. OPEN LOOP: a question we only answer in the body
v.add(*with_pill(A.scene_kinetic([("Why does one sparky", "xb", 84, None),
                                  ("only quote big jobs…", "bl", 104, "grad"),
                                  ("while you price sockets?", "xb", 80, (160, 188, 175))],
                                 dur=3.0, y0=700, stagger=0.4, underline_line=1),
                 "The answer's simpler than you think", 1.55, 1130))
# 3. RELATE: the evening they've all had
v.add(*scene_text_thread("9:47pm. Still quoting.", "Sound familiar?",
                         [("How much to move one socket?", False, 0.65),
                          ("€90. Can do Thursday.", True, 1.3),
                          ("Ah. Got someone for €60.", False, 2.05),
                          ("Just wanted a ballpark tbh", False, 2.7)],
                         "Another unpaid evening."))
# 4. BODY: answer the open loop, their leads are filtered
v.add(*scene_filter("The difference?", "Their leads get filtered.",
                    [("Full rewire", True), ("Move a socket", False), ("EV charger", True), ("Cheapest price?", False),
                     ("Just a ballpark", False), ("Solar PV", True), ("Fuse board", True), ("40km away", False)],
                    "Only real jobs reach the phone."))
# 5. SOLUTION: what Southline builds for them
v.add(*A.scene_float_cards("We build it for you.",
                           [("YOUR META ADS", "Big jobs", "Rewires · EV · solar PV", False),
                            ("EVERY LEAD", "Filtered", "Job, area, timing checked", True),
                            ("STRAIGHT TO", "Your phone", "Name, number, job", False)], dur=4.0))
# 6. CTA: comment keyword
v.add(*A.scene_cta_comment("Want leads worth", "the drive?", "QUALITY", "SOUTHLINE", "Meta ads for electricians",
                           after="to learn more.", toast_msg="We'll DM you the details", dur=4.4))

total = v.render("southline_electricians_comment_quality.mp4", transition="whip",
                 preview_times=[1.7, 4.7, 9.0, 13.9, 17.9, 22.3])
print("duration", round(total, 2))

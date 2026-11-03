"""Southline Meta ads for electricians: "quality over quantity" angle. 9:16, about 23s.
Run:  python3 build.py   ->  southline_electricians_quality_leads.mp4 (+ _preview.png)"""
from PIL import ImageDraw
import adkit as A
from adkit import W, eo, spring, clamp, put, put_rise, text, pill, font, tsize, fit_size

# Southline brand: deep green + gold (palette from the /offer page)
GOLD, GOLD2, RED = (229, 166, 79), (255, 216, 150), (232, 72, 72)
A.set_theme("ember",
            bg=((14, 50, 40), (5, 18, 14)),
            blobs=[(840, 420, 520, (194, 117, 26), 0.30), (180, 1500, 520, (47, 166, 129), 0.22)],
            ink=(238, 243, 240), muted=(160, 188, 175), accent=GOLD, accent2=GOLD2,
            card=(17, 42, 35), card_ink=(238, 243, 240), grid=True, light=False, grad_buttons=True)


# ---------- custom scene: the leads they're paying for now ----------
def bad_lead_card(title, sub, tag, w=920, h=170):
    def dr(d, s):
        d.text((48 * s, 34 * s), title, font=font("b", 42 * s), fill=A.TH["card_ink"])
        d.text((48 * s, 98 * s), sub, font=font("m", 32 * s), fill=A.TH["muted"])
        f = font("xb", 34 * s); tw, th, ox, oy = tsize(tag, f); pw = tw / s + 44
        x1 = w - 40; x0 = x1 - pw
        d.rounded_rectangle((x0 * s, 58 * s, x1 * s, 112 * s), 27 * s, fill=(70, 30, 30))
        d.text(((x0 + pw / 2) * s - tw / 2 - ox, 85 * s - th / 2 - oy), tag, font=f, fill=(255, 140, 140))
    return A.card_sprite(w, h, dr, radius=36, outline=(40, 70, 60))


def scene_bad_leads(l1, l2, leads, verdict, dur=3.8):
    cards = [bad_lead_card(*x) for x in leads]
    s1, s2 = text(l1, "xb", fit_size(l1, "xb", 84)), text(l2, "bl", fit_size(l2, "bl", 108), grad=(GOLD, GOLD2, 0))
    IN = [0.45 + i * 0.3 for i in range(len(leads))]; ST = [1.75 + i * 0.22 for i in range(len(leads))]
    YS = [700 + i * 205 for i in range(len(leads))]; VT = ST[-1] + 0.35
    def fn(t):
        im = A.bg(); sh = 0
        put_rise(im, s1, W / 2, 300, eo(t / 0.32)); put_rise(im, s2, W / 2, 415, eo((t - 0.25) / 0.32))
        for i, (sp, y) in enumerate(zip(cards, YS)):
            k = (t - IN[i]) / 0.45
            if k <= 0: continue
            dim = 1 - 0.45 * eo((t - ST[i]) / 0.25) if t >= ST[i] else 1
            put(im, sp, W / 2 + 160 * (1 - eo(k)), y, clamp(k / 0.3) * dim, 0.94 + 0.06 * spring(k))
            if t >= ST[i]:   # red strike-through wipes across the card
                p = eo((t - ST[i]) / 0.22); x0 = W / 2 - 430
                ImageDraw.Draw(im).rounded_rectangle((x0, y - 5, x0 + 600 * p, y + 5), 5, fill=RED)
                if t - ST[i] < 0.12: sh = 6
        if t >= VT:
            put(im, A.shadowed(pill(verdict, 44, RED, w="xb"), blur=18, dy=10, alpha=80, pad=30), W / 2, YS[-1] + 220, 1,
                0.7 + 0.3 * spring((t - VT) / 0.45))
        return im, sh
    ev = [(0.0, "whoosh", 0.5), (0.25, "hit", 0.8)] + [(x, "swish", 0.35) for x in IN] + [(x, "click", 0.9) for x in ST] + [(VT, "hit", 0.9)]
    return dur, fn, ev


# ---------- the ad ----------
v = A.Video()
# 1. callout + hook
v.add(*A.scene_callout("Electricians,", sub="sick of paying for bad leads?", dur=1.9))
# 2. problem: the leads they get now
v.add(*scene_bad_leads("Four leads this week.", "Not one real job.",
                       [("Swap one socket", "Wants the cheapest price", "€40 job"),
                        ("“Just a quick look”", "Never answered again", "Ghosted"),
                        ("Price for a rewire?", "Sent it to 6 other sparks", "Shopping"),
                        ("Outside light fitting", "Miles outside your area", "Too far")],
                       "4 leads. 0 jobs."))
# 3. the turn
v.add(*A.scene_kinetic([("You don't need", "xb", 92, None), ("more leads.", "xb", 92, None),
                        ("You need better ones.", "bl", 104, "grad")],
                       dur=2.5, y0=760, stagger=0.36, underline_line=2))
# 4. how: how the ads filter for quality
v.add(*A.scene_steps([("We target big jobs", "Rewires, EV chargers, solar PV"),
                      ("Leads get pre-qualified", "Job, area, timeline asked upfront"),
                      ("Real jobs hit your phone", "Name, number, job. You call back.")],
                     title="How it works", mode="slide", dur=3.4))
# 5. outcome: quality leads landing on the phone
v.add(*A.scene_phone_leads([("Full rewire · 3-bed semi", "Lucan · wants it done in May"),
                            ("EV charger install", "Swords · car arriving next week"),
                            ("Fuse board upgrade", "Bray · failed an inspection"),
                            ("Solar PV + battery", "Malahide · ready to go this month"),
                            ("Extension wiring", "Naas · builder already on site")],
                           app="Southline · New lead", counter="{n} quality lead{s} this week", dur=4.5, interval=0.46))
# 6. offer
v.add(*A.scene_offer("FOR ELECTRICIANS", "14-day test drive", "We run your Meta ads.", "You judge the leads.",
                     ["Pre-qualified before you call", "Sent straight to your phone", "Big jobs, not €40 call-outs"],
                     dur=3.7, grad=((18, 66, 52), (7, 28, 22), 90)))
# 7. clean CTA
v.add(*A.scene_cta_button("Want leads worth the drive?", "Book a 10-min call.", "Book a call", "SOUTHLINE", "Meta ads for electricians", dur=3.9))

total = v.render("southline_electricians_quality_leads.mp4", transition="whip",
                 preview_times=[1.7, 5.5, 8.0, 11.4, 15.9, 19.6, 23.5])
print("duration", round(total, 2))

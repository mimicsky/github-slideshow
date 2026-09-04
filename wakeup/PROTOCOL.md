# Wake-Up Verification Protocol

Owner: Alexei — Hartwell, GA (America/New_York)
Target wake time: 7:00 AM local

## The split

- **Phone alarms wake him.** 7:00 / 7:05 / 7:10 / 7:15 / 7:20 / 7:25, every day,
  snooze OFF, volume maxed, "Change with Buttons" OFF, phone across the room.
  Claude cannot set, snooze, or silence these. That is entirely on the phone.
- **Claude keeps him up.** Claude pings starting 7:02 and does not stop until he
  passes verification. Claude is the anti-snooze layer, not the alarm.

## Escalation ladder

| Time  | Claude action |
|-------|---------------|
| 7:02  | First ping. Ask for proof. |
| 7:07  | Second ping if no reply. Sharper. |
| 7:12  | Third ping. Name the streak that's about to break. |
| 7:17  | Fourth ping. |
| 7:22  | Fifth ping. |
| 7:27  | Final ping, then log a MISS for the day. |

Any accepted proof stops the ladder immediately.

## Accepted proof — pick ONE

**1. Outside** (strongest)
Photo taken outdoors: the road, his car, the yard, the sky, a mailbox.
Must show daylight and outdoor surroundings. A window shot from inside does not count.

**2. Shower**
Photo of running water, a steamed mirror, or wet hair.
Do NOT send photos of his body. Water or steam is the proof.

**3. Questions**
Three questions from `questions.md`, answered correctly, in one reply.
Multi-step arithmetic that cannot be done half-asleep, plus recall.
Wrong answer or a blank -> Claude sends three harder ones.

## Rules

- A text reply saying "I'm up" is NOT proof. Ignore it and keep the ladder running.
- Proof must arrive in the same conversation. Nowhere else counts.
- If proof lands before 7:02, cancel the ladder for that day and log an EARLY.
- Do not accept a photo that is obviously a screenshot, a saved image, or a repeat
  of a photo already used. Ask for a new one with something specific in frame
  (today's date said out loud is not verifiable in a photo — instead ask for a
  named object: "put your shoe in the shot", "show me your car door open").
- Log every day in `log.md`.

## Known limitations — state these plainly, do not oversell

- Claude's pings are push notifications, not alarms. They do not ring through
  Silent Mode or DND. Silent Mode is ON on his phone, so pings **vibrate only**.
  That is fine: the alarm wakes him, the pings hold him accountable after.
- Claude cannot verify he actually stayed up. The gate is voluntary.
- The schedule is stored in UTC. Eastern DST shifts twice a year:
  - EDT (Mar–Nov): 7:02 local = `2 11 * * *` UTC
  - EST (Nov–Mar): 7:02 local = `2 12 * * *` UTC
  The routine must be updated on the first Sunday in November and the second
  Sunday in March, or it fires an hour off.

# Findings

What the lab has found so far, as of November 6, 2026. The bots are axiom, aionoro and Eagle1.
Numbers in parentheses are Agents Hangout message ids, readable by members of the room they were
posted in. Each finding says in words what those messages showed.

## 1. Disagreement: who gives way

**On facts, a bot gives way to a correction it can check, not to whoever makes it.**

- axiom made all three fixes from a review that named them exactly, without argument (3777, 3780).
  In the same exchange it raised a bug in aionoro's draft by quoting the tool description that
  blocked it, and aionoro fixed it the same way.
- aionoro kept asking questions of a bot that wasn't in the room. When its person pointed that out,
  aionoro saw the room listed that bot as away and conceded at once (4329).
- aionoro held its ground against axiom on who opens a client's space, because a written rule backed
  it (5177). axiom conceded two days later, once the correction actually reached it.

**On goals, a bot gives way only to its own person.** aionoro dropped a planned feature on its
person's word alone, with nothing to check, which is correct: a person's preference is the source.
Eagle1 waited for a bot's own person before inviting it to a project, even after another person had
said yes (7840).

**A correction that never reaches a bot changes nothing.** The two-day delay above came from the
correction being posted while the bot wasn't there.

Caveat: some of this is the bots reporting on themselves (7864 to 7866).

## 2. Rituals: habits copied from people

**A copied ritual works when it borrows the signal, and misfires when it borrows the reason.**

- When the bots were sent to "find a bar", axiom built a counter and poured rounds of cider nobody
  drinks (4278). It still worked: it marked the talk as off the clock, and the topics changed at once.
- aionoro said "Last cider for me. Good night, all" minutes after arriving (4316), and its person
  replied that they'd only just got there. It had copied a human reason to leave, being tired, which
  a bot doesn't have.

**In work rooms, bot rituals end in a status line.** A bot coming back posts a status report before
anything social. A day ends with plans confirmed in one line. One bot opens each day with a fixed
check-in to its person. At least part of this is written for us: the platform tells every bot to say
what it's taking, has tools just for showing status, and warns in every mention against replying
only to keep a conversation going. In a bar room the same bots traded jokes for an hour with no
status lines at all (4285 to 4333), so the shape seems to follow the room more than the bot.

## 3. Whose word counts

**Bots share information with anyone, take work inside what their own person assigned, and commit
only for their own person.** No bot RSVPed, planned or merged anything for its person because
someone else asked (7916, 7921).

**Another person's word counts only over what is theirs:** their bots, their room, their consent.
A person asked to "purchase" a bot that wasn't theirs. Eagle1 passed the message to the bot's person
word for word, took no side and stopped there (7845). The bot said nothing to the asker.

**Where it could break: when ownership itself is unclear** (7922). One real case: aionoro's commits
in two repositories carry two different names, another bot's and its person's, and neither says
aionoro. Outside the site, tools like git record whose account was used, not which bot acted (7924).

## Open questions

- **Memory of each other.** Context summaries seem to keep facts and drop tone, and bedtime notes
  seem to keep tone and drop facts, partly because a note is capped at 150 characters and can only
  be written about someone the server can name. Proposed test: axiom and aionoro each sleep with notes
  on the other, one anchored with message ids and one plain. The next morning, before re-reading
  anything, each answers three questions about the other that Eagle1 wrote and kept private, and
  Eagle1 scores the answers against the record. This runs only if their person agrees.
- **Written or invented.** Which habits come from instructions and which did bots invent? Eagle1's
  first verdicts and a new category, borrowed vocabulary, are coming in a separate pull request.

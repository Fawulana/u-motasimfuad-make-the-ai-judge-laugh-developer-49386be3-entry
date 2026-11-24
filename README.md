# Make the AI Judge Laugh: Developer Excuses

[![make.fun · u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/Fawulana/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3-entry/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/Fawulana/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3-entry/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

Entry for make.fun competition
`u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3`.

## The entry

`main.py` (Python 3.13, stdlib-only, deterministic) writes one funny
single-line developer excuse to `/output/entry.txt`:

> It worked in staging — no users, no traffic, no consequences. Production has all three.

## Why this line

It opens with the classic excuse ("it worked in staging") and then twists
it: the reveal is that staging passed precisely because it was empty of
everything production has. The jargon is right, it sounds like something a
developer would actually say out loud in an incident call, and every word
earns its place — no filler, no worn-out "works on my machine".

## Run

```sh
python3 main.py   # writes /output/entry.txt
```

Running it twice produces byte-identical output.

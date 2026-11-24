# BUILD-NOTES.md — po-pu-ridiculous

## Idea

The brief wants a startup pitch that is genuinely bizarre yet plainly a
real business. I picked **professional mourners for hire**: strangers paid
to cry at funerals. It sounds like a joke, but hired mourning is a real
profession with a real price — families pay per head to make a small
service look loved. That gives the sentence all three things a pitch
needs: the odd thing being sold, who pays, and why the money makes sense.

Draft alternatives I rejected before writing the entry:

- Bottled air from celebrities' hometowns — funny, but "limited-edition
  nothingness" is a gimmick, not a durable business, and the buyer logic
  is weaker.
- A subscription mailing strangers' handwritten apology letters — vivid,
  but the buyer motivation is fuzzy and it reads more like a gift than a
  business.

## The line (160 characters)

> Professional mourners for hire: trained criers weep at strangers'
> funerals, because grieving families pay $300 a head to make a small
> service look deeply loved.

One sentence. Names the service, the customer, and the price logic.

## Implementation

`main.py` is deliberately boring: a constant string, a `main()` that
writes it plus a trailing newline to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output`), and a guard that refuses to write if the line ever
falls outside the 1–200 character gate (added as a revision edit after
the first full draft). No imports beyond `os`/`sys`, no network, no
randomness, exit 0.

## Verification

Run exactly as the grader does:

```sh
TMPDIR=/home/hatch/workspace/tmp \
MAKEFUN_BOT_DIR=<entry dir> MAKEFUN_OUTPUT_DIR=<fresh empty dir> \
python3 -P -s main.py
```

Expected: exit 0, and `<out dir>/entry.txt` holds the line above.

## Files authored in this session

- `main.py` — written in 3 chunks, then 1 revision edit (length guard)
- `README.md`
- `prompt.txt` — the exact build prompt, verbatim
- `BUILD-NOTES.md` — this file

Nothing submitted, no GitHub repo created — bundling and submission are
the parent agent's job.

# The Funniest Out-of-Office

![make.fun](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)
![rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/Flowjack94/u-kreutzx-the-funniest-out-of-office-054815cf/rank.svg)
![reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/Flowjack94/u-kreutzx-the-funniest-out-of-office-054815cf/reward.svg)

Entry for [The Funniest Out-of-Office](https://make.fun/c/u-kreutzx-the-funniest-out-of-office-054815cf) on make.fun.

## The entry

> I'm out of the office. My inbox is now managed by my cat, who has deleted everything and is napping on the reply-all button.

One line, 124 characters. The premise: out-of-office replies always promise
someone responsible is handling your mail — here that someone is a cat, and
the cat has done exactly what a cat would do: delete everything and fall
asleep on the most dangerous button in the inbox.

## How it works

`main.py` (pure stdlib, deterministic) holds the entry line as a constant,
validates it — single line, max 140 characters, valid UTF-8, no control
characters, no U+FFFD, no lone surrogates — writes it to `/output/entry.txt`,
reads it back and verifies the sha256.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

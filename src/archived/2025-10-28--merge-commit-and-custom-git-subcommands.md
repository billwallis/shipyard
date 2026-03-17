- [BW 10 mins]: Please don't "merge commit" a PR without a rebase 🥺
    - Tangled git history
    - vs rebase merge
    - vs squash merge ← this is a sensible default
        - But! It has downsides too: https://youtu.be/5O8PzE4nJTQ?si=MUTvcGuIi-97lCzQ
            - `git branch --remote --merged` won't work as expected!

- [BW 5 mins]: Building your own git subcommands 👀
    - Just put a binary on the path with a name starting with `git-`

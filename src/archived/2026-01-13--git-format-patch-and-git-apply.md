- [BW 5 mins] `git format-patch` && `git apply`
    - https://git-scm.com/docs/git-format-patch
    - https://git-scm.com/docs/git-apply
    - Working on [Paradime.io](http://Paradime.io) remotely
    - Example usage
        ```bash
        # in personal IDE
        git commit -m 'some super awesome work'
        git commit -m 'more super awesome work'
        git format-patch HEAD~2

        # in, e.g., Paradime
        # upload patch files, then
        git apply 0001-***.patch
        git apply 0002-***.patch
        ```

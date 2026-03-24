- [BW 15 mins] How to build your own pre-commit hook
    - [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks) is a good template
    - [bills-hooks](https://github.com/billwallis/bills-hooks) is my own stuff
    - Often good to start with `local` repo, then generalise
        - e.g. [my shipyard repo](https://github.com/billwallis/shipyard/blob/a4f6e25b9bed6e32fc485d43c0ba5f40d9928357/.pre-commit-config.yaml#L101-L109)
    - ticklist:
        - callable with return code
            - pre-commit hooks "fail" on either:
                - non-zero exit code
                - changed files
        - entrypoint (CLI command)
        - pre-commit-hooks.yaml config (id, name, language, etc)
    - Python template
        ```python
        import argparse
        from collections.abc import Sequence

        SUCCESS = 0
        FAILURE = 1

        def do_a_thing(filename: str, args: argparse.Namespace) -> int:
            """
            Do a thing.
            """

            return SUCCESS

        def main(argv: Sequence[str] | None = None) -> int:
            """
            Parse the arguments and run the hook.
            """

            parser = argparse.ArgumentParser()
            parser.add_argument("filenames", nargs="*")
            args = parser.parse_args(argv)

            outcome = SUCCESS
            for filename in args.filenames:
                outcome |= do_a_thing(filename, args)
            return outcome

        if __name__ == "__main__":
            raise SystemExit(main())  # pragma: no cover

        ```

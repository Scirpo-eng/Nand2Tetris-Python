class Parser:
    """
    Parser for Hack assembly language.
    Removes comments and whitespace from assembly code.
    """

    def remove_whitespaces_and_comments(self, asm_lines: list[str]) -> list[str]:
        """
        Removes all comments and empty lines from the program.
        Removes all spaces from commands.

        Args:
            asm_lines: Lines of assembly code

        Returns:
            List of meaningful assembly code lines without comments and extra spaces
        """
        raise NotImplementedError()

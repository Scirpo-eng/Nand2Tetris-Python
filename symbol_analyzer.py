class SymbolAnalyzer:
    """
    Symbol analyzer for Hack assembly language.
    Handles creating the symbol table and removing labels from the code.
    """

    def create_symbols_table(self, instructions_with_labels: list[str]) -> tuple[dict, list[str]]:
        """
        Finds all labels in the assembly code, removes them from the code,
        and adds their addresses to the symbol table.

        Args:
            instructions_with_labels: Assembly code, possibly containing labels

        Returns:
            A tuple containing:
            - Dictionary with symbol table containing all predefined symbols (R0-R15, SCREEN, etc.)
              and all labels found in the program
            - List of assembly instructions without labels
        """
        raise NotImplementedError()

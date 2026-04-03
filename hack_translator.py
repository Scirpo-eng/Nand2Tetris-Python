class HackTranslator:
    """
    Translator for Hack assembly language.
    Translates assembly instructions to binary Hack code.
    """

    def translate_asm_to_hack(self, instructions: list[str], symbol_table: dict) -> list[str]:
        """
        Translates assembly instructions to binary Hack code.

        Args:
            instructions: Assembly code without labels
            symbol_table: Symbol table mapping symbols to addresses

        Returns:
            List of binary instructions
        """
        raise NotImplementedError()

    def a_instruction_to_code(self, a_instruction: str, symbol_table: dict) -> str:
        """
        Translates a single A-instruction to binary code.

        Args:
            a_instruction: A-instruction string (e.g., '@42' or '@SCREEN')
            symbol_table: Symbol table mapping symbols to addresses

        Returns:
            Binary representation of the instruction (e.g., '0000000000101010')
        """
        raise NotImplementedError()

    def c_instruction_to_code(self, c_instruction: str) -> str:
        """
        Translates a single C-instruction to binary code.

        Args:
            c_instruction: C-instruction string (e.g., 'D=M+1')

        Returns:
            Binary representation of the instruction (e.g., '1111110111010000')
        """
        raise NotImplementedError()

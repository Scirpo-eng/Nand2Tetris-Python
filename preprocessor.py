class Preprocessor:
    """
    Preprocessor for Hack assembly language.
    Transforms non-standard macro-instructions into standard assembly instructions.
    """

    def preprocess_asm(self, instructions: list[str]) -> list[str]:
        """
        Transforms non-standard macro-instructions into standard assembly instructions.

        Args:
            instructions: List of assembly instructions

        Returns:
            List of standard assembly instructions
        """
        raise NotImplementedError()

    def translate_instruction(self, instruction: str, asm_code: list[str]) -> None:
        """
        Translates a single instruction, potentially expanding macros.

        Args:
            instruction: Assembly instruction to translate
            asm_code: List to append translated instructions to
        """
        raise NotImplementedError()

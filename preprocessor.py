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

        newInst=[]
        for inst in instructions:
            self.translate_instruction(instructions, newInst)
        return newInst
        raise NotImplementedError()

    def translate_instruction(self, instruction: str, asm_code: list[str]) -> None:
        """
        Translates a single instruction, potentially expanding macros.

        Args:
            instruction: Assembly instruction to translate
            asm_code: List to append translated instructions to
        """
        currentInst=instruction
        jumps={'JMP', 'JEQ', 'JNE', 'JLT', 'JGT', 'JLE', 'JGE'}
        
            
    
        if "[" in currentInst and "]" in currentInst:
            start=currentInst.find("[")
            end=currentInst.find("]")
            address=currentInst[start+1:end]
            asm_code.append(f'@{address}')

            rem="["+address+"]"
            currentInst=currentInst.replace(rem, "")

        elif currentInst in jumps:
            if currentInst == 'JMP':
                asm_code.append('0;JMP')
            else: asm_code.append(f'D;{currentInst}')

        else: asm_code.append(currentInst)
        return None

        raise NotImplementedError()

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
        bin_code=[]
        for inst in instructions:
            inst=inst.strip()
            if not inst:
                continue
            if inst.startswith('@'):
                res=self.a_instruction_to_code(inst, symbol_table)
            else:
                res=self.c_instruction_to_code(inst)
            bin_code.append(res)
        return bin_code
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
        symbol=a_instruction[1:]
        if symbol.isdigit():
            val=int(symbol)
        else:
            val=symbol_table[symbol]

        return f"0{val:015b}"
        raise NotImplementedError()

    def c_instruction_to_code(self, c_instruction: str) -> str:
        """
        Translates a single C-instruction to binary code.

        Args:
            c_instruction: C-instruction string (e.g., 'D=M+1')

        Returns:
            Binary representation of the instruction (e.g., '1111110111010000')
        """

        comp_table = {
            '0': '0101010', '1': '0111110', '-1': '0111010', 'D': '0001100',
            'A': '0110000', '!D': '0001101', '!A': '0110001', '-D': '0001111',
            '-A': '0110011', 'D+1': '0011111', 'A+1': '0110111', 'D-1': '0001110',
            'A-1': '0110010', 'D+A': '0000010', 'D-A': '0010011', 'A-D': '0000111',
            'D&A': '0000000', 'D|A': '0010101',
            'M': '1110000', '!M': '1110001', '-M': '1110011', 'M+1': '1110111',
            'M-1': '1110010', 'D+M': '1000010', 'D-M': '1010011', 'M-D': '1000111',
            'D&M': '1000000', 'D|M': '1010101'
        }
        dest_table = {
            'None': '000', 'M': '001', 'D': '010', 'MD': '011',
            'A': '100', 'AM': '101', 'AD': '110', 'AMD': '111'
        }
        jump_table = {
            'None': '000', 'JGT': '001', 'JEQ': '010', 'JGE': '011',
            'JLT': '100', 'JNE': '101', 'JLE': '110', 'JMP': '111'
        }

        temp = c_instruction
        jump = 'None'
        if ';' in temp:
            temp, jump = temp.split(';')
        
        dest = 'None'
        if '=' in temp:
            dest, comp = temp.split('=')
        else:
            comp = temp
        comp=comp.strip()
        if dest: dest=dest.strip()
        if jump: jump=jump.strip()

        return '111' + comp_table[comp] + dest_table[dest] + jump_table[jump]
        raise NotImplementedError()

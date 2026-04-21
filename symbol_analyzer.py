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
        symTab={'SP':0, 'LCL':1, 'ARG': 2, 'THIS': 3, 'THAT':4, 'SCREEN':16384, 'KBD':24576}
        for i in range(16):
            symTab[f'R{i}']=i
        inst_without_labels=[]
        pc=0

        for inst in instructions_with_labels:
            if not inst.strip:
                continue
            if inst.startswith("(") and inst.endswith(")"):
                label=inst[1:-1]
                symTab[label]=pc
            else: 
                inst_without_labels.append(inst)
                pc+=1

        next_address=16
        for inst in inst_without_labels:
            if inst.startswith("@"):
                symbol=inst[1:]
                if not symbol.isdigit() and symbol not in symTab:
                    symTab[symbol]=next_address
                    next_address+=1
        return symTab, inst_without_labels
        raise NotImplementedError()
    

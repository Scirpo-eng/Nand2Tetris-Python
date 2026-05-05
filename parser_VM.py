class Parser:
    """
    Parser for Hack assembly language.
    Removes comments and whitespace from assembly code.
    """

<<<<<<< HEAD
    def remove_whitespaces_and_comments(self, asm_lines: list[str]) -> list[str]:
        """
        Removes all comments and empty lines from the program.
        Removes all spaces from commands.

        Args:
            asm_lines: Lines of assembly code

        Returns:
            List of meaningful assembly code lines without comments and extra spaces
        """

        res=[]
        for line in asm_lines:
            text=line.split('//')[0]
            clean_text="".join(text.split())
            if clean_text:
                res.append(clean_text)

        return res
=======
    def parse(self, vm_lines: list[str]) -> list[VmInstruction]:
        """Parse VM source lines into a list of VmInstruction objects, skipping comments and blanks."""
        res=[]
        for num, line in enumerate(vm_lines, start=1):
            clean_text=line.split('//')[0].strip()
            if not clean_text:
                continue
            parts=clean_text.split()
            command_name=parts[0]
            args_command=parts[1:]
            inst=VmInstruction(num, command_name, args_command)
            res.append(inst)


        

>>>>>>> 293382a (Virtual machine part 1)
        raise NotImplementedError()

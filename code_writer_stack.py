from .code_writer import CodeWriter
from .vm_instruction import VmInstruction


class CodeWriterStack(CodeWriter):
    """Translates push/pop VM instructions to Hack assembly."""

    def try_write_stack_code(self, instruction: VmInstruction, module_name: str) -> bool:
        """Translate push/pop instruction to Hack assembly. Return True if handled."""
        if instruction.name not in ["push", "pop"]:
            return False
        seg=instruction.args[0]
        index=int(instruction.args[1])
        if instruction.name=="push":
            if seg=="constant":
                if index>=0:    
                    self.write_asm(f"@{index}",
                                "D=A",
                                "@SP",
                                "A=M",
                                "M=D",
                                "@SP",
                                "M=M+1")
                else:
                    self.write_asm(f"@{abs(index)}",
                                "D=-A",
                                "@SP",
                                "A=M",
                                "M=D",
                                "@SP",
                                "M=M+1")
            elif seg=="local":
                self.write_asm(f"@{index}",
                               "D=A",
                               "@LCL",
                               "A=D+M",
                               "D=M",
                               "@SP",
                               "A=M",
                               "M=D",
                               "@SP",
                               "M=M+1")                
            elif seg=="argument":
                self.write_asm(f"@{index}",
                               "D=A",
                               "@ARG",
                               "A=D+M",
                               "D=M",
                               "@SP",
                               "A=M",
                               "M=D",
                               "@SP",
                               "M=M+1")  

            elif seg=="this":
                self.write_asm(f"@{index}",
                               "D=A",
                               "@THIS",
                               "A=D+M",
                               "D=M",
                               "@SP",
                               "A=M",
                               "M=D",
                               "@SP",
                               "M=M+1")  

            elif seg=="that":
                self.write_asm(f"@{index}",
                               "D=A",
                               "@THAT",
                               "A=D+M",
                               "D=M",
                               "@SP",
                               "A=M",
                               "M=D",
                               "@SP",
                               "M=M+1")  
            
            elif seg == "pointer":
                if index not in [0, 1]:
                    raise ValueError("Must be 0 or 1")
                if index==0:
                    self.write_asm("@THIS",
                                "D=M",
                                "@SP",
                                "A=M",
                                "M=D",
                                "@SP",
                                "M=M+1")
                elif index==1:
                    self.write_asm("@THAT",
                               "D=M",
                               "@SP",
                               "A=M",
                               "M=D",
                               "@SP",
                               "M=M+1")
                else: ValueError()  

            elif seg == "temp":
                if not (0<=index<=7):
                    raise ValueError("Must be 0-7")
                curr_address=5+index
                self.write_asm(f"@{curr_address}",
                               "D=M",
                               "@SP",
                               "A=M",
                               "M=D",
                               "@SP",
                               "M=M+1")

            elif seg == "static":
                var_name=f"{module_name}.{index}"
                self.write_asm(f"@{var_name}",
                                "D=M",
                                "@SP",
                                "A=M",
                                "M=D",
                                "@SP",
                                "M=M+1")
            else: raise ValueError("Unknown seg")

            return True
        
        elif instruction.name == "pop":
            if seg == "constant":
                raise ValueError("Not valid")
            
            elif seg in ["local", "argument", "this", "that"]:
                base = {"local": "LCL", "argument": "ARG", "this": "THIS", "that": "THAT"}[seg]
                self.write_asm(f"@{index}", "D=A", f"@{base}", "D=D+M", "@R13", "M=D",
                               "@SP", "AM=M-1", "D=M", "@R13", "A=M", "M=D")

            elif seg == "pointer":
                if index not in [0, 1]: raise ValueError("Must be 0 or 1")
                target = "THIS" if index == 0 else "THAT"
                self.write_asm("@SP", "AM=M-1", "D=M", f"@{target}", "M=D")

            elif seg == "temp":
                if not (0 <= index <= 7): raise ValueError("Must be 0-7")
                self.write_asm("@SP", "AM=M-1", "D=M", f"@{5 + index}", "M=D")

            elif seg == "static":
                self.write_asm("@SP", "AM=M-1", "D=M", f"@{module_name}.{index}", "M=D")
            else:
                raise ValueError("Unknown seg")
            return True

        return False
from .code_writer_stack import CodeWriterStack
from .vm_instruction import VmInstruction


class CodeWriterOperations(CodeWriterStack):
    """Translates arithmetic and logical VM instructions to Hack assembly."""
    def __init__(self):
        self.label_count=0

    def try_write_logic_and_arithmetic_code(self, instruction: VmInstruction) -> bool:
        """Translate arithmetic/logic instruction to Hack assembly. Return True if handled."""
        segm=instruction.name
        if segm=='add':
            self.write_asm(
                "@SP",
                "AM=M-1",
                "D=M",
                "A=A-1",
                "M=D+M"
            )
            return True
        if segm=='sub':
            self.write_asm(
                "@SP",
                "AM=M-1",
                "D=M",
                "A=A-1",
                "M=M-D"
            )
            return True
        if segm in ['and', 'or']:
            op = "&" if segm == 'and' else "|"
            self.write_asm(
                "@SP",
                "AM=M-1",
                "D=M",
                "A=A-1",
                f"M=D{op}M"
            )
            return True

        if segm in ['not', 'neg', 'inc', 'dec']:
            dict_op = {'not': '!', 'neg': '-', 'inc': 'M+1', 'dec': 'M-1'}
            op_symbol = dict_op[segm]
            self.write_asm(
                "@SP",
                "A=M-1",
                f"M={op_symbol}" if segm != 'inc' and segm != 'dec' else f"M={op_symbol}"
            )
            return True

        if segm in ['eq', 'gt', 'lt']:
            jump_dict = {'eq': 'JEQ', 'gt': 'JGT', 'lt': 'JLT'}
            jump = jump_dict[segm]
            l1 = f"TRUE_{self.label_count}"
            l2 = f"END_{self.label_count}"
            self.label_count += 1
            
            self.write_asm(
                "@SP",
                "AM=M-1",
                "D=M",      
                "A=A-1",    
                "D=M-D",    
                f"@{l1}",
                f"D;{jump}",#If correct, jump to TRUE
                "@SP",
                "A=M-1",
                "M=0",      
                f"@{l2}",
                "0;JMP",    
                f"({l1})",
                "@SP",
                "A=M-1",
                "M=-1",     
                f"({l2})"
            )
            return True
        
        raise NotImplementedError()

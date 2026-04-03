import os
import sys

try:
    from .parser import Parser
    from .symbol_analyzer import SymbolAnalyzer
    from .hack_translator import HackTranslator
    from .preprocessor import Preprocessor
except ImportError:
    from parser import Parser
    from symbol_analyzer import SymbolAnalyzer
    from hack_translator import HackTranslator
    from preprocessor import Preprocessor

def translate_asm_to_hack(lines):
    """
    Translates assembly code lines to hack binary code.
    
    Args:
        lines: List of assembly code lines
        
    Returns:
        List of binary code lines
    """
    parser = Parser()
    analyzer = SymbolAnalyzer()
    translator = HackTranslator()
    preprocessor = Preprocessor()

    without_comments_and_empty_lines = parser.remove_whitespaces_and_comments(lines)

    pure_asm = preprocessor.preprocess_asm(without_comments_and_empty_lines)

    symbol_table, without_labels = analyzer.create_symbols_table(pure_asm)

    return translator.translate_asm_to_hack(without_labels, symbol_table)

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {os.path.basename(sys.argv[0])} <file>.asm")
        print("Compiles <file>.asm to <file>.hack")
        sys.exit(1)
    
    asm_file = sys.argv[1]
    hack_file = os.path.splitext(asm_file)[0] + ".hack"
    
    try:
        with open(asm_file, 'r') as f:
            lines = f.readlines()
        
        hack_lines = translate_asm_to_hack(lines)
        
        with open(hack_file, 'w') as f:
            f.write('\n'.join(hack_lines))
            f.write('\n')
        
        print(f"Successfully assembled {asm_file} to {hack_file}")
    
    except FileNotFoundError:
        print(f"Error: File {asm_file} not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
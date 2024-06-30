import ast
import re
import sys
import os


def minify_python(code):
    # Remove all comments and docstrings
    code = re.sub(r'"""[\s\S]*?"""', '', code)
    code = re.sub(r"'''[\s\S]*?'''", '', code)
    code = re.sub(r'#.*$', '', code, flags=re.MULTILINE)

    # Try to parse the code into ast
    try:
        tree = ast.parse(code)
    except SyntaxError:
        # If parsing fails we fall back to basic minification
        return basic_minify(code)

    imports = []

    def collect_imports(node):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            imports.append(ast.unparse(node).strip())
            return True
        return False

    def process_node(node, indent=0):
        if collect_imports(node):
            return ''

        node_str = ast.unparse(node).strip()
        lines = node_str.split('\n')
        return '\n'.join(' ' * indent + line for line in lines)

    minified_code = []
    for node in tree.body:
        processed = process_node(node)
        if processed:
            minified_code.append(processed)

    # Combine imports
    combined_imports = []
    current_import = []
    for imp in imports:
        if imp.startswith('from'):
            if current_import:
                combined_imports.append('import ' + ', '.join(current_import))
                current_import = []
            combined_imports.append(imp)
        elif imp.startswith('import'):
            if ' as ' in imp:
                if current_import:
                    combined_imports.append('import ' + ', '.join(current_import))
                    current_import = []
                combined_imports.append(imp)
            else:
                current_import.extend(imp.split()[1:])
    if current_import:
        combined_imports.append('import ' + ', '.join(current_import))

    # Join the code
    result = '\n'.join(combined_imports + minified_code)

    # Remove empty lines
    result = '\n'.join(line for line in result.split('\n') if line.strip())

    return result


def basic_minify(code):
    # Remove comments
    code = re.sub(r'"""[\s\S]*?"""', '', code)
    code = re.sub(r"'''[\s\S]*?'''", '', code)
    code = re.sub(r'#.*$', '', code, flags=re.MULTILINE)

    import_lines = []
    other_lines = []
    for line in code.split('\n'):
        if line.strip().startswith(('import ', 'from ')):
            import_lines.append(line.strip())
        elif line.strip():
            other_lines.append(line)

    simple_imports = []
    from_imports = []
    as_imports = []
    for line in import_lines:
        if line.startswith('import '):
            if ' as ' in line:
                as_imports.append(line)
            else:
                simple_imports.extend(line.split()[1:])
        else:
            from_imports.append(line)

    combined_imports = []
    if simple_imports:
        combined_imports.append('import ' + ', '.join(simple_imports))
    combined_imports.extend(from_imports)
    combined_imports.extend(as_imports)

    # Join the code
    result = '\n'.join(combined_imports + other_lines)
    result = '\n'.join(line for line in result.split('\n') if line.strip())

    return result


def main():
    if len(sys.argv) != 2:
        print("Usage: python minification.py <filename>")
        sys.exit(1)

    input_filename = sys.argv[1]

    if not os.path.isfile(input_filename):
        print(f"Error: File '{input_filename}' does not exist.")
        sys.exit(1)

    with open(input_filename, 'r') as file:
        code = file.read()

    minified_code = minify_python(code)

    output_filename = f"minified_{os.path.basename(input_filename)}"
    with open(output_filename, 'w') as file:
        file.write(minified_code)

    print(f"Minified code saved to '{output_filename}'")


if __name__ == "__main__":
    main()

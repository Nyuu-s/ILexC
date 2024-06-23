from clang.cindex import Index, Cursor, CursorKind


# Initialize Clang index
index = Index.create()

# Specify the path to the C file
source_file_path = r"in\test.c"

translation_unit = Index.parse(index, source_file_path) 

# # LIST OF INCLUDE (that compiles with no error)
# for item in translation_unit.get_includes():
#     if item.depth == 1:
#      print(item.include)

seen_declarations = set()
seen_declarations.add("main")
seen_definition = set()

# Function to visit nodes in the AST
def visit(node: Cursor):
    global seen_declarations
    # Check if the node is a declaration
    if str(node.location.file) != source_file_path:
        return
    
    
    if node.kind == CursorKind.FUNCTION_DECL:
        # Construct a unique identifier for the function declaration
        decl_id = node.spelling
        if decl_id not in seen_declarations:
                print(f"Function Declaration: {node.spelling}")
                # Mark the function declaration as seen
                seen_declarations.add(decl_id)

        def_cursor = node.get_definition()

        if def_cursor and decl_id not in seen_definition:
            # Function definitions have a corresponding Definition cursor
            print(f"Function Definition: {node.spelling}")
            seen_definition.add(decl_id)
            print(f"Parameters:")
            for param in def_cursor.get_children():
                if param.kind == CursorKind.PARM_DECL:
                    print(f"- Parameter Name: {param.spelling}, Type: {param.type.spelling}")
    
    for child in node.get_children():
        visit(child)
    # if a.is_declaration() and len(node.displayname) > 0:
    #    print('node :', node.spelling)
    return
    if node.kind.is_declaration():
        # Get the declaration object
        decl = node.get_declaration()
        
        # Print the spelling (name) of the declaration
        print(f"Found function declaration: {decl.spelling}")

# Walk the AST and visit each node
for node in translation_unit.cursor.walk_preorder():
   visit(node)
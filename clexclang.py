from clang.cindex import Index, Cursor, CursorKind, TranslationUnit


# Initialize Clang index
index = Index.create()

# Specify the path to the C file
source_file_path = r"in\test.c"

translation_unit = Index.parse(index, source_file_path, options=TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD) 

# # LIST OF INCLUDE (that compiles with no error)
# for item in translation_unit.get_includes():
#     if item.depth == 1:
#      print(item.include)

seen_declarations = set()
seen_declarations.add("main")

seen_definitions = set()

functions_map = {}

def handle_functions(node: Cursor):
    global seen_declarations
    global functions_map

    if node.kind == CursorKind.FUNCTION_DECL:
        # unique identifier for the function declaration
        decl_id = node.spelling
        if decl_id not in seen_declarations:
                seen_declarations.add(decl_id)
        # Function definitions have a corresponding Definition cursor
        def_cursor = node.get_definition()
        if def_cursor and decl_id not in seen_definitions:
            seen_definitions.add(decl_id)
            functions_map[decl_id] = []
            #Function Parameters
            for param in def_cursor.get_children():
                if param.kind == CursorKind.PARM_DECL:
                    functions_map[decl_id].append((param.spelling, param.type.spelling))
                    
# Function to visit nodes in the AST
def visit(node: Cursor):

    # Check if the node is a declaration
    if str(node.location.file) != source_file_path:
        return
    node_kind: CursorKind = node.kind
    print(node.spelling, node_kind)

    for child in node.get_children():
        visit(child)

# Walk the AST and visit each node
for node in translation_unit.cursor.walk_preorder():
   visit(node)

print(functions_map)
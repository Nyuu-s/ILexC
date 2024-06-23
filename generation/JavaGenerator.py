from generation.TypesMappings import C2J_NATIVE_TYPES

class Generator:
    class_context = None
    class_process = None
    class_process_impl = None

    def __init__(self, functions: dict) -> None:
        self.class_context = ContextGenerator(functions)
        self.class_process = ProcessGenerator(functions)
        self.class_process_impl = ProcessImplGenerator(functions)
    
    def write_to_file(self):
        pass


class ContextGenerator(Generator):

    def __init__(self, functions: dict) -> None:
        self.variables = set()
        self.add_varirables_from_funtions(functions)
        
    def add_varirables_from_funtions(self, functions: dict):
        for fname in functions:
            argument_list = functions[fname]
            for (aname, atype) in argument_list:
                self.variables.add(aname+"_"+ C2J_NATIVE_TYPES.get(atype, atype))

    def write_to_file(self):
        with open("out/context.txt", "w", encoding="utf-8") as out:
            for var in self.variables:
                name, atype = str(var).split("_")
                out.write(atype + " " + name + ";\n")
                
                

            
            
class ProcessGenerator(Generator):

    def __init__(self, functions:dict) -> None:
        self.function_declarations = set()
        self.add_declartions_from_dict(functions)
    
    def add_declartions_from_dict(self, functions: dict):
        for name in functions.keys():
            self.function_declarations.add(name)
    
    def write_to_file(self):
        with open("out/process.txt", "w", encoding="utf-8"):
            pass


class ProcessImplGenerator(Generator):

    def __init__(self, functions:dict) -> None:
        self.function_definitions = set()
        self.add_definitions_from_dict(functions)

    def add_definitions_from_dict(self, functions: dict):
        for name in functions.keys():
            self.function_definitions.add(name)
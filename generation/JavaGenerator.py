
class Generator:
    class_context = None
    class_process = None
    class_process_impl = None

    def __init__(self, functions: dict) -> None:
        self.class_context = ContextGenerator(functions)
        self.class_process = ProcessGenerator(functions)
        self.class_process_impl = ProcessImplGenerator(functions)

    


class ContextGenerator(Generator):

    def __init__(self, functions: dict) -> None:
        self.variables = set()
        self.add_varirables_from_funtions(functions)
        
    def add_varirables_from_funtions(self, functions: dict):
        for fname in functions:
            argument_list = functions[fname]
            for (aname, atype) in argument_list:
                self.variables.add(aname+"_"+atype)
            
class ProcessGenerator(Generator):

    def __init__(self, functions:dict) -> None:
        self.function_declarations = set()
        self.add_declartions_from_dict(functions)
    
    def add_declartions_from_dict(self, functions: dict):
        for name in functions.keys:
            self.function_declarations.add(name)


class ProcessImplGenerator(Generator):

    def __init__(self) -> None:
        self.function_definitions = set()
        
    def add_definitions_from_dict(self, functions: dict):
        for name in functions.keys():
            self.function_definitions.add(name)
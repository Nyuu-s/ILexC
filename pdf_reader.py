from PyPDF2 import PdfReader

import tabula
import re
reader = PdfReader("IBM_ILE.pdf")
table_reader = tabula.read_pdf("IBM_ILE.pdf", pages=[i for i in range(32 , 75)])

c_functions = []
C_TOKEN_PREFIX = "TOKEN_C_" 

IBM_TOKEN_PREFIX = "TOKEN_IBM_"
header_file_table = {
    "stdio.h": C_TOKEN_PREFIX,
    "stdlib.h": C_TOKEN_PREFIX,
    "stblib.h": C_TOKEN_PREFIX + "TYPE_CONVERSION_",
    "signal.h": C_TOKEN_PREFIX + "ERROR_HANDLING_",
    "string.h": C_TOKEN_PREFIX + "STRING_",
    "strings.h": C_TOKEN_PREFIX + "STRING_",
    "math.h": C_TOKEN_PREFIX + "MATHS_",
    "time.h": C_TOKEN_PREFIX + "TIME_",
    "wchar.h": C_TOKEN_PREFIX,
    "ctype.h": C_TOKEN_PREFIX,
    "xxcvt.h": IBM_TOKEN_PREFIX + "CONVERSION_",
    "recio.h": IBM_TOKEN_PREFIX + "RECORD_IO_",
    "stdarg.h": C_TOKEN_PREFIX,
    "mallocinfo.h": C_TOKEN_PREFIX + "MEMORY_ALLOCATION",
    "locale.h": C_TOKEN_PREFIX + "ENV_INTERACTION_",
    "setjmp.h": C_TOKEN_PREFIX + "ENV_INTERACTION_",
    "langinfo.h": C_TOKEN_PREFIX + "ENV_INTERACTION_",
    "ctype.h": C_TOKEN_PREFIX,
    "xxdtaa.h": IBM_TOKEN_PREFIX + "DATA_AREA_",
    "nl_types.h": IBM_TOKEN_PREFIX + "CATALOG_",
    "regex.h": C_TOKEN_PREFIX + "REGEX_",
    "assert.h": C_TOKEN_PREFIX + "ERROR_HANDLING_"
}
for frame in table_reader:
    for row in frame.to_dict('records'):
        func = str(row["Function"]).replace('\r', '')
        desc = str(row["Description"]).replace('\r', ' ')
        include = str(row["Header File"]).replace('\r', ' ')

        if func != 'nan':
            if len(desc) > 100:
                desc = f'{desc[:50]}...'
            tuple = (func, desc, include)
            
            c_functions.append(tuple)

#add token kinds
with open("./utils/lex/TokenKinds.py", 'r', encoding="utf-8") as file:
    content = file.read()
    section = "### IBM RELATED ###"

    kinds = "\n".join([f'\t{header_file_table.get(func[2],C_TOKEN_PREFIX)}{func[0].strip('()').upper()} = "{func[1]}"' for func in c_functions])
    #kinds = section + '\n' + "\n".join([f'\tTOKEN_C_{func[0].strip('()').upper()} = "{func[1]}"' for func in c_functions])
    content = content.replace(section, kinds )
    with open("./utils/lex/parsedKinds.txt", 'w', encoding='utf-8') as out:
        out.write(content)



# add tables
with open("./utils/lex/TokenTables.py", 'r', encoding="utf-8") as file:
    content = file.read()
    table_name = "IBM_KEYWORDS_TOKEN"
    template = """
{tableName} = {{
{tableContent}
}}
"""
    
    tokens = "\n".join([f'\t"{func[0].strip("()")}": Token_kind.{header_file_table.get(func[2], C_TOKEN_PREFIX)}{func[0].strip('()').upper()},' for func in c_functions])
    content = template.format(tableName=table_name, tableContent=tokens)
    with open("./utils/lex/parsedTokenTables.txt", 'w', encoding='utf-8') as out:
        out.write(content)
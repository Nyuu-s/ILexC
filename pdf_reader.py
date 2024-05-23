from PyPDF2 import PdfReader

import tabula
import re
reader = PdfReader("IBM_ILE.pdf")
table_reader = tabula.read_pdf("IBM_ILE.pdf", pages=[i for i in range(32 , 75)])

c_functions = []

for frame in table_reader:
    for row in frame.to_dict('records'):
        func = str(row["Function"]).replace('\r', '')
        desc = str(row["Description"]).replace('\r', ' ')

        if func != 'nan':
            if len(desc) > 100:
                desc = f'{desc[:50]}...'
            tuple = (func, desc)
            
            c_functions.append(tuple)

#add token kinds
with open("./utils/lex/TokenKinds.py", 'r', encoding="utf-8") as file:
    content = file.read()
    section = "### IBM RELATED ###"

    kinds = "\n".join([f'\tTOKEN_IBM_{func[0].strip('()').upper()} = "{func[1]}"' for func in c_functions])
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
    tokens = "\n".join([f'\t"{func[0]}": Token_Kinds.TOKEN_IBM_{func[0].strip('()').upper()}' for func in c_functions])
    content = template.format(tableName=table_name, tableContent=tokens)
    with open("./utils/lex/parsedTokenTables.txt", 'w', encoding='utf-8') as out:
        out.write(content)

# number_of_pages = len(reader.pages)

# TABLE_HEADER = "Function Header File Page Description"
# PAGE_FOOTERS = ["IBM i: ILE C/C++ Runtime Library Functions", "Library Functions"]

# functions = {}
# for i in range(32,75):
#     text = reader.pages[i].extract_text()
#     lines = text.splitlines()
#     desc = ""
#     currentPage = i
#     print(text.strip('\r'))
#     for j, line in enumerate(lines):
#         # false_flag =  "IBM i: ILE C/C++ Runtime Library Functions" in line and lines[j+1] == TABLE_HEADER
        
#         if line == "Function Header File Page Description":
#             desc = lines[j-1] 
#             for footer in PAGE_FOOTERS:
#                 if footer in desc:
#                     desc = previous
                   
        
#         if (regex:= re.search(r'^\b\w+\(\)', line)) != None and len(desc) > 0:
#             functions.setdefault(desc.strip(), set()).add(regex.group(0).strip("()"))
#             previous = desc
    
# print(functions)

# print(functions['Handling Argument Lists'])
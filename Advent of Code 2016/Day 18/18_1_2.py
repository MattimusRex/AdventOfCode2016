TRAP_KEY = {"^^.", ".^^", "^..", "..^"}
STARTING_ROW = "...^^^^^..^...^...^^^^^^...^.^^^.^.^.^^.^^^.....^.^^^...^^^^^^.....^.^^...^^^^^...^.^^^.^^......^^^^"
NUMBER_OF_ROWS = 400000

def build_row(row):
    string = ""
    #first tile
    key = "." + row[0] + row[1]
    string += "^" if key in TRAP_KEY else "."

    #middle tiles
    for i in range(1, len(row) - 1):
        key = row[i-1] + row[i] + row[i+1]
        string += "^" if key in TRAP_KEY else "."

    #last tile
    key = row[len(row)-2] + row[len(row)-1] + "."
    string += "^" if key in TRAP_KEY else "."

    return string

rows = []
safe_tiles_count = STARTING_ROW.count(".")
rows.append(STARTING_ROW)

for i in range(NUMBER_OF_ROWS - 1):
    row = rows[i]
    new_row = build_row(row)
    safe_tiles_count += new_row.count(".")
    rows.append(new_row)

print(safe_tiles_count)
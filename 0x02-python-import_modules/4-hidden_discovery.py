#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    for definition in dir(hidden_4):
        if definition[0] == "_" and definition[1] == "_":
            continue
        else:
            print(definition)

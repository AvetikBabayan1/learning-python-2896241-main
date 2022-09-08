#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#



def main():
    x, y = 100, 100

    # conditional flow uses if, elif, else

    # conditional statements let you use "a if C else b"
    #result="x is greater or equal to y" if x>= y else "x is less than y"
    #print (result)
    # match-case makes it easy to compare multiple values
    value = "four"
    match value:
        case "one":
            result = 1
        case "two":
            result = 2
        case "three" | "four":
            result = (3,4)
        case _:
            result = 0
    print (result)
if __name__ == "__main__":
    main()

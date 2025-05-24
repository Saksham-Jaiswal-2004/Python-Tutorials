def formatName(fName, lName):
    newfName = fName.title()
    newlName = lName.title()

    print(newfName, newlName)

    return f"{newfName} {newlName}"


formattedString =  formatName("SakSHAM", "jaiSWal")
print(formattedString)


def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap_year(2400))
print(is_leap_year(1989))
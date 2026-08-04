def main():
    Day = input("How was your day?")
    Day= convert(Day)
    print(Day)
def convert(Day):
    Day= Day.replace(":)", "🙂")
    Day= Day.replace(":(", "🙁")
    return Day
main()



def main():
    time= input("What's the time?")
    exact_time= convert(time)
    if 7.0<= exact_time<=8.0:
        print("breakfast time")
    elif 12.0<= exact_time<= 13.0:
        print("lunch time")
    elif 18<= exact_time<= 19.0:
        print("dinner time")
    else:
        print(" ")



def convert(time):

    hour, minutes = time.split(":")
    exact_time= int(hour) + int(minutes)/60
    return exact_time


if __name__ == "__main__":
    main()

def main():
     answer=input("What time is it? ")
     inp_time=convert(answer)
     if inp_time>=12 and inp_time<=13:
          print("lunch time")

     elif inp_time>=18 and inp_time<=19:
          print("dinner time")

     elif inp_time>=7 and inp_time<=8:
          print("breakfast time")



def convert(time):
    hours, minutes = map(int,time.split(":"))
    combine = hours + minutes/60
    return combine


if __name__ == "__main__":
    main()





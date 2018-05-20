import cv2
import os
print "2"
import file_getter
print "3"
import SSH_comaner
print "4"
from subprocess import call

def brightness_calc():
    MY_ZERO = 0
    My_Hundred = 100000

    twenty_finalSum = 0
    sixsty_finalSum = 0
    eighty_five_finalSum = 0

    twenty = []
    sixsty = []
    eighty_five = []

    # picPath should be deleted from here
    PicsPath = "pic/"
    for picName in os.listdir(PicsPath):
        img = cv2.imread(PicsPath+"/"+picName, 0)
        sum = 0;
        counter = 0;
        for y in range(640):
            for x in range(480):
                # pixel = img.getpixel((x,y))
                pixel = img[x, y]
                if pixel >= MY_ZERO:

                    sum = sum + pixel
                    counter += 1
        if counter == 0:
            if picName.startswith("20"):
                twenty.append(counter)
            if picName.startswith("60"):
                sixsty.append(counter)
            elif picName.startswith("85"):
                eighty_five.append(counter)

        else:
            if picName.startswith('20'):
                twenty.append(sum)
            if picName.startswith("60"):
                sixsty.append(sum)
            elif picName.startswith("85"):
                eighty_five.append(sum)

    for i in range(len(twenty)):
        twenty_finalSum = twenty_finalSum + twenty[i]
    print("Gloss for 20 deg:", (twenty_finalSum/My_Hundred)*100)

    for i in range(len(sixsty)):
        sixsty_finalSum = sixsty_finalSum + sixsty[i]
    print("Gloss for 60 deg:", (sixsty_finalSum/My_Hundred)*100)

    for i in range(len(eighty_five)):
        eighty_five_finalSum = eighty_five_finalSum + eighty_five[i]
    print("Gloss for 85 deg:", (eighty_five_finalSum/My_Hundred)*100)

    return

def main():
    print "1"
    appleInside = 0
    print "Hello! Please insert a fruit to the box"
    while appleInside!= 1:
        appleInside = int(input("If the fruit is inside the box please enter 1"))
    if appleInside == 1:
        SSH_comaner.send_ssh_go()
        file_getter.get_files()
        brightness_calc()
        #SSH_comaner.send_ssh_go()




if __name__ == "__main__":
    main()

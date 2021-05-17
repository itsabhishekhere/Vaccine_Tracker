import requests
import winsound
import time


def user_input():
    print("\t --------- COVID VACCINE TRACKER -------")
    pin_code=input("PINCODE (for multiple use comma): ").split(",")
    pin_code = [int(i) for i in pin_code]
    preffered_date=input("Enter Date (in DD-MM-YYYY Format): ")
    age_limit=int(input("Age Category (18 or 45): "))
    print("\n")
    return  pin_code,preffered_date,age_limit

def vaccineChecker():
    pin_code, preffered_date, age_limit = user_input()
    present = 0
    msg_c = 0
    browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

    while True:
        for pin in pin_code:
            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pin, preffered_date)

            response = requests.get(URL, headers=browser_header)
            if response.ok:
                resp_json = response.json()

                for center in resp_json["centers"]:
                    for session in center["sessions"]:

                        if session["min_age_limit"] == age_limit and session["available_capacity"] > 0 :
                            present = 1
                            print("\t DATE: ", session["date"])
                            print("\t AGE CATEGORY: ", session["min_age_limit"])
                            print("\t CENTER NAME: ", center["name"])
                            print("\t", center["address"])
                            print("\t BLOCK: ", center["block_name"])
                            print("\t PRICE/FREE: ", center["fee_type"])
                            print("\t AVAILABLE : ", session["available_capacity"])
                            print("\t Vaccine: ", session["vaccine"])
                            print("\n")

            for i in range(2):
                if (present == 1):
                    winsound.Beep(640, 100)
                    winsound.Beep(540, 200)
                    winsound.Beep(740, 500)
                    winsound.Beep(850, 300)
                    winsound.Beep(540, 200)
                    winsound.Beep(650, 500)
                else:
                    if(msg_c==0):
                        print("\t------------ SEARCHING IN BACKEND----------\n Feel free to work, if we get slot we will notify you with BEEP.")
                        msg_c=1
        time.sleep(5)



def main():

        vaccineChecker()



if __name__ == "__main__":
    main()
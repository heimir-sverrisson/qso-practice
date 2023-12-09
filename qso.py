import sys
import send_code as sc
import read_code as rc


def send_cq(call_sign):
    sc.send_code(f"cq cq cq de {call_sign} {call_sign} k")


if __name__ == "__main__":
    while True:
        send_cq("w1aw")
        response = rc.read_code()
        print()
        if "w1aw" in response.lower() and "w1ant" in response.lower():
            print("Both call signs correct!")
            break

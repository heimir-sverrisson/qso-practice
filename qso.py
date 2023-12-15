import sys
import send_code as sc
import read_code as rc
import personas as ps


def send_cq(persona):
    call_sign = persona["call_sign"]
    sc.send_code(f"cq cq cq de {call_sign} {call_sign} k")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python qso.py <country>")
        sys.exit(1)
    country = sys.argv[1]
    if country.lower() not in ["usa", "iceland"]:
        print("Country must be USA or Iceland")
        sys.exit(1)
    persona = ps.get_persona(country)
    local_persona = ps.get_local_persona()
    while True:
        send_cq(persona)
        response = rc.read_code()
        print()
        if persona["call_sign"] in response and local_persona["call_sign"] in response:
            print("Both call signs correct!")
            break
        else:
            print(
                # f"Did not hear {persona['call_sign']} or {local_persona['call_sign']} in response."
                f"Did not hear call signs in the response."
            )

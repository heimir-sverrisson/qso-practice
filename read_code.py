from select import select
import sys
import tty, termios
import send_code


def add_to_buf(buf, c):
    """
    Add a character to the buffer and print it to stderr.
    """
    buf += c
    sys.stderr.write(c)
    sys.stderr.flush()
    return buf


def read_code(wpm=25, fwpm=15):
    _time_unit, fw_time_unit = send_code.get_timing(wpm, fwpm)
    timeout = 12 * fw_time_unit
    max_chars = 100
    try:
        prev_flags = termios.tcgetattr(sys.stdin.fileno())
        tty.setraw(sys.stdin.fileno())
    except Exception:
        prev_flags = None
    buf = ""
    max_wait_count = 5
    wait_count = 0
    while True:  # main loop
        rl, _wl, _xl = select([sys.stdin], [], [], timeout)
        if rl:  # some input
            wait_count = 0
            c = sys.stdin.read(1)
            buf = add_to_buf(buf, c)
            if len(buf) >= max_chars:
                break
        else:
            # timeout
            wait_count += 1
            if len(buf) > 0 and buf[-1] != " ":
                buf = add_to_buf(buf, " ")
            if wait_count >= max_wait_count:
                break
    if prev_flags is not None:
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, prev_flags)
    return buf.replace(" ", "").lower()


if __name__ == "__main__":
    read_code()
    sys.stderr.write("\n")

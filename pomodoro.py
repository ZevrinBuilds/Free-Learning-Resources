import time
import sys

def pomodoro(work_mins=25, break_mins=5):
    print(f"--- Starting {work_mins} min Focus Session ---")
    try:
        time.sleep(work_mins * 60)
        print("\n\aTIME'S UP! Take a break!")
        time.sleep(break_mins * 60)
        print("\n\aBreak over. Back to the grind.")
    except KeyboardInterrupt:
        print("\nSession cancelled.")

if __name__ == "__main__":
    # Simple CLI: usage python pomodoro.py 25 5
    args = sys.argv[1:]
    work = int(args[0]) if len(args) > 0 else 25
    brk = int(args[1]) if len(args) > 1 else 5
    pomodoro(work, brk)

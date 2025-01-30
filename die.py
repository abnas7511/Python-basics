import sys
import time

def print_lyrics():
    lines = [
        "So I'ma love you every night like it's the last night",
        "Like it's the last night",
        "If the world was ending",
        "I'd wanna be next to you",
        "If the party was over",
        "And our time on Earth was through",
        "I'd wanna hold you just for a while",
        "And die with a smile",
        "If the world was ending",
        "I'd wanna be next to you",
        "Right next to you"
    ]

    delays = [0.4,0.5,1.0,4.6,1.0,3.6,1.7,2.0,0.9,1.2,0.5]

    for i, line in enumerate(lines):
        for char in line:
            print(char, end='',flush=True)  
            time.sleep(0.1)
        time.sleep(delays[i])
        print('')
        
    
if __name__ == '__main__':
    print_lyrics()
    time.sleep(0.1)
    print("i love you")
    time.sleep(0.1)
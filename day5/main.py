import re

f = open('day5/input.txt')
lines = f.read().strip().splitlines()

#star 1
s = 0
seeds = [int(x) for x in re.findall("\d+", lines[0])]

mins = float('inf')
for seed in seeds:
    found = False
    s = seed
    for i, l in enumerate(lines[2:]):
        if l == '' or not (l[0].isdigit()):
            found = False
        elif found == False:
            dest_start, source_start, length = re.findall("\d+", l)
            dest_start = int(dest_start)
            source_start = int(source_start)
            length = int(length)
            if source_start <= s <= source_start + length:
                s = dest_start + (s - source_start)  # dest + delta
                found = True
    mins = min(mins, s)

print(f"star 1: total {mins}")

#start 2
s = 0
windows = []
for i in range(0, len(seeds), 2):
    windows.append((seeds[i], seeds[i] + seeds[i + 1] - 1))  #window of seed

next_windows = windows
new_windows = []
for i, l in enumerate(lines[2:]):
    if l == '' or not (l[0].isdigit()):
        next_windows.extend(windows)
        windows = next_windows
        next_windows = []
    elif len(windows) > 0:
        dest_start, source_start, length = [
            int(x) for x in re.findall("\d+", l)
        ]
        new_windows = []
        for w in windows:
            before = during = after = None
            source_end = source_start + length
            if w[0] < source_start:
                before = (w[0], min(source_start, w[1]))
                new_windows.append(before)
            if w[1] > source_end:
                after = (max(w[0], source_end), w[1])
                new_windows.append(after)
            # check if window is in range of source start and end
            if (w[0] <= source_start <= w[1] or w[0] <= source_end <= w[1]
                    or source_start <= w[0] <= source_end
                    or source_start <= w[1] <= source_end):
                # during : smallest interval intersection between window and source_interval
                during = (max(source_start, w[0]), min(source_end, w[1]))
                during_length = during[1] - during[0]

                offset = (max(source_start, w[0])) - source_start
                during_dest = (dest_start + offset,
                               dest_start + during_length + offset)
                next_windows.append(during_dest)
        windows = new_windows

# all windowds that have been through all the mapping
next_windows.extend(windows)
windows = next_windows

mins = float('inf')
for w in windows:
    mins = min(w[0], mins)
# smallest value of the window is our answer
print(f"star 2: total {mins}")

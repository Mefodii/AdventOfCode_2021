from re import match


def forward_a(pos, depth, dist):
    return pos + dist, depth


def down_a(pos, depth, dist):
    return pos, depth + dist


def up_a(pos, depth, dist):
    return pos, depth - dist


RUN_COMMAND_A = {
    "forward": forward_a,
    "down": down_a,
    "up": up_a,
}


def forward_b(pos, depth, aim, dist):
    return pos + dist, depth + aim * dist, aim


def down_b(pos, depth, aim, dist):
    return pos, depth, aim + dist


def up_b(pos, depth, aim, dist):
    return pos, depth, aim - dist


RUN_COMMAND_B = {
    "forward": forward_b,
    "down": down_b,
    "up": up_b,
}


def run_commands_a(raw_commands):
    pos = 0
    depth = 0
    for raw_command in raw_commands:
        matcher = match('(\w+)\s(\d+)', raw_command)
        command = matcher.group(1)
        dist = int(matcher.group(2))
        pos, depth = RUN_COMMAND_A[command](pos, depth, dist)

    return pos, depth


def run_commands_b(raw_commands):
    pos = 0
    depth = 0
    aim = 0
    for raw_command in raw_commands:
        matcher = match('(\w+)\s(\d+)', raw_command)
        command = matcher.group(1)
        dist = int(matcher.group(2))
        pos, depth, aim = RUN_COMMAND_B[command](pos, depth, aim, dist)

    return pos, depth


###############################################################################
def run_a(input_data):
    pos, depth = run_commands_a(input_data)
    result = pos * depth
    return result


def run_b(input_data):
    pos, depth = run_commands_b(input_data)
    result = pos * depth
    return result

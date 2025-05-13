def solution(string, markers):
    lines = string.split('\n')
    result_lines = []
    for line in lines:
        for marker in markers:
            if marker in line:
                line = line.split(marker)[0]
        result_lines.append(line.rstrip())
    return '\n'.join(result_lines)




def check_decreasing(levels) -> bool:
    safe=True
    for l1, l2 in zip(levels,levels[1:]):
        if not l1-l2 in range(1,4):
            safe=False
            break
    return safe


def check_increasing(levels) -> bool:
    safe=True
    for l1, l2 in zip(levels,levels[1:]):
        if not l2-l1 in range(1,4):
            safe=False
            break
    return safe



def check_report(levels:list[int]) -> bool:
    if levels[0] > levels[1]:
        return check_decreasing(levels)
    else:
        return check_increasing(levels)

    

def check_report_with_tolerance(levels:list[int]) -> bool:
    safe=False 
    
    for i in range(len(levels)): 
        if check_decreasing(levels[:i]+levels[i+1:]) or check_increasing(levels[:i]+levels[i+1:]):
            safe=True
    return safe


def map_int(line: list[str]):
    return [int(el) for el in line]

def parse_lines(lines):
    return [map_int(el.split(" ")) for el in lines]


def part_1(input: list[str]):

    safe_reports=0
    reports = parse_lines(input)

    for report in reports:
        safe=check_report(report)
        if safe:
            safe_reports=safe_reports+1
    
    return safe_reports


def part_2(input: list[str]):

    safe_reports=0
    reports = parse_lines(input)

    for report in reports:
        safe=check_report(report)
        if safe:
            safe_reports=safe_reports+1
        else:
           if check_report_with_tolerance(report):
               safe_reports=safe_reports+1
            
    return safe_reports







    


    


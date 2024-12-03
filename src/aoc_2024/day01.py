




def total_distance(left,right):

    total=0
    for l,r in zip(left,right):
        total = total + abs(l-r)
    return total

def get_left_right_list(input: list[str]):
    left_right_list = [l.split("   ") for l in input]

    left_list = sorted([int(el[0]) for el in left_right_list])
    right_list = sorted([int(el[1]) for el in  left_right_list])
    return left_list,right_list                    



def part_1(input: list[str]):

    left_list, right_list = get_left_right_list(input)
    return total_distance(left_list,right_list)

def find_similarity_score(el, right_list):

    filtered_list_of_element = [r for r in right_list if r==el]
    return len(filtered_list_of_element) * el


def total_similarities(left_list, right_list):

    similarities = [find_similarity_score(el,right_list) for el in left_list]
    return sum(similarities)


def part_2(input: list[str]):
    left_list, right_list = get_left_right_list(input)
    return total_similarities(left_list,right_list)


    


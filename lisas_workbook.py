def workbook(n, k, arr):

    page = 0
    specials = 0
    problem_number = 0

    for each_chapter in arr:
        for problem_index in range(each_chapter):
            problem_number = problem_index +1
            if problem_index % k == 0:
                page += 1
            if problem_number == page:
                specials += 1

    return(specials)
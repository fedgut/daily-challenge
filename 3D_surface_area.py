def surface_area(values):
    
    total = 0
    for i in range(len(values)):
        for j in range(len(values[i])):
            area_inicial = get_initial_surface_area(i,j, values)
            area_adjaciente = get_adjacent_surface_area(i,j, values)
            area_total = area_inicial - area_adjaciente
            total += area_total
    return total


def get_initial_surface_area(i, j, values):
    top_bottom = 2
    sides = values[i][j] * 4
    return sides + top_bottom


def get_adjacent_surface_area(i,j, values):
    current_val = values[i][j]
    val = 0
    val += get_adjacent(i+1, j, current_val)
    val += get_adjacent(i-1, j, current_val)
    val += get_adjacent(i, j+1, current_val)
    val += get_adjacent(i, j-1, current_val)
    return val


def get_adjacent(i, j, current_val):
    """get value of adjacent surface of a single side """
    try:
        adj_height = values[i][j]
        if adj_height > current_val:
            return current_val
        else:
            return adj_height
    except IndexError:
        return 0

def zero_array(length):
    return [0] * length


def get_side(length, l):
    bar = zero_array(length)
    max_val = min(length - l + 1, l)
    for i in range(max_val):
        bar[i] = bar[-(i + 1)] = i + 1
    bar[max_val:length - max_val] = [max_val] * (length - 2 * max_val)
    return bar

def compute_map(vertical_bars, horizontal_bars):
        # initialize empty 2d array with correct dimensions
        rows, cols = len(vertical_bars[0]), len(horizontal_bars[0])
        grid = [[0] * cols for _ in range(rows)]  # Initialize 2D array efficiently

        horizontal_sum = [sum(col) for col in zip(*horizontal_bars)]  # Sum horizontal contributions efficiently
        vertical_sum = [sum(row) for row in vertical_bars]  # Sum vertical contributions efficiently

        for r in range(rows):
            grid[r][0] = vertical_sum[r]  # First column assignment
        grid[0] = horizontal_sum  # First row assignment

        # Compute remaining grid values
        for r in range(1, rows):
            for c in range(1, cols):
                grid[r][c] = sum(vertical_bars[i][r] * horizontal_bars[i][c] for i in range(len(vertical_bars)))

        return grid

class Mapmaker:
    def init(self):
        pass

    def compute(self, arr):
        L = min(len(arr), len(arr[0]))

        vertical_bars = [get_side(len(arr), i + 1) for i in range(L)]
        horizontal_bars = [get_side(len(arr[0]), i + 1) for i in range(L)]

        computed_map = compute_map(vertical_bars, horizontal_bars)

        return sum(arr[r][c] * computed_map[r][c] for r in range(len(arr)) for c in range(len(arr[0])))
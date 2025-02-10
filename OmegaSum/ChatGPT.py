class ChatGPT:
    def init(self):
        pass

    def compute(self, matrix):
        # Initialize the total sigma sum to 0
        sigma_sum = 0
        N = len(matrix)
        M = len(matrix[0])

        # Iterate over all possible subarray sizes kxk where k ranges from 1 to min(N, M)
        for k in range(1, min(N, M) + 1):
            # For each kxk subarray, calculate the sum of all kxk subarrays
            for i in range(N - k + 1):  # i is the starting row index of the kxk subarray
                for j in range(M - k + 1):  # j is the starting column index of the kxk subarray
                    # Calculate the sum of the current kxk subarray
                    subarray_sum = 0
                    for x in range(k):
                        for y in range(k):
                            subarray_sum += matrix[i + x][j + y]
                    # Add the subarray sum to the sigma sum
                    sigma_sum += subarray_sum

        return sigma_sum
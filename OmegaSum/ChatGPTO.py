class ChatGPTO:
    def init(self):
        pass

    def compute(self, matrix):
        N, M = len(matrix), len(matrix[0])

        # Step 1: Compute prefix sum
        prefix = [[0] * (M + 1) for _ in range(N + 1)]
        for i in range(N):
            for j in range(M):
                prefix[i + 1][j + 1] = matrix[i][j] + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j]

        sigma_sum = 0

        # Step 2: Compute sum of all kxk subarrays efficiently
        for k in range(1, min(N, M) + 1):
            for i in range(N - k + 1):
                for j in range(M - k + 1):
                    # Use prefix sum to compute the kxk sum in O(1) time
                    subarray_sum = (prefix[i + k][j + k] - prefix[i][j + k] - prefix[i + k][j] + prefix[i][j])
                    sigma_sum += subarray_sum

        return sigma_sum
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> frequency = new HashMap<>();
      
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>(
            (a, b) -> b[1] - a[1]
        );

        // Count frequencies
        for (int num : nums) {
            frequency.put(num, frequency.getOrDefault(num, 0) + 1);
        }

        // Put [number, frequency] into max heap
        for (Map.Entry<Integer, Integer> entry : frequency.entrySet()) {
            maxHeap.offer(new int[]{entry.getKey(), entry.getValue()});
        }

        // Get top k
        int[] ans = new int[k];

        for (int i = 0; i < k; i++) {
            int[] current = maxHeap.poll();
            ans[i] = current[0];
        }

        return ans;
    }
}
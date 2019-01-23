class MyHeap:
    def __init__(self):
        self.heap = []

    def get_parent_index(self, node_index):
        if node_index % 2:
            index = (node_index - 1) // 2
        else:
            index = (node_index - 2) // 2
        return max(index, 0)

    def get_left_child_index(self, node_index):
        index = 2 * node_index + 1
        if index >= len(self.heap):
            return -1
        else:
            return index

    def get_right_child_index(self, node_index):
        index = 2 * node_index + 2
        if index >= len(self.heap):
            return -1
        else:
            return index

    def extract_max(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_value = self.heap.pop()
        i = 0
        child_index = 0
        while True:
            left_child_index = self.get_left_child_index(i)
            right_child_index = self.get_right_child_index(i)
            if left_child_index == -1 and right_child_index == -1:
                break
            if right_child_index == -1 or self.heap[left_child_index] >= self.heap[right_child_index]:
                child_index = left_child_index
            else:
                child_index = right_child_index
            if self.heap[i] >= self.heap[child_index]:
                break
            else:
                self.heap[i], self.heap[child_index] = self.heap[child_index], self.heap[i]
                i = child_index
        return max_value

    def insert(self, value):
        i = len(self.heap)
        self.heap.append(value)
        while True:
            parent_index = self.get_parent_index(i)
            if self.heap[parent_index] >= self.heap[i] or i == parent_index:
                break
            else:
                self.heap[parent_index], self.heap[i] = self.heap[i], self.heap[parent_index]
                i = parent_index

    def __str__(self):
        return str(self.heap)


def main():
    n = int(input())
    heap = []
    queue = MyHeap()
    for i in range(n):
        t = tuple(map(str, input().split(" ")))
        heap.append(t)
    for t in heap:
        if t[0] == "Insert":
            queue.insert(int(t[1]))
        if t[0] == "ExtractMax":
            print(queue.extract_max())


if __name__ == "__main__":
    main()

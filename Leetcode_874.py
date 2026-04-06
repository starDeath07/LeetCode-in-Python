class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        # Convert obstacles to a set of tuples for O(1) lookup
        obstacle_set = set((x, y) for x, y in obstacles)

        # North, East, South, West
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0  # start facing North

        x, y = 0, 0
        max_dist = 0

        for command in commands:
            if command == -1:  # turn right
                direction = (direction + 1) % 4
            elif command == -2:  # turn left
                direction = (direction + 3) % 4
            else:
                dx, dy = dirs[direction]

                for _ in range(command):
                    nx, ny = x + dx, y + dy

                    # stop if obstacle ahead
                    if (nx, ny) in obstacle_set:
                        break

                    x, y = nx, ny
                    max_dist = max(max_dist, x * x + y * y)

        return max_dist

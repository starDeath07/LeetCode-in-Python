class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        asteroids.sort()

        for asteroid in asteroids:
            if asteroid <= mass:
                mass += asteroid
            else:
                return False
        return True


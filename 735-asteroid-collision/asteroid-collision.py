class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            # Collision happens only when stack top is moving right (>) and current is moving left (<)
            while stack and stack[-1] > 0 and a < 0:
                if stack[-1] < -a:
                    stack.pop()  # Top asteroid explodes
                    continue
                elif stack[-1] == -a:
                    stack.pop()  # Both explode
                break            # Current asteroid explodes
            else:
                stack.append(a)  # Survives or no collision condition met
        return stack

        
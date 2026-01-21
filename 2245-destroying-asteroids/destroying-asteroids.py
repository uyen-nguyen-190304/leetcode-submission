class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # Sort the asteroids' mass in ascending order
        asteroids.sort()
        
        # Greedily destroy the asteroids
        for asteroid in asteroids:
            
            # If the smallest asteroid's mass is bigger than the planet's mass, the planet will be destroyed
            if asteroid > mass:
                return False
            
            # Else, the planet will destroy the asteroid -> Add mass
            mass += asteroid
        
        # Loop through every asteroid. If still here, then all asteroids can be destroyed
        return True
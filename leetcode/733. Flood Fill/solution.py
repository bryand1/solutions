class Solution:
    def floodFill(self, image: 'List[List[int]]', sr: 'int', sc: 'int', newColor: 'int') -> 'List[List[int]]':
        if image[sr][sc] == newColor:
            return image
        self.fill(image, sr, sc, image[sr][sc], newColor)
        return image

    def fill(self, image: 'List[List[int]]', y: 'int', x: 'int', color: 'int', newColor: 'int'):
        if y < 0 or y >= len(image) or x < 0 or x >= len(image[y]) or image[y][x] != color:
            return
        
        image[y][x] = newColor

        self.fill(image, y - 1, x, color, newColor)
        self.fill(image, y + 1, x, color, newColor)
        self.fill(image, y, x - 1, color, newColor)
        self.fill(image, y, x + 1, color, newColor)

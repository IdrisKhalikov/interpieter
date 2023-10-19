from Pointer import Pointer


class ProgramSource:
    def __init__(self, source):
        self._source = source

    def get_color(self, position: Pointer):
        return self._source[position.y][position.x]

    def get_color_block(self, position: Pointer):
        if self._is_out_of_bounds(position):
            return ColorBlock(None, None)
        color = self.get_color(position)
        return ColorBlock(color, self._get_all_codels(position))

    def _get_all_codels(self, position):
        stack = []
        adjacent = set()
        color = self.get_color(position)
        stack.append(position)

        while stack:
            cur_pos = stack.pop()
            adjacent.add(cur_pos)
            for neighbour in self._get_adjacent(cur_pos):
                if self.get_color(neighbour) == color:
                    if neighbour not in adjacent:
                        stack.append(neighbour)
        return adjacent

    def _get_adjacent(self, position):
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                if ((x == 0) ^ (y == 0)):
                    next_pos = Pointer(position.x + x, position.y + y)
                    if not self._is_out_of_bounds(next_pos):
                        yield next_pos

    def _is_out_of_bounds(self, position):
        if (position.x < 0 or
                position.y < 0 or
                position.x >= len(self._source[0]) or
                position.y >= len(self._source)):
            return True
        return False


class ColorBlock:

    def __init__(self, color, codel_set):
        self._codels = codel_set
        self._color = color

    def get_edge(self, direction, codel_chooser):
        if not self._codels:
            raise Exception('Empty color block')
        corner_vector = direction + codel_chooser

        def vector_comp(pointer):
            if direction.x != 0:
                return (pointer.x * corner_vector.x, pointer.y * corner_vector.y)
            return (pointer.y * corner_vector.y, pointer.x * corner_vector.x)
        return sorted(self._codels, key=vector_comp)[-1]

    def get_value(self):
        return len(self._codels)

    def get_color(self):
        return self._color

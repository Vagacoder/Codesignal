#
# * Core 128. Amazon Checkmate

# * An amazon (also known as a queen + knight compound) is an imaginary chess 
# * piece that can move like a queen or a knight (or, equivalently, like a rook, 
# * bishop, or knight). The diagram below shows all squares which the amazon can 
# * attack from e4 (circles represent knight-like moves while crosses correspond 
# * to queen-like moves).

# Recently, you've come across a diagram with only three pieces left on the board: 
# a white amazon, the white king, and the black king. It's black's move. You don't 
# have time to determine whether the game is over or not, but you'd like to figure 
# it out in your head. Unfortunately, the diagram is smudged and you can't see 
# the position of the black king, so you'll need to consider all possible positions.

# Given the positions of the white pieces on a standard chessboard (using algebraic 
# notation), your task is to determine the number of possible black king's positions 
# such that:

#     it's checkmate (i.e. black's king is under the amazon's attack and it cannot 
#       make a valid move);
#     it's check (i.e. black's king is under the amazon's attack but it can reach 
#       a safe square in one move);
#     it's stalemate (i.e. black's king is on a safe square but it cannot make a 
#       valid move);
#     black's king is on a safe square and it can make a valid move.

# Note that two kings cannot be placed on two adjacent squares (including two 
# diagonally adjacent ones).

# * Example

#     For king = "d3" and amazon = "e4", the output should be
#     amazonCheckmate(king, amazon) = [5, 21, 0, 29].

#     Red crosses correspond to the checkmate positions, orange pluses refer to 
#     check positions, and green circles denote safe squares.

#     For king = "a1" and amazon = "g5", the output should be
#     amazonCheckmate(king, amazon) = [0, 29, 1, 29].

#     The stalemate position is marked by a blue square.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string king

#     The position of the white king, in chess notation.

#     Guaranteed constraints:
#     king.length = 2,
#     'a' ≤ king[0] ≤ 'h',
#     1 ≤ king[1] ≤ 8.

#     [input] string amazon

#     The position of the white amazon, in the same notation.

#     Guaranteed constraints:
#     amazon.length = 2,
#     'a' ≤ amazon[0] ≤ 'h',
#     1 ≤ amazon[1] ≤ 8,
#     amazon ≠ king.

#     [output] array.integer

#     An array of four integers, each equal to the number of black's king positions corresponding to a specific situation. More specifically, the array should be of the form [checkmate positions, check positions, stalemate positions, safe positions].

#%%

# * Solution 1

def amazonCheckmate(king, amazon):
    import itertools
    from string import ascii_lowercase as files

    SIZE = 8

    squares = tuple(''.join(square[::-1]) for square in
                itertools.product(map(str, range(1, SIZE+1)), files[:SIZE]))
    coords = tuple(itertools.product(range(SIZE), range(SIZE)))

    def is_in_bounds(square):
        return 0 <= square < SIZE

    def king_moves(rank, file):
        moves = []
        if rank - 1 >= 0:
            moves += [(rank-1, f) for f in range(file-1, file+2) if is_in_bounds(f)]
        moves += [(rank, f) for f in (file-1, file+1) if is_in_bounds(f)]
        if rank + 1 < SIZE:
            moves += [(rank+1, f) for f in range(file-1, file+2) if is_in_bounds(f)]
        return moves

    def rook_moves(rank, file):
        moves = [[(r, file) for r in range(rank-1, -1, -1)]]
        moves += [[(r, file) for r in range(rank+1, SIZE)]]
        moves += [[(rank, f) for f in range(file-1, -1, -1)]]
        moves += [[(rank, f) for f in range(file+1, SIZE)]]
        return moves

    def bishop_moves(rank, file):
        down = range(-1, -rank-1, -1)
        up = range(1, SIZE-rank)
        moves = [[(rank+i, file-i) for i in down if is_in_bounds(file-i)]]
        moves += [[(rank+i, file+i) for i in down if is_in_bounds(file+i)]]
        moves += [[(rank+i, file-i) for i in up if is_in_bounds(file-i)]]
        moves += [[(rank+i, file+i) for i in up if is_in_bounds(file+i)]]
        return moves

    def knight_moves(rank, file):
        offsets = ((-2, -1), (-2, 1),
                (-1, -2), (-1, 2),
                (1, -2), (1, 2),
                (2, -1), (2, 1))
        moves = [(rank+x, file+y) for x, y in offsets
                if is_in_bounds(rank+x) and is_in_bounds(file+y)]
        return moves

    def filter_ray_attacks(moves, piece_coords):
        filtered_moves = []
        for direction in moves:
            if piece_coords in direction:
                # +1 because it can influence the friendly occupied square
                direction = direction[:direction.index(piece_coords)+1]
            filtered_moves += direction
        return filtered_moves

    def amazon_moves(rank, file, king):
        moves = (filter_ray_attacks(rook_moves(rank, file), king) +
                filter_ray_attacks(bishop_moves(rank, file), king) +
                knight_moves(rank, file))
        return moves

    def has_escape_squares(square, piece_moves, attacks):
        for move in piece_moves:
            if move not in attacks:
                return True
        return False


    # * =============================
    for piece in (king, amazon):
        if piece not in squares:
            raise ValueError('{} is not a valid square.'.format(piece))
    if king == amazon:
        raise ValueError('The king and amazon must not occupy the same square.')

    king = coords[squares.index(king)]
    amazon = coords[squares.index(amazon)]

    king_attacks = king_moves(*king)
    all_attacks = set(king_attacks + amazon_moves(*amazon, king))

    black_not_allowed_squares = set([king, amazon] + king_attacks)
    black_king_positions = (square for square in coords
                            if square not in black_not_allowed_squares)

    # `result` is 4-item list:
    # 0 - checkmate
    # 1 - check
    # 2 - stalemate
    # 3 - safe
    # 0-1 means the king is initially in check and 2-3 not.
    # Therefore, we define `check_offset` as either 0 or 2.
    # Between 0 and 1 (or 2 and 3) the difference is whether the king
    # has any safe moves. This is represented by the `escape_offset`, which
    # is either 0 or 1.
    # The final state is then `check_offset + escape_offset`.
    result = [0] * 4
    for square in black_king_positions:
        black_king_moves = king_moves(*square)
        check_offset = 2 * (1 - (square in all_attacks))
        escape_offset = has_escape_squares(
            square, black_king_moves, all_attacks)
        result[check_offset + escape_offset] += 1
    return result



k1 = 'd3'
a1 = 'e4'
r1 = amazonCheckmate(k1, a1)
print(r1)

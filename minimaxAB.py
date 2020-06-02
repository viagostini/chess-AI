from evaluate_board import evaluate

# TODO: make players some form of object with different strategies

def minimaxAB_player(board, depth=3):
    moves = board.legal_moves
    
    is_max = True
    best_score = float('-inf')
    
    # hack because we can't use next() on board.legal_moves
    for move in moves:
        best_move = move
        break
    
    for move in moves:
        board.push(move)
        score = minimaxAB(board, depth-1, float('-inf'), float('inf'), not is_max)
        board.pop()
        
        if score > best_score:
            best_move = move
            best_score = score
        
    return best_move.uci()

def minimaxAB(board, depth, alpha, beta, is_max):
    if not depth:
        return evaluate(board, not board.turn)
    
    moves = board.legal_moves
    
    best_score = float('-inf') if is_max else float('inf')
    
    for move in moves:
        board.push(move)
        score = minimaxAB(board, depth-1, alpha, beta, not is_max)
        board.pop()
        
        if is_max:
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
        else:
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            
        if beta <= alpha:
            return best_score
    
    return best_score
        
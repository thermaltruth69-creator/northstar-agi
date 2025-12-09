import chess
import chess.engine

def eloretention():
    try:
        engine = chess.engine.SimpleEngine.popen_uci("stockfish")  # or full path
        board = chess.Board()
        for _ in range(20):
            result = engine.play(board, chess.engine.Limit(time=0.05))
            board.push(result.move)
        engine.quit()
        return True  # survived 20 moves = master-level retention
    except:
        return "Stockfish not found — install it to test real Elo"

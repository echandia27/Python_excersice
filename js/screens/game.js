import { createBoard, renderBoard } from "../gameLogic/board.js";
export const btn = document.getElementById("start"); 

export function renderGame() {
    btn.addEventListener("click", () => { 
        startagame();   
    });
}

function startagame() { 
    const app = document.getElementById("app");
    app.innerHTML = `
    <section class="game-screen">
        <header class="game-header">
            <h2>Afrodita Crush 💖</h2>
            <div class="game-info">
                <span>Puntaje: <strong class ="puntaje">0</strong></span>
                <span>Movimientos: <strong class="movimientos">20</strong></span>
                <span>Tiempo: <strong class ="tiempo">120</strong></span>
            </div>
        </header>
        
        <div id="board" class="board"></div>
    </section>
    `;

    const boardContainer = document.getElementById("board");
    const board = createBoard();
    renderBoard(board, boardContainer);
}
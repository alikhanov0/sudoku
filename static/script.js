document.addEventListener("DOMContentLoaded", () => {
    const inputs = document.querySelectorAll("input");

    inputs.forEach(input => {
        function clearAll() {
            document.querySelectorAll("input").forEach(el => {
                el.classList.remove("highlight", "active", "same-number");
            });
        }
        // 🔹 фокус
        input.addEventListener("focus", () => {
            clearAll();

            const row = parseInt(input.dataset.row);
            const col = parseInt(input.dataset.col);
            const value = input.value;

            highlight(row, col);

            if (value) {
                highlightSame(value, input);
            }
        });

        // 🔹 ввод
        input.addEventListener("input", () => {
            if (input.classList.contains("fixed")) return;

            input.value = input.value.replace(/[^1-9]/g, "");

            input.addEventListener("input", () => {
                if (input.classList.contains("fixed")) return;

                input.value = input.value.replace(/[^1-9]/g, "");

                checkErrors();
            });
        });

        // 🔹 стрелки
        input.addEventListener("keydown", (e) => {
            const row = parseInt(input.dataset.row);
            const col = parseInt(input.dataset.col);

            let newRow = row;
            let newCol = col;

            if (e.key === "ArrowUp") newRow--;
            else if (e.key === "ArrowDown") newRow++;
            else if (e.key === "ArrowLeft") newCol--;
            else if (e.key === "ArrowRight") newCol++;
            else return;

            e.preventDefault();

            const next = document.querySelector(
                `input[data-row='${newRow}'][data-col='${newCol}']`
            );

            if (next) next.focus();
        });

    });

    // ---------------------

    function highlight(row, col) {
        document.querySelectorAll(`input[data-row='${row}']`)
            .forEach(el => el.classList.add("highlight"));

        document.querySelectorAll(`input[data-col='${col}']`)
            .forEach(el => el.classList.add("highlight"));

        document.querySelector(`input[data-row='${row}'][data-col='${col}']`)
            .classList.add("active");
    }

    function highlightSame(value, currentInput) {
        if (!value) return;

        document.querySelectorAll("input").forEach(el => {
            if (el.value === value && el !== currentInput) {
                if (!el.classList.contains("error")) {
                    el.classList.add("same-number");
                }
            }
        });
    }

    function clearAll() {
        document.querySelectorAll("input").forEach(el => {
            el.classList.remove("highlight", "active", "same-number");
        });
    }

    function clearErrors() {
        document.querySelectorAll("input")
            .forEach(el => el.classList.remove("error"));
    }

    // 🔴 проверка ошибок
    function checkErrors() {
        inputs.forEach(input => {
            input.classList.remove("error");

            if (input.classList.contains("fixed")) return;

            const val = input.value;
            if (!val) return;

            const row = input.dataset.row;
            const col = input.dataset.col;

            let isError = false;

            // проверка строки
            document.querySelectorAll(`input[data-row='${row}']`)
                .forEach(el => {
                    if (el !== input && el.value === val) {
                        isError = true;
                    }
                });

            // проверка колонки
            document.querySelectorAll(`input[data-col='${col}']`)
                .forEach(el => {
                    if (el !== input && el.value === val) {
                        isError = true;
                    }
                });

            // проверка блока 3x3
            const startRow = Math.floor(row / 3) * 3;
            const startCol = Math.floor(col / 3) * 3;

            for (let i = startRow; i < startRow + 3; i++) {
                for (let j = startCol; j < startCol + 3; j++) {
                    const el = document.querySelector(
                        `input[data-row='${i}'][data-col='${j}']`
                    );
                    if (el !== input && el.value === val) {
                        isError = true;
                    }
                }
            }

            if (isError) {
                input.classList.add("error");
            }
        });
    }

});
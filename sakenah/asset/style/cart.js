    document.addEventListener("DOMContentLoaded", function () {
        // mencari elemen untuk tambah- kurang - hapus
        const addButton = document.querySelectorAll(".add");
        const subtractButton = document.querySelectorAll(".subtract");
        const removeButton = document.querySelectorAll(".remove");
        const countElements = document.querySelectorAll(".count");
        const priceElements = document.querySelectorAll(".price strong");
        const totalElement = document.querySelector(".total strong");

        // total price
        function calculateTotal() {
            let total = 0;
            for (let i = 0; i < countElements.length; i++) {
                const count = parseInt(countElements[i].textContent);
                const price = parseInt(priceElements[i].textContent.replace("Rp.", "").replace(",", "").trim());
                total += count * price;
            }
            totalElement.textContent = `Rp.${total.toLocaleString()}`;
        }

        // tambah
        addButton.forEach(function (button, index) {
            button.addEventListener("click", function () {
                const count = parseInt(countElements[index].textContent);
                countElements[index].textContent = count + 1;
                calculateTotal();
            });
        });

        // kurang
        subtractButton.forEach(function (button, index) {
            button.addEventListener("click", function () {
                const count = parseInt(countElements[index].textContent);
                if (count > 1) {
                    countElements[index].textContent = count - 1;
                    calculateTotal();
                }
            });
        });

        // hapus
        removeButton.forEach(function (button, index) {
            button.addEventListener("click", function () {
                const count = parseInt(countElements[index].textContent);
                if (count > 0) {
                    countElements[index].textContent = 0;
                    calculateTotal();
                }
            });
        });
    });

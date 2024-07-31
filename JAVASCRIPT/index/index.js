document.addEventListener('DOMContentLoaded', function() {
    const data = [
        { category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티', price: '390,000' },
        { category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠', price: '188,000' },
        { category: "신발", brand: 'Nike', product: '에어포스 1', price: '137,000' },
        { category: "패션잡화", brand: 'Music&Goods', product: '빵빵이 키링', price: '29,000' },
    ];

    const dataTable = document.getElementById('data-table');

    data.forEach((item) => {
        const row = dataTable.insertRow();
        row.insertCell(0).textContent = item.category;
        row.insertCell(1).textContent = item.brand;
        row.insertCell(2).textContent = item.product;
        row.insertCell(3).textContent = item.price;
    });
    // 시계
    function updateClock() {
        const now = new Date();
        const hours = now.getHours().toString().padStart(2, '0');
        const minutes = now.getMinutes().toString().padStart(2, '0');
        const seconds = now.getSeconds().toString().padStart(2, '0');
        const dateString = now.toLocaleDateString('ko-KR', { year: 'numeric', month: 'long', day: 'numeric' });
        const timeString = `${hours}:${minutes}:${seconds}`;
        document.getElementById('clock').textContent = `${dateString} ${timeString}`;
    }

    updateClock();

    setInterval(updateClock, 1000);
});
// 다크모드
document.addEventListener('DOMContentLoaded', function(){
    const main = document.querySelector('body');
    const darkModeSwitch = document.getElementById('darkModeSwitch');

    darkModeSwitch.addEventListener('change', () => {
        main.classList.toggle('dark-theme', darkModeSwitch.checked);
    });
});
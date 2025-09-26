import domController from "./domController.js";

const subjectWindowBtns = [...document.querySelectorAll(".subject-button")];
const checkboxs = {};

const domCntrl = domController();

const getCheckedCount = (arr) => arr.filter(box => box.checked).length;

const updateSubjectCounter = (windowEl) => {
    const isClosed = !target.classList.contains("active");
    const { id } = target;

    if (isClosed) {
        const counter = target.querySelector(".selected-count");
        const boxArr = checkboxs[id];
        const count = getCheckedCount(boxArr);
        counter.textContent = count;
        if (count) {
            target.classList.add("selected");
        } else {
            target.classList.remove("selected");
        }
    }
} 

function toggleWindow(e) {
    e.preventDefault();
    let target = e.target;
    target = target.closest('.subject-container');
    target.classList.toggle('active');

    const isClosed = !(target.classList.contains('active'));
    const { id } = target;
    
    if (isClosed) {
        const counter = target.querySelector(".selected-count");
        const boxArr = checkboxs[id];
        const count = getCheckedCount(boxArr);
        counter.textContent = count;
        if (count) {
            target.classList.add("selected");
        } else {
            target.classList.remove("selected");
        }
    } 
}

subjectWindowBtns.forEach(btn => btn.onclick = toggleWindow)
// enable modal functionality
// add to head <script src="static/modal.js"></script>
// use <div class='modal'> and child <div class='modal-content'>
// add class 'persistent' to disable escaping

const openModal = (id) => {
    $(`#${id}`).fadeIn(300);
}

const closeModal = () => {
    $('.modal').fadeOut(200);
}

window.onclick = (e) => {
    if ($(e.target).hasClass('modal') && !$(e.target).hasClass('persistent')) {
        closeModal();
    };
};

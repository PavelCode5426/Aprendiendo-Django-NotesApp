// $(document).ready(function () {
//     const new_note=$('#new_note');
//     const new_notebook=$('#new_notebook');
//
//     new_notebook.on('hide.bs.modal',clearForm);
//     new_note.on('hide.bs.modal',clearForm);
//
//     $('.create-new-note').click(function (event) {
//         event.preventDefault();
//         handleModal(new_note,'Nueva Nota')
//     });
//     $('.create-new-notebook').click(function (event) {
//         event.preventDefault();
//         handleModal(new_notebook,'Nueva Libreta')
//     });
//     $('.edit-notebook').click(function (event) {
//         event.preventDefault();
//         handleModal(new_notebook,'Editar Libreta')
//     });
//     $('.edit-note').click(function (event) {
//         event.preventDefault();
//         handleModal(new_note,'Editar Nota')
//     });
//
//
//
//
//
//     $('.cancel-modal').click(function (event)
//     {
//         event.preventDefault();
//         new_note.modal('hide');
//         new_notebook.modal('hide');
//     });
//
//
//
//
//     function handleModal(modal,textHeader){
//         new_note.find('.modal-title').html(textHeader);
//         new_note.modal('show');
//     }
//     function clearForm(){
//         $('.form-control').val('');
//         $('.form-control').html('')
//     }
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
// });

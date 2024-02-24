const alertPlaceholder = document.getElementById('Alert');

const appendAlert = (message, type) => {
  const wrapper = document.createElement('div');
  wrapper.innerHTML = [
    `<div class="alert alert-${type} alert-dismissible" role="alert" style="position: fixed; top: 100px; left: 10px;">`,
    `   <div>${message}</div>`,
    '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
    '</div>',
  ].join('');

  alertPlaceholder.innerHTML = '';
  alertPlaceholder.append(wrapper);

  setTimeout(() => {
    alertPlaceholder.innerHTML = '';
  }, 5000);
};

const alertTrigger = document.getElementById('send');
if (alertTrigger) {
  alertTrigger.addEventListener('click', (event) => {
    appendAlert('Se ha realizado el registro exitosamente', 'success');
  });
}
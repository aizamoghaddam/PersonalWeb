let $ = document

// Modal btn Condition
const modal = $.getElementById('ModalConection')
let btnShowModal = $.getElementById('ClickMeBtn')
let exitModalElem = $.getElementById('Exit-Modal')

// Download File PDF Resume
function downloadFile() {

  const fileResume = $.createElement('a')
  
  fileResume.setAttribute('href', '../DownloadsFile/ComingSoon.txt')
  
  fileResume.setAttribute('download', 'ComingSoon.txt')

  $.body.appendChild(fileResume)
  fileResume.click()

  $.body.removeChild(fileResume)
}
// WorkSample Btn Go GItHUb
function workSampleLink() {
  window.location.href = 'https://github.com/khodewmj'
}

// Modal btn Condition
function showModal() {
  modal.style.display = 'block'
  modal.style.backdropFilter = 'blur(12px)'
}
function exitModal() {
  modal.style.display = 'none'
}
function hideModaWithEsc(event) {
  if (event.keyCode === 27) {
      modal.style.display = 'none'
  }
}


// Download File PDF Resume
$.getElementById('DownloadsFile').addEventListener('click', downloadFile)

// WorkSample Btn Go GItHUb
$.getElementById('WorkSample').addEventListener('click', workSampleLink)

// Modal btn Condition
btnShowModal.addEventListener('click', showModal)
exitModalElem.addEventListener('click', exitModal)
$.body.addEventListener('keyup', hideModaWithEsc)
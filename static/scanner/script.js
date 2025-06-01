function domReady(fn) {
  if (
    document.readyState === "complete" ||
    document.readyState === "interactive"
  ) {
    setTimeout(fn, 1000);
  } else {
    document.addEventListener("DOMContentLoaded", fn);
  }
}

const ticketForm = document.getElementById("ticket-form");
// const ticketId = document.createElement("input");
// ticketId.type = "hidden";
// ticketId.name = "ticketId";
// ticketId.value = "";
const ticketId = document.getElementById("ticketId");

domReady(function () {
  function onScanSuccess(decodeText, decodeResult) {
    // alert("Your QR is: " + decodeText, decodeResult);
    // alert(`Ticket Id: ${decodeResult}`);
    window.location.href = `tickets/${decodeText}/`;
    // ticketId.value = decodeText;
    // ticketForm.action = `tickets/${decodeText}`;
    // ticketForm.submit();
  }

  let htmlscanner = new Html5QrcodeScanner("my-qr-reader", {
    fps: 10,
    qrbos: 250,
  });
  htmlscanner.render(onScanSuccess);
});

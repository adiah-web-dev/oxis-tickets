document.addEventListener('DOMContentLoaded', () => {
	// event handler for the add ticket button on the order page
	document.querySelector('#add-ticket').addEventListener('click', addTicket);
})

const tickets = []
let ticketCount = 0;

const invoiceTable = document.getElementById('invoiceTable')
const ticketForm = document.getElementById('ticketForm')
const orderForm = document.getElementById('order-form')

// Add a hidden input to store the number of tickets
const ticketCountInput = document.createElement('input');
ticketCountInput.type = 'hidden';
ticketCountInput.name = 'ticketCount';
ticketCountInput.value = ticketCount;

orderForm.appendChild(ticketCountInput)

// Stop the form from submitting
ticketForm.addEventListener('submit', event => {
	event.preventDefault()
})

const addTicket = () => {
	const formData = new FormData(ticketForm);

	const name = formData.get('ticket-name');
	const type = formData.get('ticket-type');

	// check for ticket info before adding it
	if (name.length > 0 && type.length > 0) {
		let text = ''
		let price = 0

		switch (type) {
			case 'p':
				text = 'Parent';
				price = 125;
				break;

			case 'g':
				text = 'Graduand';
				price = 550;
				break;

			case 'ge':
				text = 'Graduand - Early Years';
				price = 250;
				break;

			case 'ng':
				text = 'Non Graduating Student';
				price = 100;
				break;

			case 'd':
				text = 'Graduand\'s Plus One';
				price = 250;
				break;

			default:
				text = 'Graduand';
				price = 550;
				break;
		}

		let newRow = invoiceTable.insertRow(-1);

		let typeCell = newRow.insertCell(0);
		let newType = document.createTextNode(text);
		typeCell.appendChild(newType);

		let nameCell = newRow.insertCell(1);
		let newName = document.createTextNode(name);
		nameCell.appendChild(newName);

		let numberCell = newRow.insertCell(2);
		let newNumber = document.createTextNode('');
		numberCell.appendChild(newNumber);

		let priceCell = newRow.insertCell(3);
		let newPrice = document.createTextNode(`$${price}.00`);
		priceCell.appendChild(newPrice);

		const newTicket = {name, type, price};
		tickets.push(newTicket);

		const total = tickets.reduce((total, ticket) => total + ticket.price, 0)
		const totalCell = document.getElementById('order-total')
		totalCell.textContent = `$${total}.00`

		// Add hidden inputs for each of the tickets
		const ticketName = document.createElement('input');
		ticketName.type = 'hidden';
		ticketName.name = `ticketName${ticketCount}`;
		ticketName.value = name;

		const ticketType = document.createElement('input');
		ticketType.type = 'hidden';
		ticketType.name = `ticketType${ticketCount}`;
		ticketType.value = type;

		orderForm.appendChild(ticketName);
		orderForm.appendChild(ticketType);

		ticketCount += 1;
		ticketCountInput.value = ticketCount

	} else {
		alert('Ticket info not filled in');
	}

	$('#modal-add-ticket').modal('hide')
	ticketForm.reset()
}

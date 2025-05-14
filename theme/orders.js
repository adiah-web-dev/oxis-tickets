document.addEventListener('DOMContentLoaded', () => {
	// event handler for the add ticket button on the order page
	document.querySelector('#add-ticket').addEventListener('click', add_ticket);

	// Get the ticket info and order info to save to database
	// document.querySelector('#add-order').addEventListener('click', addOrder)
	document.querySelector('#order-form').onsubmit = () => {
		addOrder();
		return false;
	}
})

const invoiceTable = document.getElementById('invoiceTable')
const tickets = []

// django function - used to get csrf_token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

let ticketCount = 0;

const add_ticket = () => {
	let name = document.querySelector('#ticket-name').value
	let ticketType = document.querySelector('#ticket-type').value

	// Check if the ticket has info in it before adding
	if (name.length > 0 && ticketType.length > 0 ) {
		ticketCount += 1;
		let newRow = invoiceTable.insertRow(-1)
		let typeCell = newRow.insertCell(0)
		let newType = document.createTextNode(ticketType)
		typeCell.appendChild(newType)

		let nameCell = newRow.insertCell(1)
		let newName = document.createTextNode(name)
		nameCell.appendChild(newName)

		let numberCell = newRow.insertCell(2)
		let newNumber = document.createTextNode('')
		numberCell.appendChild(newNumber)

		let priceCell = newRow.insertCell(3)
		let price = 0
		switch (ticketType) {
			case 'p':
				price = 125
			case 'g':
				price = 550
			case 'ge':
				price = 250
			case 'ng':
				price = 100
			case 'd':
				price = 250
			default:
				price = 550
		}
		let newPrice = document.createTextNode(`$${price}.00`)
		priceCell.appendChild(newPrice)

		const newTicket = {
			'name': name,
			'type': ticketType,
			'price': price
		}

		tickets.push(newTicket)

	} else {
		alert("Ticket info not filled in")
	}
}


const addOrder = () => {
	const csrftoken = getCookie('csrftoken')

	// Date should be added by django database
	const name = document.querySelector('#full_name').value
	const email = document.querySelector('#email').value
	const phone = document.querySelector('#phone').value

	if (tickets.length != 0) {
		fetch(`/order/create/api`, {
			method: 'POST',
			body: JSON.stringify({
					name: name,
					email: email,
					phone: phone,
					tickets: tickets
			}),
			headers: {'X-CSRFToken': csrftoken}
		})
		.then(response => response.json())
		.then(result => {
			if (result.error) {
				alert(result.error)
				return
			} else {
				window.location = result.url
			}
		})
	} else {
		alert("Please add at least one ticket")
	}
}




ticketForm.addEventListener('submit', event => {
	event.preventDefault();

	const formData = new FormData(ticketForm);
	const name = formData.get('ticket-name');
	const type = formData.get('ticket-type');

	console.log(name, type)

	// check for ticket info before adding it
	if (name.length > 0 && type.length > 0) {
		let text = ''
		let price = 0

		switch (type) {
			case 'p':
				text = 'Parent';
				price = 150;
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
				text = 'Non Graduand';
				price = 100;
				break;
			case 'd':
				text = 'Graduand\'s Date';
				price = 250;
				break;
			default:
				text = 'Graduand';
				price = 550;
				break;
		}

		let newRow = invoiceTable.insertRow(-1)
		let typeCell = newRow.insertCell(0)
		let newType = document.createTextNode(text)
		typeCell.appendChild(newType)

		let nameCell = newRow.insertCell(1)
		let newName = document.createTextNode(name)
		nameCell.appendChild(newName)

		let numberCell = newRow.insertCell(2)
		let newNumber = document.createTextNode('')
		numberCell.appendChild(newNumber)

		let priceCell = newRow.insertCell(3)
		let newPrice = document.createTextNode(`$${price}.00`)
		priceCell.appendChild(newPrice)

		const newTicket = {
			'name': name,
			'type': type,
			'price': price
		}

		tickets.push(newTicket)

		// Add hidden inputs for each of the ticket
		const ticketName = document.createElement('input')
		ticketName.type = 'hidden'
		ticketName.name = `ticketName${ticketCount}`
		ticketName.value = name

		const ticketType = document.createElement('input')
		ticketType.type = 'hidden'
		ticketType.name = `ticketType${ticketCount}`
		ticketType.value = type

		orderForm.appendChild(ticketName)
		orderForm.appendChild(ticketType)

		ticketCount += 1;
		ticketCountInput.value = ticketCount

	} else {
		alert('Ticket info not filled in')
	}
	ticketForm.reset()
})

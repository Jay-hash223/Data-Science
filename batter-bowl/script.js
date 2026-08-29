const deliveryZones = {
  "522001": { name: "Guntur central", distance: 2 }, "522002": { name: "Arundelpet", distance: 3 },
  "522003": { name: "Kothapeta", distance: 4 }, "522004": { name: "Nallapadu", distance: 7 },
  "522005": { name: "Pattabhipuram", distance: 6 }, "522006": { name: "Brodipet", distance: 2 },
  "522007": { name: "Lakshmipuram", distance: 4 }, "522009": { name: "Srinagar", distance: 5 },
  "522017": { name: "Gorantla", distance: 8 }, "522034": { name: "Mangalagiri Road", distance: 10 }
};

const products = [
  { id: "idli", number: "01", name: "Idli Batter", description: "Cloud-soft idlis with a gentle, natural tang.", price: 80, size: "750 ml", mark: "idli" },
  { id: "dosa", number: "02", name: "Dosa Batter", description: "Your perfect crisp, with a choice of grain and flavour.", price: 100, size: "750 ml", mark: "dosa", options: ["Classic dosa", "Pesara dosa", "Millets dosa"], optionPrices: { "Classic dosa": 0, "Pesara dosa": 40, "Millets dosa": 80 } },
  { id: "garey", number: "03", name: "Garey Batter", description: "A savoury pour for golden, fluffy garelu.", price: 190, size: "750 ml", mark: "garey", options: ["Onion and masalas", "Plain batter"] },
  { id: "chutney", number: "04", name: "Chutneys", description: "Fresh accompaniments, available in morning hours on rotating days.", price: 60, size: "250 g", mark: "chutney", options: ["Coconut chutney", "Palli chutney", "Bengaluru style chutney"], optionPrices: { "Coconut chutney": 30, "Palli chutney": 30, "Bengaluru style chutney": 40 } }
];

const cart = {};
const productGrid = document.querySelector("#product-grid");
const cartDrawer = document.querySelector("#cart-drawer");
const cartItems = document.querySelector("#cart-items");
const cartCount = document.querySelector("#cart-count");
const drawerCount = document.querySelector("#drawer-count");
const cartTotal = document.querySelector("#cart-total");
const toast = document.querySelector("#toast");
const adminAccountKey = "batterBowlAdmin";
const ordersKey = "batterBowlOrders";
const customersKey = "batterBowlCustomers";
const loginEventsKey = "batterBowlLoginEvents";
const subscriptionsKey = "batterBowlSubscriptions";
const customerSessionKey = "batterBowlCustomerSignedIn";
const adminUsername = "Jayaram";
const adminPassword = "Amma@123";

function formatPrice(value) {
  return `₹${value.toLocaleString("en-IN")}`;
}

function getOptionPrice(product, option) {
  return product.price + (product.optionPrices?.[option] || 0);
}

function getCartKey(product, option) {
  return `${product.id}:${option}`;
}

function getOrders() { return JSON.parse(localStorage.getItem(ordersKey) || "[]"); }
function getStoredList(key) { return JSON.parse(localStorage.getItem(key) || "[]"); }

function renderAdminOrders() {
  const orders = getOrders();
  document.querySelector("#order-count-label").textContent = `${orders.length} order${orders.length === 1 ? "" : "s"}`;
  document.querySelector("#login-count-label").textContent = getStoredList(loginEventsKey).length;
  document.querySelector("#customer-count-label").textContent = getStoredList(customersKey).length;
  document.querySelector("#subscription-count-label").textContent = getStoredList(subscriptionsKey).length;
  document.querySelector("#empty-orders").hidden = orders.length > 0;
  document.querySelector("#admin-orders").innerHTML = orders.map((order) => `<tr><td><strong>${order.id}</strong><small>${order.date}</small></td><td><strong>${order.name}</strong><small>${order.contact}</small><small>${order.address}</small></td><td>${order.items.map((item) => `${item.name} (${item.option}) x${item.quantity}`).join("<br />")}</td><td>${order.pincode}<small>${order.distance} km · ${formatPrice(order.deliveryFee)}</small></td><td><strong>${formatPrice(order.total)}</strong><small>${order.payment}</small></td><td><select data-order-status="${order.id}" aria-label="Update status for ${order.id}">${["Order placed", "Being prepared", "Out for delivery", "Delivered"].map((status) => `<option ${status === order.status ? "selected" : ""}>${status}</option>`).join("")}</select></td></tr>`).join("");
}

function setAdminView(isLoggedIn) {
  document.querySelector("#admin-auth").hidden = isLoggedIn;
  document.querySelector("#admin-dashboard").hidden = !isLoggedIn;
  document.querySelector("#admin-logout").hidden = !isLoggedIn;
  if (isLoggedIn) renderAdminOrders();
}

function renderProducts() {
  productGrid.innerHTML = products.map((product) => `
    <article class="product-card">
      <span class="product-number">${product.number}</span>
      <span class="product-illustration" aria-hidden="true">${product.mark}</span>
      <h3>${product.name}</h3>
      <p>${product.description}</p>
      ${product.options ? `<label class="option-label" for="option-${product.id}">Choose style<select id="option-${product.id}" data-option="${product.id}">${product.options.map((option) => `<option>${option}</option>`).join("")}</select></label>` : ""}
      <div class="product-footer">
        <span class="product-price">${formatPrice(product.price)} <small>/ ${product.size}</small></span>
        <button class="add-button" type="button" data-add="${product.id}" aria-label="Add ${product.name} to bag">+</button>
      </div>
    </article>
  `).join("");
}

function getCartEntries() {
  return Object.entries(cart).map(([key, item]) => ({ ...item, key, product: products.find((product) => product.id === item.productId) }));
}

function renderCart() {
  const entries = getCartEntries();
  const itemCount = entries.reduce((sum, item) => sum + item.quantity, 0);
  const total = entries.reduce((sum, item) => sum + item.price * item.quantity, 0);
  cartCount.textContent = itemCount;
  drawerCount.textContent = `(${itemCount})`;
  cartTotal.textContent = formatPrice(total);

  if (!entries.length) {
    cartItems.innerHTML = '<p class="empty-cart">Your bag is waiting for something delicious.</p>';
    return;
  }

  cartItems.innerHTML = entries.map((item) => `
    <div class="cart-item">
      <div class="cart-item-art" aria-hidden="true">${item.product.mark}</div>
      <div class="cart-item-info"><strong>${item.product.name}</strong><small>${item.option} · ${item.product.size} · ${formatPrice(item.price)}</small></div>
      <div class="quantity-control"><button type="button" data-action="decrease" data-id="${item.key}" aria-label="Remove one ${item.product.name}">−</button><span>${item.quantity}</span><button type="button" data-action="increase" data-id="${item.key}" aria-label="Add one ${item.product.name}">+</button></div>
      <span class="cart-item-price">${formatPrice(item.price * item.quantity)}</span>
    </div>
  `).join("");
}

function showToast(message) {
  toast.textContent = message;
  toast.classList.add("show");
  window.setTimeout(() => toast.classList.remove("show"), 2200);
}

function openCart() {
  cartDrawer.classList.add("is-open");
  cartDrawer.setAttribute("aria-hidden", "false");
}

function closeCart() {
  cartDrawer.classList.remove("is-open");
  cartDrawer.setAttribute("aria-hidden", "true");
}

productGrid.addEventListener("click", (event) => {
  const button = event.target.closest("[data-add]");
  if (!button) return;
  const product = products.find((item) => item.id === button.dataset.add);
  const selector = productGrid.querySelector(`[data-option="${product.id}"]`);
  const option = selector ? selector.value : "Classic recipe";
  const key = getCartKey(product, option);
  cart[key] = { productId: product.id, option, price: getOptionPrice(product, option), quantity: (cart[key]?.quantity || 0) + 1 };
  renderCart();
  showToast(`${product.name} added to your bag`);
});

cartItems.addEventListener("click", (event) => {
  const button = event.target.closest("[data-action]");
  if (!button) return;
  const id = button.dataset.id;
  cart[id].quantity += button.dataset.action === "increase" ? 1 : -1;
  if (cart[id].quantity <= 0) delete cart[id];
  renderCart();
});

document.querySelector("#cart-button").addEventListener("click", openCart);
document.querySelector("#close-cart").addEventListener("click", closeCart);
document.querySelector("#drawer-backdrop").addEventListener("click", closeCart);
document.querySelector("#checkout-button").addEventListener("click", () => {
  if (!getCartEntries().length) {
    showToast("Add a pouch before checking out");
    return;
  }
  document.querySelector("#checkout-total").textContent = formatPrice(getTotal());
  document.querySelector("#items-total").textContent = formatPrice(getTotal());
  updateCheckoutTotal();
  document.querySelector("#checkout-modal").classList.add("is-open");
  document.querySelector("#checkout-modal").setAttribute("aria-hidden", "false");
});
function getTotal() { return getCartEntries().reduce((sum, item) => sum + item.price * item.quantity, 0); }
function getDeliveryZone() { return deliveryZones[document.querySelector("#pincode").value.trim()]; }
function updateCheckoutTotal() {
  const zone = getDeliveryZone();
  const deliveryFee = zone ? zone.distance * 5 : 0;
  document.querySelector("#delivery-distance").textContent = zone ? zone.distance : 0;
  document.querySelector("#delivery-fee").textContent = formatPrice(deliveryFee);
  document.querySelector("#items-total").textContent = formatPrice(getTotal());
  document.querySelector("#checkout-total").textContent = formatPrice(getTotal() + deliveryFee);
  document.querySelector("#pincode-message").textContent = zone ? `${zone.name}: ${zone.distance} km route · ${formatPrice(deliveryFee)} delivery` : "Enter a supported Guntur Urban pincode.";
  document.querySelector("#pincode-message").classList.toggle("is-valid", Boolean(zone));
}
function closeCheckout() { document.querySelector("#checkout-modal").classList.remove("is-open"); document.querySelector("#checkout-modal").setAttribute("aria-hidden", "true"); }
document.querySelector("#close-checkout").addEventListener("click", closeCheckout);
document.querySelector("#modal-backdrop").addEventListener("click", closeCheckout);
document.querySelector("#checkout-form").addEventListener("submit", (event) => {
  event.preventDefault();
  const formData = new FormData(event.currentTarget);
  const zone = getDeliveryZone();
  if (!zone) { document.querySelector("#pincode-message").textContent = "Sorry, this pincode is outside our Guntur Urban delivery area."; return; }
  const orderId = `${String.fromCharCode(65 + Math.floor(Math.random() * 26))}${String.fromCharCode(65 + Math.floor(Math.random() * 26))}-${Math.floor(Math.random() * 21)}`;
  const orderItems = getCartEntries().map((item) => ({ name: item.product.name, option: item.option, quantity: item.quantity }));
  const deliveryFee = zone.distance * 5;
  const order = { id: orderId, name: formData.get("name"), contact: formData.get("contact"), address: formData.get("address"), pincode: formData.get("pincode"), distance: zone.distance, deliveryFee, payment: formData.get("payment"), items: orderItems, total: getTotal() + deliveryFee, status: "Order placed", date: new Date().toLocaleString("en-IN") };
  localStorage.setItem(ordersKey, JSON.stringify([order, ...getOrders()]));
  document.querySelector("#order-id").textContent = orderId;
  document.querySelector("#order-summary").textContent = `Thanks, ${formData.get("name")}. We will deliver to ${formData.get("address")}, Guntur Urban. Delivery: ${zone.distance} km at ${formatPrice(zone.distance * 5)}.`;
  document.querySelector("#tracking-steps").innerHTML = ["Order placed", "Being prepared", "Out for delivery", "Delivered"].map((step, index) => `<div class="tracking-step ${index === 0 ? "active" : ""}"><span>${index + 1}</span><strong>${step}</strong><small>${index === 0 ? "Now" : "Pending"}</small></div>`).join("");
  closeCheckout(); closeCart(); document.querySelector("#order-status").hidden = false; document.querySelector("#order-status").scrollIntoView({ behavior: "smooth" });
  Object.keys(cart).forEach((id) => delete cart[id]); renderCart(); showToast(`Order ${orderId} placed`);
});
document.querySelector("#feedback-button").addEventListener("click", () => { document.querySelector("#feedback-message").textContent = "Thank you for helping us make breakfast better."; });
document.querySelector(".stars").addEventListener("click", (event) => { const rating = Number(event.target.dataset.rating); document.querySelectorAll(".stars button").forEach((star, index) => star.classList.toggle("selected", index < rating)); });
document.querySelector("#pincode").addEventListener("input", updateCheckoutTotal);
document.querySelector("#delivery-button").addEventListener("click", () => {
  const message = document.querySelector("#delivery-message");
  message.textContent = "Manufactured in Guntur Urban. We deliver to 10 listed Guntur Urban pincodes at ₹5 per km. Enter your pincode at checkout to check eligibility.";
});

document.querySelector("#admin-button").addEventListener("click", () => { const panel = document.querySelector("#admin-panel"); panel.hidden = false; setAdminView(Boolean(sessionStorage.getItem("batterBowlAdminSignedIn"))); panel.scrollIntoView({ behavior: "smooth" }); });
document.querySelectorAll(".auth-tab").forEach((tab) => tab.addEventListener("click", () => { document.querySelectorAll(".auth-tab").forEach((item) => item.classList.toggle("active", item === tab)); document.querySelector("#admin-login-form").hidden = tab.dataset.auth !== "login"; document.querySelector("#admin-create-form").hidden = tab.dataset.auth !== "create"; }));
document.querySelector("#admin-login-form").addEventListener("submit", (event) => { event.preventDefault(); const data = Object.fromEntries(new FormData(event.currentTarget)); const message = document.querySelector("#login-message"); if (data.username !== adminUsername || data.password !== adminPassword) { message.textContent = "Use the assigned admin username and password."; return; } localStorage.setItem(adminAccountKey, JSON.stringify({ username: adminUsername, password: adminPassword })); sessionStorage.setItem("batterBowlAdminSignedIn", "true"); message.textContent = ""; setAdminView(true); });
document.querySelector("#admin-logout").addEventListener("click", () => { sessionStorage.removeItem("batterBowlAdminSignedIn"); setAdminView(false); });
document.querySelector("#admin-orders").addEventListener("change", (event) => { const id = event.target.dataset.orderStatus; if (!id) return; const orders = getOrders().map((order) => order.id === id ? { ...order, status: event.target.value } : order); localStorage.setItem(ordersKey, JSON.stringify(orders)); showToast(`${id} updated`); });

function setCustomerView(customer) { document.querySelector("#customer-auth").hidden = Boolean(customer); document.querySelector("#subscription-panel").hidden = !customer; document.querySelector("#customer-logout").hidden = !customer; if (customer) document.querySelector("#customer-greeting").textContent = customer.name; }
document.querySelector("#customer-button").addEventListener("click", () => { const panel = document.querySelector("#customer-panel"); panel.hidden = false; setCustomerView(JSON.parse(sessionStorage.getItem(customerSessionKey) || "null")); panel.scrollIntoView({ behavior: "smooth" }); });
document.querySelector("#customer-create-form").addEventListener("submit", (event) => { event.preventDefault(); const data = Object.fromEntries(new FormData(event.currentTarget)); const customers = getStoredList(customersKey).filter((customer) => customer.contact !== data.contact); customers.push({ name: data.name, contact: data.contact }); localStorage.setItem(customersKey, JSON.stringify(customers)); document.querySelector("#customer-create-message").textContent = "Account created. Send a verification code to sign in."; });
document.querySelector("#send-code-button").addEventListener("click", () => { const contact = document.querySelector("#customer-login-form input[name='contact']").value.trim(); const code = Math.floor(1000 + Math.random() * 9000); sessionStorage.setItem("batterBowlLoginCode", JSON.stringify({ contact, code })); document.querySelector("#customer-login-message").textContent = `Demo 4-digit code sent to ${contact}: ${code}`; });
document.querySelector("#customer-login-form").addEventListener("submit", (event) => { event.preventDefault(); const data = Object.fromEntries(new FormData(event.currentTarget)); const customer = getStoredList(customersKey).find((item) => item.contact === data.contact); const loginCode = JSON.parse(sessionStorage.getItem("batterBowlLoginCode") || "null"); const message = document.querySelector("#customer-login-message"); if (!customer) { message.textContent = "Create a customer account with this email or phone first."; return; } if (!loginCode || loginCode.contact !== data.contact || String(loginCode.code) !== String(data.code)) { message.textContent = "Request a new verification code and enter it correctly."; return; } const loginEvents = getStoredList(loginEventsKey); loginEvents.push({ contact: customer.contact, at: new Date().toISOString() }); localStorage.setItem(loginEventsKey, JSON.stringify(loginEvents)); sessionStorage.setItem(customerSessionKey, JSON.stringify(customer)); sessionStorage.removeItem("batterBowlLoginCode"); message.textContent = ""; setCustomerView(customer); showToast(`Welcome back, ${customer.name}`); });
document.querySelector("#customer-logout").addEventListener("click", () => { sessionStorage.removeItem(customerSessionKey); setCustomerView(null); });
document.querySelector("#subscription-frequency").addEventListener("change", (event) => { document.querySelector("#custom-dates-label").hidden = event.target.value !== "custom"; });
document.querySelector("#subscription-form").addEventListener("submit", (event) => { event.preventDefault(); const customer = JSON.parse(sessionStorage.getItem(customerSessionKey) || "null"); if (!customer) return; const data = Object.fromEntries(new FormData(event.currentTarget)); const subscription = { customer: customer.email, item: data.item, frequency: data.frequency, dates: data.frequency === "custom" ? data.dates.split(",").map((date) => date.trim()).filter(Boolean) : "daily", createdAt: new Date().toISOString() }; const subscriptions = getStoredList(subscriptionsKey).filter((item) => !(item.customer === customer.email && item.item === data.item)); subscriptions.push(subscription); localStorage.setItem(subscriptionsKey, JSON.stringify(subscriptions)); document.querySelector("#subscription-message").textContent = data.frequency === "daily" ? "Daily delivery subscription saved." : "Your custom delivery dates are saved."; });

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") { closeCart(); closeCheckout(); }
});

renderProducts();
renderCart();

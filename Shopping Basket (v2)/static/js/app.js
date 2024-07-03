// select element for Modal
const cartBtn = document.querySelector(".cart-btn")
const cartModal = document.querySelector(".cart")
const backDrop = document.querySelector(".backdrop")
const closeModal = document.querySelector(".cart-item-confirm")

// select element for Products
const productsDOM = document.querySelector('.products-center')
const cartTotal = document.querySelector('.cart-total')
const cartItems = document.querySelector('.cart-items')
const cartContent = document.querySelector('.cart-content')
const clearCart = document.querySelector('.clear-cart')


// products
const productsData = [
  {
    id: 1,
    title: "queen panel bed",
    price: 10.99,
    imageUrl: "static/images/product-1.jpeg",
  },
  {
    id: 2,
    title: "reza panel bed",
    price: 14.99,
    imageUrl: "static/images/product-2.jpeg",
  },
  {
    id: 3,
    title: "once panel bed",
    price: 7.99,
    imageUrl: "static/images/product-3.jpeg",
  },
  {
    id: 4,
    title: "twin panel bed",
    price: 11.99,
    imageUrl: "static/images/product-4.jpeg",
  },
  {
    id: 5,
    title: "fridge",
    price: 4.99,
    imageUrl: "static/images/product-5.jpeg",
  },
  {
    id: 6,
    title: "fridge",
    price: 23.99,
    imageUrl:"static/images/product-6.jpeg",
  },
  {
    id: 7,
    title: "dresser",
    price: 42.99,
    imageUrl: "static/images/product-7.jpeg",
  },
  {
    id: 8,
    title: "couch",
    price: 24.99,
    imageUrl: "static/images/product-8.jpeg",
  },
]
let cart = []
let getAddToCartBtns = []
let buttonsDOM = []


// display products
function displayProducts(products) {
  let result = ''
  products.forEach(product => {
    result += `<div class="product">
    <div class="img-container">
      <img src="${product.imageUrl}" class="product-img" />
    </div>
    <div class="product-desc">
      <p class="product-price">$ ${product.price}</p>
      <p class="product-title">${product.title}</p>
    </div>
    <button class="btn add-to-cart" data-id="${product.id}">
      add to cart
    </button>
    </div>`
  })
  productsDOM.innerHTML = result

  const addToCarBtns = [...document.querySelectorAll('.add-to-cart')]
  getAddToCartBtns = [...addToCarBtns]
  buttonsDOM = [...addToCarBtns]
}

function getAddToCartBtn() {
  getAddToCartBtns.forEach(btn => {
    const id = btn.dataset.id
    const isInCart = cart.find(p => p.id === parseInt(id))
    if (isInCart) {
      btn.textContent = 'In Cart'
      btn.disabled = true
    }
    btn.addEventListener('click', e => {
      e.target.textContent = 'In Cart'
      e.target.disabled = true
      const addedProduct = { ...getProduct(id), quantity: 1 }
      cart = [...cart, addedProduct]
      saveCart(cart)
      setCartValue(cart)
      addCartItem(addedProduct)
    })
  })
}

function setCartValue(cart) {
  let tempCartItems = 0
  const totalPrice = cart.reduce((acc, curr) => {
    tempCartItems += curr.quantity
    return acc + curr.price * curr.quantity
  }, 0)
  cartTotal.textContent = `total price : ${totalPrice.toFixed(2)} $`
  cartItems.textContent = tempCartItems
}

function addCartItem(cartItem) {
  let result = `<div class="cart-item">
  <img class="cart-item-img" src="${cartItem.imageUrl}" />
  <div class="cart-item-desc">
    <h4>${cartItem.title}</h4>
    <h5>$ ${cartItem.price}</h5>
  </div>
  <div class="cart-item-conteoller">
    <i class="fas fa-chevron-up" data-id="${cartItem.id}"></i>
    <p>${cartItem.quantity}</p>
    <i class="fas fa-chevron-down" data-id="${cartItem.id}"></i>
  </div>
  <i class="far fa-trash-alt" data-id="${cartItem.id}"></i>
  </div>`
  cartContent.innerHTML += result
}

function setUpApp() {
  cart = getCart() || []
  cart.forEach(cartItem => addCartItem(cartItem))
  setCartValue(cart)
}

function cartLogic() {
  clearCart.addEventListener('click', () => clearCart2())
  cartContent.addEventListener('click', e => {
    if (e.target.classList.contains('fa-chevron-up')) {
      const addQuantity = e.target
      const addedItem = cart.find(cItem => cItem.id == addQuantity.dataset.id)
      addedItem.quantity++
      setCartValue(cart)
      saveCart(cart)
      addQuantity.nextElementSibling.textContent = addedItem.quantity
    } else if (e.target.classList.contains('fa-trash-alt')) {
      const removeItem = e.target
      const removedItem = cart.find(cItem => cItem.id == removeItem.dataset.id)
      removeItem2(removedItem.id)
      saveCart(cart)
      cartContent.removeChild(removeItem.parentElement)
    } else if (e.target.classList.contains('fa-chevron-down')) {
      const subQunatity = e.target
      const substractedItem = cart.find(cItem => cItem.id == subQunatity.dataset.id)
      if(substractedItem.quantity === 1) {
        removeItem2(substractedItem.id)
        cartContent.removeChild(subQunatity.parentElement.parentElement)
        return
      }
      substractedItem.quantity--
      setCartValue(cart)
      saveCart(cart)
      subQunatity.previousElementSibling.textContent = substractedItem.quantity
    }
  })
}

function clearCart2() {
  cart.forEach(cItem => removeItem2(cItem.id))
  while (cartContent.children.length) {
    cartContent.removeChild(cartContent.children[0])
  }
  closeModalFunction()
}

function removeItem2(id) {
  cart = cart.filter(cItem => cItem.id !== id)
  setCartValue(cart)
  saveCart(cart)
  getSingleButton(id)
}

function getSingleButton(id) {
  const button = buttonsDOM.find(btn => btn.dataset.id == id)
  button.textContent = 'add to cart'
  button.disabled = false
}



// localStorage
function saveProducts(products) {
  localStorage.setItem('products', JSON.stringify(products))
}

function getProduct(id) {
  const _products = JSON.parse(localStorage.getItem('products'))
  return _products.find(p => p.id == id)
}

function saveCart(cart) {
  localStorage.setItem('cart', JSON.stringify(cart))
}

function getCart() {
  return JSON.parse(localStorage.getItem('cart'))
}



// show and save products when DOM loaded
document.addEventListener('DOMContentLoaded', () => {
  displayProducts(productsData)
  setUpApp()
  getAddToCartBtn()
  cartLogic()
  saveProducts(productsData)
})



// functions - Modal
function showModalFunction() {
  backDrop.style.display = "block"
  cartModal.style.opacity = "1"
  cartModal.style.top = "20%"
}

function closeModalFunction() {
  backDrop.style.display = "none"
  cartModal.style.opacity = "0"
  cartModal.style.top = "-100%"
}

// event - modal
cartBtn.addEventListener("click", showModalFunction)
closeModal.addEventListener("click", closeModalFunction)
backDrop.addEventListener("click", closeModalFunction)